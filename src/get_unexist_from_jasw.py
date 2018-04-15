import mw_api_client as mw
# Requires Kenny2github's code

jasw=mw.Wiki("https://ja.scratch-wiki.info/w/api.php","GetPage by Apple502j via mw-api-client")
randoms=jasw.random(limit=50,namespace=0)
for page in randoms:
		with open("char-list.txt","r",encoding="utf-8") as c:
			with open("lookedfor-wiki.txt","a",encoding="utf-8") as n:
				chars=set()
				load_chars=set()
				for lchar in c.read():
					load_chars.add(lchar)
				for char in page.read():
					chars.add(char)
				unexist=chars - load_chars
				n.write("".join(map(str,list(unexist))))
				print("Checked page " + page.title)
