class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def display(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}")


l1 = Laptop("Dell", "16GB")
l2 = Laptop("HP", "8GB")

l1.display()
l2.display()


# class Laptop:
#     def __init__(self, brand, ram):
#         self.brand = brand
#         self.ram = ram

#     def display(self):
#         print(f"Brand: {self.brand}, RAM: {self.ram}")


# l1 = Laptop("Dell", "16GB")
# l2 = Laptop("HP", "8GB")

# l1.display()
# l2.display()


# b1 = Bike("Yamaha", "Black")
# b1.start()


# class Bike:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print(f"{self.color} {self.brand} bike is starting")


# b1 = Bike("Yamaha", "Black")
# b1.start()


# class Class:
#     college_name = "BBDU"

#     def __init__(self, branch, course, student_name):
#         self.branch = branch
#         self.course = course
#         self.student_name = student_name

#     def display(self):
#         print(
#             f"Student Name: {self.student_name}, Branch: {self.branch}, Course: {self.course}"
#         )


# b1 = Class("CSE", "BTech", "Rahul")
# b2 = Class("IT", "BTech", "Ananya")

# b1.display()
# b2.display()


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display(self):
#         print(f"Title: {self.title}, Author: {self.author}")


# b1 = Book("Book 1", "Author 1")
# b2 = Book("Book 2", "Author 2")

# b1.display()
# b2.display()


# class Mobile:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}")


# m1 = Mobile("Apple", "Iphone 17 Pro Max")
# m2 = Mobile("Samsung", "Galaxy S25 Ultra")

# m1.info()
# m2.info()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")


# c1 = Employee("Ayush", 65000.67)
# c2 = Employee("Saksham", 56332.56)

# c1.info()
# c2.info()

# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def show_details(self):
#         print(f"Brand: {self.brand}, Name: {self.price}")


# c1 = Car("BMW", 6500000)
# c2 = Car("AUDI", 4900000)

# c1.show_details()
# c2.show_details()

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")


# s1 = Student("Rahul", 20)
# s2 = Student("Ananya", 19)

# s1.info()
# s2.info()


# def check(
#     value_1, value_2
# ):  # Write a function that takes a list of numbers and returns their maximum.
#     if value_1 > value_2:
#         return "First number is the maximum."
#     elif value_1 < value_2:
#         return "Second number is the maximum."
#     elif value_1 == value_2:
#         return "BOTH ARE EQUAL."
#     else:
#         return "INVALID."


# value_1 = int(input("Enter your first number:"))
# value_2 = int(input("Enter your second number:"))
# n1 = check(value_1, value_2)
# print(n1)

# def check(value_1, value_2):
#     if value_1 > value_2:
#         return "First number is the maximum."
#     elif value_1 < value_2:
#         return "Second number is the maximum."
#     elif value_1 == value_2:
#         return "BOTH ARE EQUAL."
#     else:
#         return "INVALID."


# value_1 = int(input("Enter your first number:"))
# value_2 = int(input("Enter your second number:"))
# n1 = check(value_1, value_2)
# print(n1)


# def check(n1):
#     if n1 % 2 == 0:
#         return "Even Number."
#     else:
#         return "Odd Number."


# value = int(input("Enter your number to find square root:"))
# n1 = check(value)
# print(n1)

# def add(n1, n2):
#     return n1 + n2


# n = add(23, 54)
# print(n)

# def greet(n="guest"):
#     print("Hello", n)


# n = input("Enter your name: ")
# greet(n)

# def greet():
#     print("Hello, World")


# greet()

# s1 = {34, 23, 54}
# s2 = {34, 54, 89}
# s3 = s1.intersection(s2)
# print(s3)

# s = {2, 34, 56}
# a = s.copy()
# print(s)

# s1 = {34, 23, 54}
# s2 = {53, 37, 89}
# s3 = s1 - s2
# print(s3)


# s1 = {34, 23, 54}
# s2 = {53, 37, 89}
# s3 = s1.union(s2)
# print(s3)

# s = {1, 2, 356, 4, 5}
# s.pop()
# print(s)

