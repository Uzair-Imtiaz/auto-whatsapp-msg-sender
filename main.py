import phonenumbers
import pywhatkit as py

phone_no = input('Enter the recepient phone number: ')
number = phonenumbers.parse(phone_no)
msg = '''Your message here. '''
time = input('Enter the time to schedule your message in 24 hours format.(Space separated)').split()
py.sendwhatmsg(phone_no,msg,int(time[0]),int(time[1]))'''
