from zipfile import ZipFile
import zipfile
import sys
import os
l=len(sys.argv)
def file_accessible(filepath, mode):
    try:
        f = open(filepath, mode)
        f.close()
    except IOError as e:
        return False
    return True
if l<2:
	print("GIVE AT LEAST ONE FILE")
	exit()
f=input("ENTER NAME OF ZIP FILE WITHOUT .ZIP EXTENSION ")
dir=os.getcwd()
dir=dir+'\\'+f+'.zip'
if file_accessible(dir,'r'):
	ch=input("FILE ALREADY THERE,PRESS E TO EXIT O TO OVERWRITE OTHERWISE APPENDS TO IT ")
	if(ch.lower()=='e'):
		exit()
	elif (ch.lower()=='o'):
		os.remove(dir)
for x in range(1,l):
	with ZipFile(dir, 'a') as myzip:
		try:
			print(os.getcwd())
			myzip.write(sys.argv[x])
			print(sys.argv[x]+" IS COMPRESSED")
		except IOError as e:
			print(sys.argv[x]+" NOT FOUND")
			s=input("ENTER exit TO EXIT ")
			if s.lower()=='exit':
				exit()

