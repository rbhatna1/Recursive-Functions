def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()

def fact(m,n):
    def fact1(m,fact=1,x=1):
        if x==m:
            fact*=x
            print("The factorial of the number",m,"is",fact)
        else:
            return fact1(m,fact*x,x+1)
    for a in range(m,n+1):
        fact1(a)
        
def sum(number):
    if number==1:
        return 1
    else:
        return number+sum(number-1)

def power(m,n):
    if n==0:
        return 1
    else:
        return m*power(m,n-1)
        
def prime(number,div=2):
    while number>div:
        if number%div==0:
            print("It is not a prime")
            break
        else:
            return prime(number,div+1)
    else:
        print("It is a prime number")
        
def GCD(number1,number2):
    if number2==0:
        return number1
    else:
        return GCD(number2,number1%number2) #Euclid's Algorithm

def tables1(number,times=1):
    if times==10:
        print(number,"x",times,"=",number*times)
    else:
        print(number,"x",times,"=",number*times)
        return tables1(number,times+1)

def rev(a):
    if a=="":
        return ""
    else:
        print(a[-1],end="")
        return rev(a[0:-1])

def palindrome(string):
    if len(string)<=1:
        print("It is a palindrome")
        return
    if string[0] == string[len(string)-1] :
      return palindrome(string[1:len(string) - 1])
    else:
        print("It is not a palindrome")
        return

def feb1(n):
    def feb(n):
        if n<=1:
            return n
        else:
            return(feb(n-1)+feb(n-2))
    for i in range(n):
        print(feb(i),end=" ")
        
def pat1(n,x=1,z="*"):
    if n==x:
        return z*x
    else:
        print(z*x)
        return pat1(n,x+1)

def pat2(n):
    def pat21(n):
        if n==1:
            return n
        else:
            print(n,end=" ")
            return pat21(n-1)
    for i in range(1,n+1,1):
        print(pat21(i))

def pat3():
    def pat31(n,x=5):
        if n==x:
            return " "
        else:
            print(x,end=" ")
            return pat31(n,x-1)
    for i in range(4,-1,-1):
        print(pat31(i))

