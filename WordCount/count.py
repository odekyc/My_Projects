from collections import Counter
filename = open("article.txt", 'r+')
mystring=filename.read()
exceptions=['\n', '.', '?', ',', '(', ')', '-', '"','_', ',', '  ', ' ']
for i in exceptions:
	stringarray=mystring.split(i)
	mystring=" ".join(stringarray)

print (stringarray)
mydic={}

for word in stringarray:

	mydic[word]=stringarray.count(word)
	

newdic=((dict(Counter(mydic).most_common(5))))
dic2=dict(zip(newdic.values(), newdic.keys()))

list1=sorted(dic2.keys())
list1.reverse()

print (list1)

for num in list1:
	print(dic2[num] + " : " + str(num))
 
