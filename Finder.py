#! python3
# Finder.py - To find email and phone number from a text in your clipbord

import pyperclip , re
text = str(pyperclip.paste())
matches = []
def phonenumber(number):
    phoneregex = re.compile(r'(\d{3}|\(\d{3}\))(\s+|-|.)?(\d{3}|\(\d{3}\))(\s+|-|.)(\d{4}|\(\d{4}\)(\s+))')
    findphone = phoneregex.findall(number)
    for i in range(len(findphone)):
        matches.append(''.join(findphone[i]))

    
def email(mail):
    emailregex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
    findemail = emailregex.findall(mail)
    for i in range(len(findemail)):
        matches.append(''.join(findemail[i]))

phonenumber(text)
email(text)

if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
else:
    print("There is no email / phonenumber")