def dec_bin(n):
    if n>=1:
        dec_bin(n//2)
    print(n%2,end=" ")
    
def dec_oct(n):
    if n>=1:
        dec_oct(n//8)
    print(n%8,end=" ")
  
def dec_hex(dec):
    if dec!=0:
        dig=dec%16
        if dig==10:
            return "A"
        if dig==11:
            return "B"
        if dig==12:
            return "C"
        if dig==13:
            return "D"
        if dig==14:
            return "E"
        if dig==15:
            return "F"
    if dec>=1:
        return dec_hex(dec//16)+str(dec%16)

def hex_dec(dec):
    if type(dec)==str:
        dig=dec[0]
        if dig=="A":
            return 10
        if dig=="B":
            return 11
        if dig=="C":
            return 12
        if dig=="D":
            return 13
        if dig=="E":
            return 14
        if dig=="F":
            return 15
    if type(dec)!=str:
        return dec_hex(dec[1::]//16)+str(dec%16)
    
def bin_dec(x,s=0,c=0):
    if x==0:
        return s
    else:
        sum=(x%10)*(2**c)
        return bin_dec(x//10,s+sum,c+1)

def oct_dec(x,s=0,c=0):
    if x==0:
        return s
    else:
        sum=(x%10)*(8**c)
        return oct_dec(x//10,s+sum,c+1)

def bsearch(ar1,val,low,high):
    mid=((high+low)//2)
    if high<low:
        return none
    else:
        if ar1[mid]>val:
            return bsearch(ar1,val,low,mid-1)
        elif ar[mid]<val:
            return bsearch(ar1,val,mid+1,high)
        else:
            return mid

def linearsearch(list,val,x=0):
    if x==len(list):
        return False
    else:
        if list[x]==val:
            return True
        else:
            return linearsearch(list,val,x+1)
        
def sumdigits(list,s=0,x=0):
    if x==len(list):
        return s
    else:
        s+=list[x]
        return sumdigits(list,s,x+1)
        
choice=0

while choice!=21:
    print("Choose from one of the folowing options")
    print("1)Choose 1 to find the factorial of a number")
    print("2)Choose 2 to find the sum of the first n natural numbers")
    print("3)Choose 3 to find the power of the number")
    print("4)Choose 4 to find whether the number is prime")
    print("5)Choose 5 to find the GCD of the numbers")
    print("6)Choose 6 find the table of the number")
    print("7)Choose 7 to find the reverse of the number and check whether it a palindrome")
    print("8)Choose 8 to find the fibonacci series")
    print("9)Choose 9 find the First pattern")
    print("10)Choose 10 find the Second pattern")
    print("11)Choose 11 find the Third pattern")
    print("12)Choose 12 to convert Decimal to Binary")
    print("13)Choose 13 to convert Decimal to Octal")
    print("14)Choose 14 to convert Decimal to Octal")
    print("15)Choose 15 to convert Binary to Decimal")
    print("16)Choose 16 to convert Octal to Decimal")
    print("17)Choose 17 to convert Hexadecimal to Decimal")
    print("18)Choose 18 find the element in the list using linear search")
    print("19)Choose 19 find the element in teh list using binary serach")
    print("20)Choose 20 find the sum of all the values entered in the list")
    print("21)Choose 21 to exit the following code")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        space()
        m=int(input("Enter the lower number of the range"))
        n=int(input("Enter the higher number of the range"))
        fact(m,n)
        space()
        
    elif choice==2:
        space()
        n=int(input("Enter the number"))
        print("The sum  of the first",n," natural numbers is",sum(n))
        space()
        
    elif choice==3:
        space()
        m=int(input("Enter the base number"))
        n=int(input("Enter the raised to number"))
        print("The number",m," raised to the power",n,"is",pow(m,n))
        space()
        
    elif choice==4:
        space()
        n=int(input("Enter the number"))
        prime(n)
        space()
        
    elif choice==5:
        space()
        m=int(input("Enter the First number"))
        n=int(input("Enter the Second number"))
        print("The GCD of the numbers",m,"and",n,"is",GCD(m,n))
        space()
        
    elif choice==6:
        space()
        n=int(input("Enter the number"))
        tables1(n)
        space()
        
    elif choice==7:
        space()
        n=int(input("Enter the number"))
        rev("n")
        palindrome("n")
        space()
        
    elif choice==8:
        space()
        n=int(input("Enter the number"))
        feb1(n)
        space()
        
    elif choice==9:
        space()
        n=int(input("Enter the number"))
        pat1(n)
        space()
        
    elif choice==10:
        space()
        n=int(input("Enter the number"))
        pat2(n)
        space()
        
    elif choice==11:
        space()
        pat3()
        space()
        
    elif choice==12:
        space()
        n=int(input("Enter the number"))
        dec_bin(n)
        space()
        
    elif choice==13:
        space()
        n=int(input("Enter the number"))
        dec_oct(n)
        space()
        
    elif choice==14:
        space()
        n=int(input("Enter the number"))
        dec_hex(n)
        space()
        
    elif choice==15:
        space()
        space()
        
    elif choice==16:
        space()
        space()
        
    elif choice==17:
        space()
        space()
        
    elif choice==18:
        space()
        list=eval(input("Enter the list"))
        list.sort()
        val=int(input("Enter the number"))
        x=linearsearch(list,val)
        if x is True:
            print("It is present")
        else:
            print("It is not present")
        space()
        
    elif choice==19:
        space()
        ar=eval(input("Enter the list"))
        ar.sort()
        val=int(input("Enter the number"))
        print("The index of the element in the sorted list is",bsearch(ar,val,0,len(ar)-1))
        space()
        
    elif choice==20:
        space()
        list=eval(input("Enter the list"))
        list.sort()
        print("The sum of the digits in the list is",sumdigits(list))
        space()