import sys
import datetime

filename=sys.argv[1]
with open(filename,"r",encoding="utf-8") as f:
	with open("char-list.txt","r",encoding="utf-8") as c:
		with open("lookedfor-"+str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))+".txt","w",encoding="utf-8") as n:
			chars=set()
			load_chars=set()
			for lchar in c.read():
				load_chars.add(lchar)
			for char in f.read():
				chars.add(char)
			unexist=chars - load_chars
			n.write("".join(map(str,list(unexist))))
