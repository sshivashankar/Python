import sys
def age_in_seconds():
    user_age = int(input("Please enter your age : "))
    s = (365*24*60*60)
    print("you have lived in", user_age * s, "seconds")
age_in_seconds()

'''
from datetime import date
now = date.today()
birthday = date(1991, 11, 17)
age = now-birthday
print(age.days)
'''