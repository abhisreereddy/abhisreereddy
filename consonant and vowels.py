str=input("enter the string:")
vow='aeiouAEIOU'
v=c=0
rep=[]
print("vowels in the string:\n")
for i in str:
    if(i in vow):
        print(i)
        v=v+1
print("constants in the entered string:\n")
for i in str:
    if(i not in vow):
        print(i)
        c=c+1
for i in str:
    if str.count(i)>1:
        rep.append(i)
print("repeated letters in the string:\n",set(rep))
b=len(set(rep))
print("no of vowels:\n no of consonants:\n no of repeated letters:\n",v,c,b)