# s = {1, 2, 356, 4, 5}
# s.remove(6)
# print(s)

# s = {1, 2, 356, 4, 5}
# s.remove(6)
# print(s)

# s = {1, 2, 356, 4, 5}
# s.add(56)
# print(s)

# s = (54, 65, 23, 34, 89)
# for i in s:
#     print(i)

# s = {1, 2, 4, 2, 6}
# print(s)

# s = {"red", "blue", "green", "yellow", "grey"}
# print(s)

"""
s = int(
    input("Enter number of seconds for conversion into min & sec: ")
)  # Time conversion
min = s // 60
sec = min % 60

print(min, " minutes & ", sec, "seconds")

distance = 120  # Avg speed
time = 3
avg_speed = distance / time
print("Average Speed: ", avg_speed)

n1 = int(input("Enter first variable: "))  # To check multiple eof first variable
n2 = int(input("Enter second variable: "))

if n1 % n2 == 0:
    print("A multiple of first variable")

else:
    print("Not multiple of first variable")

pri = 5000.78  # Simple Interest
ri = 12.6
t = 3
si = (pri * ri * t) / 100
print("Simple Interest", si)

print("Rounded Values", pri // si)  # Rounding floating values


name = input("Enter your name: ")
print("Hello", name)


a = 23
b = 65

add = a + b
subt = b - a
mult = a * b
div = a / b

print("Addition result =", add)
print("Subtraction result =", subt)
print("Multiplication result =", mult)
print("Division result =", div)
print(a // b)
print(a % b)
print(a**b)
p = 15
n = 40
print((15 * 3) + (40 * 2))

r = 45
s = 66
t = 34
print((p + n + r + s + t) / 5)

print(n**2)
print(n**3)
print(n**0.5)


op = int(input("Choose your number of operation: ")) #28 basic questions on operators and comparison.


match op:
    case 1:
        n1 = int(input("Enter your first number: "))
        n2 = int(input("Enter your second number: "))
        if n1 == n2:
            print("They are equal.")
        else:
            print("They are not equal.")
    case 2:
        n1 = int(input("Enter your first number: "))
        n2 = int(input("Enter your second number: "))
        if n1 < n2:
            print("N2 is greater than N1.")
        elif n1 > n2:
            print("N1 is greater than N2.")
        elif n1 == n2:
            print("They are equal.")
        else:
            print("Invalid")
    case 3:
        n1 = int(input("Enter your first number: "))
        n2 = int(input("Enter your second number: "))
        n3 = int(input("Enter your third variable: "))
        if n1 < n2 and n1 < n3:
            print("N1 is smallest among all.")
        elif n2 < n1 and n2 < n3:
            print("N2 is smallest among all.")
        elif n3 < n1 and n3 < n2:
            print("N3 is smallest among all.")
        else:
            print("Invalid")

    case 4:
        n1 = int(input("Enter your marks: "))

        if n1 >= 40:
            print("Pass.")
        else:
            print("Fail.")
    case 5:
        n1 = int(input("Enter your age: "))
        if n1 >= 18:
            print("Eligiblle for voting.")
        else:
            print("Not eligible for voting.")

    case 6:
        n1 = int(input("Enter your number to check even or odd:"))
        if n1 % 2 == 0:
            print("Even.")
        else:
            print("Odd.")
    case 7:
        s1 = input("Enter your first word: ")
        s2 = input("Enter your second word: ")
        if s1 == s2:
            print("Same word.")
        else:
            print("Different Word.")
    case 8:
        n1 = int(input("Enter salary of person A: "))
        n2 = int(input("Enter salary of person B: "))
        if n1 < n2:
            print("B has more salary than A.")
        elif n1 > n2:
            print("A has more salary than B")
        elif n1 == n2:
            print("They have same salary.")
        else:
            print("Invalid")
    case 9:
        n1 = int(input("Enter your number: "))
        if n1 > 10 and n1 < 50:
            print("Number lies between 10 to 50.")
        else:
            print("Number doesn't lies between 10 to 50.")
    case 10:
        n1 = int(input("Enter your yar to check leap year:"))
        if n1 % 4 == 0 and n1 % 100 != 0 and n1 % 400 == 0:
            print(n1, " is a leap year.")
        else:
            print(n1, " is not a leap year.")

    case 11:
        n1 = int(input("Enter your marks in Maths: "))
        n2 = int(input("Enter your marks in Science: "))

        if n1 >= 40 and n2 >= 40:
            print("Pass.")
        else:
            print("Fail.")

    case 12:
        n1 = int(input("Enter your bill amount: "))
        s1 = input("Enter Y if you have membership card otherwise N: ")
        if n1 < 1000 or s1 == "Y":
            print("N1 is smallest among all.")
        else:
            print("Invalid")
    case 13:
        n1 = int(input("Enter your number: "))
        if n1 % 3 == 0:
            print("Divisible by 3")
        else:
            print("Not divisible by 3")
    case 14:
        n1 = int(input("Enter your age: "))
        if n1 >= 13 and n1 <= 19:
            print("A teenager!")
        else:
            print("Not a teenager...")
    case 15:
        n1 = int(input("Enter your age: "))
        if n1 >= 18 and n1 <= 70:
            print("Eligiblle for voting and driving.")
        elif n1 >= 18 and n1 > 70:
            print("Eligiblle for voting and but not for driving.")
        elif n1 < 18:
            print("Not eligible for anything.")
        else:
            print("Invalid.")
    case 16:
        n1 = int(input("Enter your atteandance %: "))
        s1 = input("Enter Y if you have submitted all assignments otherwise N: ")
        if n1 >= 75 or s1 == "Y":
            print("Eligible for exam.")
        else:
            print("Not eligible for exam.")
    case 17:
        n1 = int(input("Enter your yar to check leap year:"))
        if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
            print(n1, " is a leap year.")
        else:
            print(n1, " is not a leap year.")
    case 18:
        s1 = input("Enter your day: ")
        s2 = input("Enter Y if you have holiday on that day otherwise N: ")
        if s1 == ("sunday" or "Sunday") or s2 == "Y":
            print("Relax.")
        else:
            print("Sorry! A working day. :)")
    case 19:
        n1 = int(input("Ente your number:"))
        if n1 % 3 == 0 and n1 % 5 == 0:
            print("It is divisible by 3 and 5.")
    case 20:
        s1 = input("Enter your username: ")
        s2 = int(input("Enter your pin: "))
        if s1 == "user" and s2 == 1234:
            print("Login Succesful.")
        else:
            print("Login Failed.")
    case 21:
        s1 = 10
        print(s1)
    case 22:
        s1 = int(input("Enter a number for increment:"))
        s1 = +5
        print(s1)
    case 23:
        s1 = int(input("Enter a number decrement:"))
        s1 = -3
        print(s1)
    case 24:
        s1 = int(input("Enter a number divide by 2:"))
        s1 /= 2
        print(s1)
    case 25:
        s1 = int(input("Enter a number for floor divison by 3:"))
        s1 //= 3
        print(s1)
    case 26:
        s1 = int(input("Enter a number for multiplication by 4:"))
        s1 *= 4
        print(s1)
    case 27:
        s1 = int(input("Enter a number to get remainder after divided by 7:"))
        s1 %= 7
        print(s1)
    case 28:
        s1 = int(input("Enter a number to raise it by power 3:"))
        s1 **= 3
        print(s1)

l = [1, 2, 3, 4, 5] #1
print(l)
print(len(l))
print(l[0])
print(l[-1])

l = ["apple", "banana", "cherry", "date", "elderberry"] #3
n1 = input("Enter a fruit name to append: ")
n2 = input("Enter a fruit name to insert at position 2: ")
p1 = l.append(n1)
p2 = l.insert(2, n2)
print(l)

l = ["apple", "banana", "cherry", "date", "elderberry"] #4

p1 = l.remove("cherry")
p2 = l.pop()
print(l)


l = [2, 3, 65, 12, 4]  # 7
print(l)
n = int(input("Enter the number to check its index in list: "))
print(n, " has index of ", l.index(n))

list = [1, 56, 32, 87]

list.reverse()
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

"""
