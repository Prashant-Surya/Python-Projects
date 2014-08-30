#! /usr/bin/python3
dictio={'a': 1,'b': 3,'c': 3,'d': 2,'e': 1,'f': 4,'g': 2,'h': 4,'i': 1,'j': 8,'k': 5,'l': 1,'m': 3,'n': 1,'o': 1,'p': 3,'q': 10,'r': 1,'s': 1,'t': 1,'u': 1,'v': 4,'w': 4,'x': 8,'y': 4,'z': 10}
def main():
	count=0
	while True:
		s=input("Enter any input or quit to exit:\n").lower()
		if len(s)>15:
			print("Size "+str(len(s))+" greater than 15")
			continue
		elif not s.isalpha():
			print("Enter only alphabets")
			continue
		elif s=='quit':
			break
		else:
			for x in s:
				count+=dictio[x]
			print("Score for the word "+s+" is "+str(count));
if __name__ == '__main__':
	main()
