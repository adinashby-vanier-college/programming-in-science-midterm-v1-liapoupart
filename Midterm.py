import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n<4:
        return "The triangle height should be at least 4."
    else:
        for i in range(1, n+1):
            if i == 1:
                line = "*" 
            elif i == i:
                line = ("*") * (n)
            else:
                line = "*" + (i-2)*(" ") + "*" 
        return line.rstrip
# To make a hollow triangle, I already know that it starts with a * at the start of each line but the nb of spaces is dependant on i.
# There are two * per line except line 1 and line n, where there are only 1 * at n=1 an n starts and line n
# With a if else code, i code the exceptions and else is everything that isn't i =1 or n. 
# There are 

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    if n<3:
        return "The pyramid height should be at least 3."
    else:
        for i in range(1, n+1):
            line = (" " * (i-1)) + (("*") * ((2*n+1)-2*i)) + "\n"
        return str(line)
    

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()