import argparse

import urllib2
import urllib

class Pyget(object):
	def __init__(self, url, out='', recursive=False):
		self.url = url
		self.file_name = out
		
		if out <> '':
			self.file_name = self.url.split('/')[-1]
			self.file_name = urllib.unquote_plus(self.file_name)
			
		if recursive:
			self.file_name = self.url.split('/')[-1]
			self.file_name = urllib.unquote_plus(self.file_name)
			#TODO: recurse action
		else:
			self.url_download(self.url)
			
	def url_download(self, url):
		u = urllib2.urlopen(url)
		f = open(self.file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		print "Downloading: %s Bytes: %s" % (self.file_name, file_size)

		file_size_dl = 0
		block_sz = 8192
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break

			file_size_dl += len(buffer)
			f.write(buffer)
			status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
			status = status + chr(8)*(len(status)+1)
			print status,

		f.close()
	
	
if __name__ == '__main__':
	#parsing CLI arguments
	parser = argparse.ArgumentParser(description= "Small wget-like program. For your eyes only.")
	parser.add_argument('url', type=str, help='URL of file to downoad')
	parser.add_argument('--out', type=str, help='Name of output file')
	parser.add_argument('--r', action='store_true', help='Recursively download files linked in the URL')
	
	args = parser.parse_args()
	
	Pyget(url=args.url, out=args.out, recursive=args.r)