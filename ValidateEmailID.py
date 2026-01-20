'''verification of email id using regular expression module
EX:Nishitha@yahho.com     output:valid 
 '''
import re
email=input("enter email.id")
pattern = r'^[A-Za-z0-9]+@(gmail|yahoo|hotmail)\.(com|in)$'
if re.match(pattern, email, re.IGNORECASE):
        print("Valid Email ID")
else:
        print("Invalid Email ID")


   