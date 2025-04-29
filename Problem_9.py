# Check if a Number is Prime

Num = int(input("Enter a Number: "));
count = 0
for i in range(1,Num+1):
    if Num%i == 0:
        count += 1;
if count == 2:
    print(Num,"Is Prime Number");
else:
    print(Num,"Its Not Prime Number");


#Logic 2
def is_prime(Num):
    if(Num <=1 ):
        