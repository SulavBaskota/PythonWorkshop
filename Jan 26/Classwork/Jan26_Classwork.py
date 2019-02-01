# Comprehension
# tuple is not comprehensible


def function1(t, w=0, *args, **kwargs):
    print(t)
    print(w)
    print(args)
    print(kwargs)


function1(1, 2, 3, 4, 5)

function1(1, name='Python')

x = list(range(0, 10))
y = []

for each in x:
    if each % 2 == 0:
        y.append(each**2)
print(f"y: {y}")

z = [each**2 for each in range(0,10) if each % 2 == 0]  # list comprehension
print(f"z: {z}")

# dictionary comprehension

programming_lang = ["C", "Python", 'Java']
creator = ["Dennis", "Guido", "James"]
d1 = {}
for each in zip(programming_lang, creator):  # zip function makes a tuple
    d1[each[0]] = each[1]
print(f"d1: {d1}")
d2 = {}
for key, val in zip(programming_lang, creator):
    d2[key] = val
print(f"d2: {d2}")

d3 = {key: val for key, val in zip(programming_lang, creator)}
print(f"d3: {d3}")

# lambda
# lambda is an anonymous function


def get_sum(n1=1, n2=1):
    return n1+n2


print(get_sum(2, 3))

a = lambda p=1, b=1: p+b  # lambda is assigned to a variable and is called through that variable
print(a(5, 6))
print(type(a))

# Generator
# it does lazy evaluation meaning that it only gives yield when
# if a function has 'yield' instead of 'return' it is a generator


def prod(n3, n4):
    yield n3 * n4
    yield n3 / n4


print(next(prod(1, 3)))
print(next(prod(1, 3)))  # prints the same yield

gen_prod = prod(1, 3)

print(next(gen_prod))
print(next(gen_prod))
# print(next(gen_prod)) # StopIteration


for each in gen_prod:  # using for loop for generator doesnot give StopIteration error
    print(each)

gen_prod = prod(2, 3)
for each in gen_prod:
    print(each)

list_1 = [x for x in range(1, 10000)]
g = (x for x in range(1, 10000))  # this code means that there is yield starting from 1 to 9999

print(type(g))
print("Memory consumed by list l : ", list_1.__sizeof__())
print("Memory consumed by generator g : ", g.__sizeof__())

# decorator


def sum_1(v, m):
    return v+m


r = sum_1  # function can be stored in a variable


def accept_func(q):
    print(q(1, 2))


accept_func(r)  # function can be passed to another function


def outer():  # function as an argument
    def inner(e, h):  # defined nested function
        return e + h
    return inner  # return the inner function as a value


s = outer()(2, 3)
print(s)


def outer2(arg_func):  # function as an argument
    def inner():
        print("Inner Executed")  # defined nested function
        arg_func()
    return inner  # execute arg_func inside the inner func


@outer2  # Decorator
def my_func():
    print("Hello World")


my_func()

# Classes and object
# name of class always starts with capital letter
# class have attribute and behaviour(method)


class Car:

    def __init__(self, name, wheels, engine):  # Attributes
        self.name = name
        self.wheels = wheels
        self.engine = engine

    def drift(self):  # Behavior # Instance method
        print(f"{self.name} is drifting")

    def __str__(self):  # string representation of object
        return self.name

    def __repr__(self):
        return f"Car({self.name}, {self.wheels}, {self.engine})"


kia = Car('Kia', 4, "diesel")
tesla = Car('Tesla', 4, 'electric')
print(type(tesla))
print(tesla)
print(kia)
print(tesla.engine)
print(kia.engine)
print(repr(kia))
print(repr(tesla))
kia.drift()
tesla.drift()

print(isinstance(kia, Car))
print(isinstance(kia, object))
print(isinstance(kia, int))


class Animal:

    def __init__(self, type):
        self.type = type


class Dog(Animal):

    def __init__(self, name, type):
        super().__init__(self)  # Inheritance
        self.name = type
        self.type = type


d = Dog('Tom', 'Carnivore')
print(d.__dict__)
print(isinstance(d, Dog))
print(isinstance(d, object))
print(isinstance(d, Animal))


class Person:

    count = 0  # count is class variable which is shared for all the instances in the class

    def __init__(self, fname, lname):  # fname and lname are instance variable
        self.fname = fname
        self.lname = lname
        Person.count += 1

    def full_name(self):
        return f"{self.fname} {self.lname}"

    @property
    def reverse_name(self):
        return f"{self.lname} {self.fname}"

    @classmethod
    def generate_person_instance(cls, dashed_name):
        fname, lname = dashed_name.split("-")
        return cls(fname, lname)


p1 = Person("Hari", "Shrestha")
print(p1.fname, p1.count)
p2 = Person("Sulav", "Baskota")
print(p2.fname, p2.count)
print(p2.fname, p2.count)
print(Person.count)
print(p1.full_name())
print(p1.reverse_name)
p = Person.generate_person_instance("Hari-Bahadur")
print(p.__dict__)

# Static Method -- doesn't depend on instance


class TempConverter:

    @staticmethod
    def cel_to_far(ctemp):
        return ctemp*(9/5) + 32

    @staticmethod
    def far_to_cel(ftemp):
        return (5/9)*(ftemp-32)


print(TempConverter.cel_to_far(100))
print(TempConverter.far_to_cel(230))

