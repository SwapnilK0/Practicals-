bk=[]
pr=[]

n=int(input("Enter Number of Books : "))
i=0
j=0
while (i<n):
	bk.append(input("Enter Name of Book "))
	pr.append(int(input("Enter Price of Book ")))
	
	i+=1


def f1(j):
	thisdict={}
	while j<n:
		#thisdict[bk[i]] = pr[i]
		thisdict.update({bk[j]: pr[j]})
		j=j+1
	
	return thisdict

def f2(thisdict):
	f2=[]
	for i in sorted(thisdict.values()):
		if i not in f2:
			f2.append(i)
			print([k for k, v in thisdict.items() if v == i],"\t: ", i)

def f3(thisdict):
	f3=[]
	for i in thisdict.values():
		if i>500:
			if i not in f3:
				f3.append(i)
				print([k for k, v in thisdict.items() if v == i],"\t: ", i)
	

def f4(thisdict):
	f4=[]
	for i in thisdict.values():
		if i<500:
			if i not in f4:
				f4.append(i)
				print([k for k, v in thisdict.items() if v == i],"\t: ", i)
	

		
while True:
	print("\n1. Delete Duplicate Entries")
	print("\n2. In Ascending Based on cost")
	print("\n3. No. of Books Cost Greater Than 500")
	print("\n4. Books Cost Less Than 500")
	print("\n5. Exit")
	
	I = input("\nEnter Your Choice: ")
	if I == '1':
		print(f1(j))
	elif I == '2':
		f2(f1(j))
	elif I == '3':
		f3(f1(j))

	elif I == '4':
		f4(f1(j))
		
	elif I == '5':
		exit()
	else:
		print("Please, Enter Valid Input")
	print("------------------------------------------------------------------------")
	
