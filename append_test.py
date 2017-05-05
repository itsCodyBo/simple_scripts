
def pig_latin(name):
	for x in name:
		lst=[]
		lst.append(x)
		print lst,

print pig_latin("cody")

prefixes="JKLMNOPQ"
suffix="ack"
for letter in prefixes:
	print letter + suffix,
