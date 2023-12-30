#!/usr/bin/python3

"""test the ContactBook class"""

from models.Contact_Book import ContactBook

#name = "olakunle"
#number = "07062869135"
obj = ContactBook()
obj.phone_number = "070622869135"
obj.name = "olakunle"
obj.email = "salauisiaka1998@gmail.com"
obj.address = "14, ogun state, Nigeria"
obj.nickname = "agroelectronics"

print("\n-----------string implementation of an instance--------------")
print(obj)

print("\n--------saving object----------")
obj.save()

print("\n================================================\n")

print(obj.to_dict())
print("\n===================OBJ2=============================\n")
obj2 = ContactBook(**obj.to_dict())
print(obj2)
print("\n--------saving object----------")
obj2.save()
print("\n=============false or true?===============\n")
print(obj is obj2)
