#!/usr/bin/env python3

import requests
import sys, fileinput, argparse, copy

url = 'https://cpy.pt/'

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--burn', type=int, help="Maximum number of paste views before deletion")
parser.add_argument('-l', '--lexer', help="Lexer to use (pygments get_lexer_by_name)", default="auto")
parser.add_argument('-t', '--ttl', type=float, help="Time before paste is deleted", default=1.0)
parser.add_argument('-r', '--raw', help="Wether to have pastebin return raw or html paste url", default='true')

parser.add_argument('FILE', help="Files to Upload", nargs="+")
args = vars(parser.parse_args())

parameters = copy.deepcopy(args)
del parameters['FILE']

with fileinput.input(files=args['FILE'], openhook=fileinput.hook_compressed) as f:
	parameters['paste'] = ''.join(f)
	r = requests.post(url, data=parameters)
	print(r.text)




