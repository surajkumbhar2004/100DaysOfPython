# WAP to Find the largest among the Three Numbers

Num1 = float(input("Enter 1st Number: "))
Num2 = float(input("Enter 2nd Number: "))
Num3 = float(input("Enter 3rd Number: "))

if(Num1 >= Num2) and (Num1 >= Num3):
    largest = Num1;
elif(Num2 >= Num1) and (Num2 >= Num3):
    largest = Num2;
else:
    largest = Num3;
print("Largest Number is ",largest)