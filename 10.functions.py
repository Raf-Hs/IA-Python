# Exercise: Functions in python

#     Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,


def area_triangule():
    print("Hey, give me base")
    base=int(input())  
    print("Hey, give me height")
    height=int(input())   
    area=(1/2)*base*height
    print(area)

#     Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,

def area_rectangule():
    print("Hey, give me lenght")
    length=int(input())  
    print("Hey, give me width")
    width=int(input())   
    area=length*width
    print(area)

print("Hey, you want a rectangule or a triangule")
response=input()
if response == "rectangule":
    area_rectangule()  
        
elif response == "triangule":
        area_triangule()
else:
     area_triangule()
# If no shape is supplied then it should take triangle as a default shape

#     Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,

# *
# **
# ***

# if input is 4 then it should print

# *
# **
# ***
# ****



# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
def print_pattern(n):
    q="*"
    for i in range(1,n+1):
        print(q*i)

        
print("Hey, how many you want")
response1=input()
print_pattern(int(response1))