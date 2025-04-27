# Write a program to calculate simple interest given the principal amount, rate of interest, and time 
Principal_Amount = float(input("Enter Principal Amount: "));
Rate = float(input("Enter a Rate: "));
Time = int(input("Enter Time Period: "));
Simple_Interest = Principal_Amount*Rate*Time/100
TA = Principal_Amount + Simple_Interest
print("Your Simple Interset Would be: ",round(Simple_Interest,2));
print("Total Amount: ",round(TA,2))
