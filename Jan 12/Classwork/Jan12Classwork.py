print("Hello! Let's Get started.") #print() is used to display message.

x = 34
y = 45
print(x/y) # '/' performs floating point division.
print(x//y) # '//' performs integer division and gives the quotient as the output.
print(x%y) # '%' performs integer division and gives the remainder as the output.
print(x**y) # '**' raises x to the power of y. There is no limit to integer precision.
print(pow(x,y)) # pow(x,y) performs x**y operation.


first_name = "My name is Sulav Baskota. "
last_name = "I am 21 years old."
print(first_name + last_name) # '+' operator can be used to concate strings.

x = input("Enter a number: ") #input() is used to prompt the user. The input given by user is stored as 'string' by input() function.
print(x)
x = int(x) #converts the data type of x into integer.
print(x+5)

x = input("Enter a string: ") # the same variable can be used to store data items of different data type.
repeat_num = int(input("Enter the number of repetition: "))
print(x * repeat_num) # '*' can be used to repeat a string for a specified number of times.
print((x+' ') * repeat_num)
print(x*10)

raw_string = r'HELLO\nWorld\t?' # the r prefix is used if you do not want to interpret escape sequences.
print(raw_string)


#Accessing values in a string.
str_1 = "LEARNING PYTHON"
print("The original value of string 'str_1' is: " + str_1)
print("The first character/value of string 'str_1' is: " + str_1[0]) # string has positive indexing that can be used to access the elements of string.
print("The last character/value of string 'str_1'is: " + str_1[-1]) # string also has negative indexing that can be used to access the elements of string.
print("The character in the string 'str_1' except the first and last character are: " + str_1[1:len(str_1)-1]) # this is called slicing a string.
print("The first 5 character in string 'str_1' are: " + str_1[:5])
print("The characters in the string except the first 3 charectars are: " + str_1[3:])
print("The characters in string 'str' skipping over every other character are: " + str_1[::2])

#Formatting string.

full_name = input("Enter your name: ")
age = input("Enter Your age: ")
print("Your name is "+full_name+". Your age is "+age+". Hello!")
print("Your name is {}. Your age is {}. Hello!".format(full_name,age))
print("Your name is {0}. Your age is {1}. {2}.Happy Birthday {0}.".format(full_name,age,"Hello!"))
print("Your name is {1}. Your age is {0}. {1}".format(age,"Hello!",full_name))
print("Your name is {name_key}. Your age is {age_key}. Hello!".format(name_key=full_name,age_key=age))
print(f"Your name is {full_name}. Your age is {age}. Hello!")




# using the bool function
z = 0
a = 'c'
b = ''
print(bool(3 < 5))
print(bool(5 < 3))
print(bool(z))
print(bool(a))
print(bool(b))

# list in python

list_1 = [] 
list_2 = list() # both of the list are empty.

list_3 = ["Sulav", 5.90,5*20,[5*20],True,[5*20,60+5,"Lokanthali"] ,"Baskota"]
# list can have elements of different data types. here list_1 has two list as it's element.
print(list_3)
print("lenght of list_3 is {}".format(len(list_3)))

list_4 = ["Sulav Baskota","Deerwalk",26,27,28,29,36]
print(f"Original list: {list_4}")
data = input("Enter a data to be added to the list: ")
list_4.append(data) # adds the value of data to the end of the list.
print(f"Modified list: {list_4}")

list_4.insert(6,30) # inserts data item to the specified loaction.
print(list_4)
list_4.insert(3,"Institute")
print(list_4)
list_4.insert(7,["of","technology",2019])
print(list_4)

list_4.remove("Institute") # removes element 'Institute' from the list. 
print(list_4)
list_4.remove('Deerwalk') # removes object/elemet 'Deerwalk' from the list.
print(list_4)
list_4.remove(list_4[0]) # removes the data item at position 0 of the list.
print(list_4)

print(f"First list : {list_4}")
print(f"Second list: {list_3}")
print("Adding second list to first list")
list_4.extend(list_3) # adds objects\elements of list_3 to list_4
print(f"New list: {list_4}")

print(list_4[:4]) # list can be sliced like string
print(list_4[-5:-2])

popped = list_4.pop(3) # pops the object at the specified position/ index from the list like in stack.
print("popped: ", popped)
print(list_4)

"""
std_data2 = ["Shreyansh Lodha", 100, 100,100, 100, 100] # declaration od another list
print(std_data2)
print("Adding these list")

std_data.extend(std_data2) # adding std_data2 to std_data using extend
print(std_data)

"""






