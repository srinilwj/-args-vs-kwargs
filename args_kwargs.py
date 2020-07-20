#1. 

def multiply(x, y):
    print (x * y)

multiply(5, 4)

#2.

def multiply(x, y):
    print (x * y)

multiply(5, 4, 3)


#3.

def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)


#4. 

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
tuple1 = (10,11)

print(my_sum(*list1, *list2, *list3, *tuple1))


#5.

def print_kwargs(**kwargs):
        print(kwargs)

print_kwargs(k_1="Shark", k_2=4.5, k_3=True)

#6.

 def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="Sammy", your_name="Casey")


#7.


def print_values(**kwargs):
    for key, value in kwargs.items():
        print(f"The value of {key} is {value}")


print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )



