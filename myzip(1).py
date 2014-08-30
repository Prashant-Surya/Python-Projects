#!/usr/bin/env python3
from zipfile import ZipFile
import sys
l=len(sys.argv)
for x in range(1,l):
	with ZipFile('second.zip', 'a') as myzip:
		print(sys.argv[x]+" is compressed")
		myzip.write(sys.argv[x]) 
