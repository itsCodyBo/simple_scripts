def main():
	
	return 0
if __name__ == '__main__':
	main()

#take an input of the phrase and split it into individual words
x = raw_input('Enter a 5 worded phrase:')
x = x.split()
#print each word on its own line
print '******'
for i in x:
	print '**' + str(i) + '**'
print '******'
	



#ask user to enter 5 names and display in alphabetical order
namelst = []
name1 = raw_input("what is the first name?")
namelst.append(name1)
name2 = raw_input("what is the second name?")
namelst.append(name2)
name3 = raw_input("what is the third name?")
namelst.append(name3)
name4 = raw_input("what is the fourth name?")
namelst.append(name4)
name5 = raw_input("what is the final name?")
namelst.append(name5)
namelst.sort()
print namelst
	
#same as prevous code, but only returns the second name the user types in
namelst = []
name1 = raw_input("what is the first name?")
namelst.append(name1)
name2 = raw_input("what is the second name?")
namelst.append(name2)
name3 = raw_input("what is the third name?")
namelst.append(name3)
name4 = raw_input("what is the fourth name?")
namelst.append(name4)
name5 = raw_input("what is the final name?")
namelst.append(name5)
print name2

#same code as prevous, but gives the option to change a name
namelst = []
name1 = raw_input("what is the first name?")
namelst.append(name1)
name2 = raw_input("what is the second name?")
namelst.append(name2)
name3 = raw_input("what is the third name?")
namelst.append(name3)
name4 = raw_input("what is the fourth name?")
namelst.append(name4)
name5 = raw_input("what is the final name?")
namelst.append(name5)

namechange =  raw_input("Enter a name to change or type none")
if namechange == name1:
	new_name1=raw_input("what is the new name?")
	namelst.append(name1)
	print namelst
elif namechange == name2:
	new_name2=raw_input("what is the new name?")
	namelst.append(new_name2)
	print namelst
elif namechange == name3:
	new_name3=raw_input("what is the new name?")
	namelst.append(new_name3)
	print namelst
elif namechange == name4:
	new_name4=raw_input("what is the new name?")
	namelst.append(new_name4)
	print namelst
elif namechange == name5:
	new_name5=raw_input("what is the new name?")
	namelst.append(new_name5)
	print namelst
elif namechange == 'none':
	print namelst
else:
	print namelst
