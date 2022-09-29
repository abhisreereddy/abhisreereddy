try:
    def rev(st):
        st=" ".join(reversed(st))
        return st
    arr=str(input("Enter the string to be reversed="))
    if(arr=='!' or arr=='@' or arr=='#' or arr=='$' or arr=='%' or arr=='^' or arr=='&' or arr=='(' or arr==')' or arr=='_' or arr=='-' or arr=='+' or arr=='=' or arr=='~' or arr=='`'):
        print("SPECIAL CHAR")
    print("THE STRING REVERSED---> ",end=" ")
    print(rev(arr))
except(ValueError):
    print("INTEGER NOT ALLOWED")
