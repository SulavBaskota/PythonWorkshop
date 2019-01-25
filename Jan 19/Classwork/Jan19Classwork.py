s = "Hello world"
print(s.split(" "))
comp = ["opperand","function"]
comp[0]= "python"
print(comp)
list_1 = comp
print(comp)
print(list_1)
list_1[1] =  "programmming"
print(comp)
print(list_1)
print(list_1 is comp)
l =[1,2,3]
a=l*5
print(a)

#tuple
x = (1,2,3)
print(x[0])
print(x[-1])
print(x[:2])

t =(1) #single value inside () is not tuple
print(type(t))
t = (1,) # single value inside() followed by ',' declares a tuple
print(type(t))
print(len(t))
tup=(1,2,3)
print(tup)
tup = tup + (4,)
print(tup)
print(tup*6)
print(tup)

tup = (1,2,4,1,3,2,5,2,4)
print(tup.count(2))
print(tup.index(2))
print(3 in tup)
print(21 not in tup)

#unpacking a tuple
x = 1, 2, 3
print(x)
p, q, r = x
print(p)
print(q)
print(r)

#swap using concept of tuple
a = 4
b = 5
b,a =a,b
print(b)
print(a)

#set
s = set() #always use this to initialize empty set
print(type(s))
s = {} # creates a dictionary
print(type(s))

s = {"Hello",1,1.15,("OK",None)} # {} signifies set
s.update(("Helloo",2))
print(s)
print(type(s))
print(len(s))

#dictionary
d={
    "a":"hello",
    "b": 77,
    "x": 45
    }
print(d.keys())
print(d.values())
print(d.items())
print(type(d))

print(d["a"])
print(d.get("x"))

d['y']=800
print(d.items())

d = {
    "name" : 'sulav',
    "subjects" : ["Pyhthon","C"],
    "mark" : (30,32)
    }
 
print(d.values())
print(d.items())


list_2=[]
list_1 = list(range(0,12))
print(list_1)
for each in list_1:
    if each % 2 == 0:
        list_2.append(each)
print(list_2)

a,b=5,6
print(a if a>b else b) #terminary operator

#funciton in python

def getsum(x,y):
    print(x+y)
getsum(5,6)

def getsum_1(a,b=0): #b has defult value 0
    return a+b
result=getsum_1(2,3)
print(result)
result=getsum_1(7) # b takes default value 0
print(result)
result=getsum_1(2,3)
print(result)
# function to print message "Happy Birthday To you .."

def print_happy(name):

    
    print(f"Happy Birthday dear {name}!\n"+f"Happy Birthday!!! \n"*3+"Happy Bithday to you!")
yourname=input("enter your name: ")
print_happy(yourname)

def sum_num(*args): #takes variable length arguments
    print(args)
sum_num()
sum_num(1,2,3)
sum_num(1,2,3,4,5)

def sum_vals(**kwargs):#variable lenght keyword arguments
    print(kwargs)
sum_vals(a=10,b=50)


