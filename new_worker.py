first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[0:5]
print(new_account)

temp_password = last_name[2:6]
print(temp_password)

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name


new_account = account_generator(first_name, last_name)
print(new_account)



first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  """Generates temporary password"""
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)

print(temp_password)




company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
print(second_to_last)


first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[-2:]
print(fixed_first_name)
final_word = company_motto[-4:]
print(final_word)


