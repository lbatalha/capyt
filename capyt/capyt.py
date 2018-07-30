#!/usr/bin/env python3
import requests
import sys, fileinput, argparse, copy
from urllib.parse import urlparse
from os.path import splitext
if __name__ == '__main__':	
	from __init__ import __version__
else:
	from . import __version__

url = 'https://cpy.pt/'

headers = {
	'User-Agent': 'capyt/{}'.format(__version__,)
}

parser = argparse.ArgumentParser(description="CLI Utility to interact with pastething")
parser.add_argument('-v', '--version', action='version', version=__version__)
parser.add_argument('-d', '--delete', help="Delete paste with supplied delete token")
parser.add_argument('-b', '--burn', type=int, help="Maximum number of paste views before deletion")
parser.add_argument('-l', '--lexer', help="Lexer to use (pygments get_lexer_by_name)", default="auto")
parser.add_argument('-t', '--ttl', type=float, help="Time in hours before paste expires", default=1.0)
parser.add_argument('-r', '--raw', help="Weather to have pastebin return raw or html paste url", default='false')
parser.add_argument('-e', '--encoding', help="Define file encoding for given file (default: utf-8)")

parser.add_argument('FILE', help="Files to upload", nargs="+") #Re-used as paste ID or URL when deleting
args = vars(parser.parse_args())


#add encoding option to compressed hook
def hook_compressed_encoded(encoding):
	def hook_compressed(filename, mode):
		ext = splitext(filename)[1]
		if ext == '.gz':
			import gzip
			return gzip.open(filename, mode, encoding=encoding)
		elif ext == '.bz2':
			import bz2
			return bz2.BZ2File(filename, mode, encoding=encoding)
		else:
			return open(filename, mode, encoding=encoding)
	return hook_compressed

def main():
	global url
	global headers

	if args['delete']:
		paste = urlparse(args['FILE'][0])
		if paste[0] != '':
			url = args['FILE'][0]
		else:
			url = url + paste[2]

		print("DELETE ", url)
		try:
			r = requests.delete(url, data={"token": args['delete']}, headers=headers)
			print(r.text)
			if r.status_code != 200:
				exit(1)
		except requests.ConnectionError:
			print("Connection to host failed")
			exit(2)
	else:
		parameters = copy.deepcopy(args)
		del parameters['FILE']

		with fileinput.input(files=args['FILE'], openhook=hook_compressed_encoded(args['encoding'])) as f:
			parameters['paste'] = ''.join(f)
			try:
				r = requests.post(url, data=parameters, headers=headers)
				print(r.text)
				if r.status_code != 200:
					exit(1)
			except requests.ConnectionError:
				print("Connection to host failed")
				exit(2)

if __name__ == "__main__":
	main()
