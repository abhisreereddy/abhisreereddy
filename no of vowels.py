string=str(input("enter the string= "))
vowel=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowel=vowel+1
print("Number of vowels",vowel)
