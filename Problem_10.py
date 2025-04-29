#WAP to find Factorial of a number using Recursion
def recur_fact(n):
    if n ==1:
        return n;
    else:
      return n*recur_fact(n-1);

num = int(input("Enter A Number: "))
if num < 0:
    print("Please Enter Number Greater than 0");
elif(num==0):
    print("The Factorial of 0 is 1");
else:
    print("The Print of Factorial",recur_fact(num))

