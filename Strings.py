#1. Find occurrence of count..


string=input("Enter a string: ")
dict1={}
#occurance of each character in string
for i in string:
    if i not in dict1:
        dict1[i]=1
        print(dict1)    
    else:
        dict1[i]+=1
#display result
for k,v in sorted(dict1.items()):
    print(k,"=",v)

#------------------------------------------
#2. Reverse string at that position 


#output:olleH nohtyp dna ognajD

str="Hello python and Django"
lis2=[]
lis1=str.split()
print(lis1)
for j in lis1:
    lis2.append("".join(reversed(j)))
print(" ".join(lis2))

             #OR

3.
str="Hello python and Django"
#lis2=[]
lis1=str.split()
for i in lis1:
    print(i[::-1],end=" ")
