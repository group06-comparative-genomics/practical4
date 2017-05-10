f1 = open("03.blastphit.txt","r")
f2 = open("08.blastphit.txt","r")
f3 = open("18.blastphit.txt","r")
f4 = open("orthologues.txt","w")
dict03 = {}
list03 = []
for line in f1:
	line=line.rstrip()
	line= line.split (' ')
	dict03[line[0]] = line [1]
	list03.append(line[0])

dict08 = {}
list08 = []
for line in f2:
	line= line.rstrip()
	line= line.split (' ')
	dict08[line[0]] = line [1]
	list08.append(line[0])
	
list18 = []
dict18 = {}
for line in f3:
	line= line.rstrip()
	line= line.split (' ')
	dict18[line[0]] = line [1]
	list18.append(line[0])
set03 = set(dict03.keys())
set08 = set(dict08.keys())
set18 = set(dict18.keys())
intersection = set03 & set08 & set18

print (len(list03))
print (len(list08))
print (len(list18))
print (len(intersection))

for item in intersection:
	f4.write(item + " " + dict03[item] +" " +dict08[item] +" " + dict18[item] + "\n")
	
