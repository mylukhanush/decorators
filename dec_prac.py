# def time_it(func):
#     def wrapper():
#         t1 = time.time()
#         print(f"Time start is : {t1}")
#         func()
#         t2 = time.time()
#         print(f"Time start is : {t2}")
#         t = t2+t1
#         print(f"Time taken is : {t} seconds")
#     return wrapper
# research = time_it(research)
# research()

# A simple decorator function
# def decorator(func):
#     def wrapper():
#         print("Before calling the function.")
#         func()
#         print("After calling the function.")
#
#     return wrapper
#
# @decorator
# def greet():
#     print("Hello, World!")
#
#
# greet()


# def decor(fun):
#     def inner():
#         x=fun
#         return x*5
#     return inner
# def num():
#     return 5
# result=num()
# print(result)
# z=decor(num)
# print(z())

# def decorator(func):
#     def location():
#         print("This is a training center in nellore named")
#         func()
#         print("It is located in magunta layout ")
#     return location
# def Ach():
#     print("Achieve Software Training")
# Ach=decorator(Ach)
# Ach()

""""
def decorstr(func):
    def x (n):
        result = func(n)
        result += " how are you?"
        return result

    return x
@decorstr
def hello(name):
    return "Hello " + name
print(hello("John"))
"""
#decorator chaining

def power(fun):
    def inner():
        n=fun()
        return n**4
    return inner
def cube(fun):
    def inner():
        n=fun()
        return n**3
    return inner
def square(fun):
    def inner():
        n=fun()
        return n**2
    return inner
def half(func):
    def inner():
        n=func()
        return n/2
    return inner
@power
@cube
@square
@half
def num():
    return 10
print(num())



