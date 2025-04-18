from unicodedata import numeric

from PhoneBook.phoneBook_method import phoneBook
contact = phoneBook()
exit_app = False
while not exit_app:
     print("""
     1. Add contact
     2. Remove contact
     3. Find contact by phone number
     4. Find contact by first name
     5. Find contact by last name
     6. Edit contact
     7 Exit application
     """)
     try:
       choice = input("Enter your choice: ")
       while not 1<= int(choice) <= 7:
         print("invalid input, try again")
         choice = input("Enter your choice: ")

     except ValueError:
          print("invalid input, try again")
          continue

     match choice:
          case "1":
              while True:
                  phone_number: str = input("Enter phone number: ")
                  while not phone_number.isnumeric():
                        print("Only input numbers, try again")
                        phone_number = input("Enter phone number: ")
                  if phone_number  in contact.phoneBook:
                      print("Phone number already exists")
                      break

                  first_name = input("Enter your first name: ")
                  while " " in first_name or len(first_name) == 0:
                      print("invalid input, try again")
                      first_name = input("Enter your first name: ")

                  last_name = input("Enter your last name: ")
                  while " " in last_name or len(last_name) == 0:
                      print("invalid input, try again")
                      last_name = input("Enter your last name: ")

                  contact.add_contact(phone_number, first_name, last_name)
                  print("Contact added successfully")
                  break

          case "2":
              phone_number: str = input("Enter phone number: ")
              while not phone_number.isnumeric():
                  print("invalid input, try again")
                  phone_number = input("Enter phone number: ")
              if phone_number not in contact.phoneBook:
                  print("Phone number NOT found")
              else:
                  contact.remove_contact(phone_number)
                  print("Contact removed")

          case "3":
              phone_number: str = input("Enter phone number: ")
              while not phone_number.isnumeric():
                  print("invalid input, try again")
                  phone_number = input("Enter phone number: ")
              if phone_number not in contact.phoneBook:
                  print("Phone number NOT found")
              else:
                  print(f"{contact.phoneBook[phone_number]}")

          case "4":
              first_name = input("Enter your first name: ")
              while " " in first_name or len(first_name) == 0:
                  print("invalid input, try again")
                  first_name = input("Enter your first name: ")

              contact.find_by_first_name(first_name)

          case "5":
              last_name = input("Enter your last name: ")
              while " " in last_name or len(last_name) == 0:
                  print("invalid input, try again")
                  last_name = input("Enter your last name: ")

              contact.find_by_last_name(last_name)

          case "6":
              while True:
                  phone_number: str = input("Enter phone number: ")
                  while not phone_number.isnumeric():
                      print("Only input numbers, try again")
                      phone_number = input("Enter phone number: ")
                  if phone_number not in contact.phoneBook:
                      print("Phone number does not exists")
                      break

                  first_name = input("Enter your  first name or new first name: ")
                  while " " in first_name or len(first_name) == 0:
                      print("invalid input, try again")
                      first_name = input("Enter your first name or new first name: ")

                  last_name = input("Enter your last name or new last name: ")
                  while " " in last_name or len(last_name) == 0:
                      print("invalid input, try again")
                      last_name = input("Enter your last name or new last name: ")

                  new_number: str = input("Enter phone number or new phone number: ")
                  while not new_number.isnumeric():
                      print("Only input numbers, try again")
                      new_number = input("Enter your  phone number new phone number: ")
                  if phone_number == new_number:
                      print("New Phone number is the same with old Phone number")

                  if new_number != phone_number and new_number in contact.phoneBook:
                          print("Phone number already exists")
                          break

                  contact.edit_contact(phone_number, new_number, first_name, last_name)
                  print("Contact edited")
                  break

          case "7":
              exit_app = False
              break