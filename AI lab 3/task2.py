contact = {"name": "Huzaifa", "phone": "03445599780", "city": "Islamabad"}

# a: Print the dictionary
print("Contact Details:", contact)

# b:
contact["email"] = "huzafanaeem354@gmaiul.com"

# c:
contact["city"] = "Wah Cantt"

# d:
phone_value = contact.pop("phone")
print("Removed phone value:", phone_value)

# e:
company_value = contact.get("company", "Freelancer")
print("Company:", company_value)

# f:
print("Final Contact Details:")
for key, value in contact.items():
    print(key, ":", value)
