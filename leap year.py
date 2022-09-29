n=int(input('enter date:'))
if(n>0):
    if(n%4==0 or n%400==0):
        print('Given year is a leap year')
    else:
        print('Given year is not a leap year')
        if n%4!=0:
            n-=int(n%4)
        print("Leap Year:",n)
else:
    print('not a valid year')
