''' 
WAP to Change Conversions from Celcius to Fahrenheit
C = (f-32)(5/9)
'''

temp = float(input("Enter a Temperatur: "))
unit = input("Enter Unit ('C for Celcius and F for Fahrenheit'): ")

if unit =='C' or unit =='c':
    newTemp = 9/5 *temp + 32;
elif unit =='F' or unit =='f':
    newTemp = 5/9 *temp -32;
else: 
    newTemp = "Unknown Unit";

print("Temprature Conversion : ",round(newTemp,2))
