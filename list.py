"""fruits= ['mango', "banana", "guava", "apple"]
fruits.insert(1,"orange")
print (fruits) """  
#list loop
"""fruits= ['mango', "banana", "guava", "apple"]
for fruit in fruits:
    print(fruit)"""

"""numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers= []
for number in numbers:
    if (number %2 !=0):
          odd_numbers.append(number)
          print(number)
"""

"""numbers= [6, 9, 7, 2, 5, 1]
max_number= numbers[0]
for number in numbers:
    if number>max_number:
        max_number=number
        print(max_number)
"""
"""username = ""
password = ""
while username != "angel" and password != "secret":
    username = (input("Please enter the username : "))
    password = (input("Please enter the password : "))
    if username == "angel" and password == "secret":
        print("login sucsefully")
    else:
        print("Invalid credential;Please try again" )"""

"""username = ""
password = ""
while username != "angel" and password != "secret":
    username = (input("Please enter the username : "))
    password = (input("Please enter the password : "))
    if username == "angel" and password != "secret":
        print("Invalid password")
    elif username != "angel" and password == "secret":
        print("Invalid username")
    elif username == "angel" and password == "secret":
        print("login sucsefully")
    else:
        print("Invalid credential;Please try again" )"""
 

