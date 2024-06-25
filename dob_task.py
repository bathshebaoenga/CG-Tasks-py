Name = []
birthdate=[]

f= open('DOB.txt','r')
#f is open for reading.

for line in f :
    parts= line.split()
    Name.append(parts[:2])  #stores the names
    birthdate.append(parts[2:]) #stores the birthdates

f.close() #closing file as now finished with it 

print("name")
for i , Name in enumerate(Name, start = 1):
    print("{}.{}".format(i, " ".join(Name)))
print("birthdate")
for i , birthdate in enumerate(birthdate, start = 1):
    print("{}.{}". format(i , " ".join(birthdate)))
