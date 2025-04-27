import time
ltime = time.localtime();
print(time.strftime("%a %b %d %H:%M:%S %Z %Y",ltime))


'''
%a - Abbrivated weekday Name 
%b - Abbrivated Month Name
%d - Date of the month in decimal number
%H:%M:%S - Hour:Minute:Second
%Z - Time Zone Name
%Y - Year
'''