

def min(x, y):      # returns minimum of two values
    if x<y:
        v_min = x   # v_min >> defining a variable for the smallest value
    else:
        v_min = y
    return v_min


def max(values_list):
    v_max = values_list[0]
    for number in values_list[1:]:    # may be faster to compare all values insted of excluding first element with [1:]
        if v_max < number:
            v_max = number
    return v_max


def len(values_list):
    i = 0                           # we use 'x' variable to count number of elements in the list
    if values_list == []:           # verifying that the list contains elements; I do not insert this in all functions
        return 0                   # containing lists to mantain the code short, but the impementation would be the same
    for element in values_list:
        i += 1
    return i


def multiply(x, y):                 # x can be float;  y needs to be integer
    if y < 0:                       # case y has negative value
        x = -x
        y = -y
    result = x
    for i in range(1, y):
        result += x
    return result


def pow(x, y):
    result = x
    for i in range(1, y):
        result *= x
    return result



def divmod(x,y):                    # divmod (optional) - returns a tupple
    q = 0                           # this will be the quotient
    if x >= 0:
        while x >= y:               # for  positive x
            x = x - y
            q = q + 1
    else:
        while x < 0:                # for negative x
            x = x + y
            q = q - 1
    return (q, x)




### verifiyng ###
x = 2.2
y = 4
my_list = [3, 1, 7, -6, 15, -12]

print(f"minimum value of {x} and {y} is {min(x,y)}")

print("\nmaximum value from the list",my_list, end = " is ")
print(max(my_list))

print(f"\nthe length of the list  {my_list} is >> {len(my_list)} elements")

print("\n\ntesting multiply(x,y) where y must be integer")
test_val_list = [(2.2, 5) ,(-2.2, 5), (-2.2, 5), (2.2, -5)]
for val in test_val_list:
    x = val[0]
    y = val[1]
    print(f"{x} * {y} = {multiply(x,y)}")

print(f"\n\n{x} pow {y} = {pow(x,y)}")

print("\n\ntesting divmod(x,y) where y must be positive integer, both can be positive or negative:")
test_val_list = [(9, 2) ,(12, 17), (-17, 3), (18, 6)]
for val in test_val_list:
    x = val[0]
    y = val[1]
    print(f"\nfor {x}//{y}  rewrite function returns:  {divmod(x, y)}  and built-in Python functipn:  ({x//y}, {x%y})")




