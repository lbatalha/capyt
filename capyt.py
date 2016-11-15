#!/usr/bin/env python3

import requests
import sys, fileinput, argparse, copy
from urllib.parse import urlparse

url = 'https://cpy.pt/'

parser = argparse.ArgumentParser(description="CLI Utility to interact with pastething")

parser.add_argument('-d', '--delete', help="Delete paste with supplied delete token")
parser.add_argument('-b', '--burn', type=int, help="Maximum number of paste views before deletion")
parser.add_argument('-l', '--lexer', help="Lexer to use (pygments get_lexer_by_name)", default="auto")
parser.add_argument('-t', '--ttl', type=float, help="Time in hours before paste expires", default=1.0)
parser.add_argument('-r', '--raw', help="Weather to have pastebin return raw or html paste url", default='true')

parser.add_argument('FILE', help="Files to upload", nargs="+") #Re-used as paste ID or URL when deleting
args = vars(parser.parse_args())

if args['delete']:
	paste = urlparse(args['FILE'][0])
	if paste[0] != '':
		url = args['FILE'][0]
	else:
		url = url + paste[2]
	
	print("DELETE ", url)
	r = requests.delete(url, data={"token": args['delete']})
	print(r.text)
	if r.status_code != 200:
		exit(1)

else:
	parameters = copy.deepcopy(args)
	del parameters['FILE']

	with fileinput.input(files=args['FILE'], openhook=fileinput.hook_compressed) as f:
		parameters['paste'] = ''.join(f)
		r = requests.post(url, data=parameters)
		print(r.text)
		if r.status_code != 200:
			exit(1)
