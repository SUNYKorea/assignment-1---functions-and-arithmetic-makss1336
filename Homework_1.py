# Name: Maksim Galkin
# SBUID: 115341166
##################### SCORE ######################
#######  Score:  7/10

#################################################
# Remove the ellipses (...) when writing your solutions.
#### your output
# Enter temperature in fahrenheit: 44
# Sweater -> correct
# The area of the triangle is : 32.5 , its perimeter is : 27.889011005163916 - >wrong
# The area of the polygon is : 5.160976731179886  - >wrong
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 


def fahrenheit2celsius(fahrenheit): 
   celsius = (5/9)*(fahrenheit - 32)
   return celsius 

def what_to_wear(celsius):
    if celsius < -10:
        return ("Puffy Jacket")
    elif celsius < 0:
        return ("Scarf")
    elif celsius < 10:
        return ("Sweater")
    elif celsius < 20:
        return ("Light Jacket")
    else:
        return ("T-Shirt")




# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs((x1*y1 + x2*y2 + x3*y3) - (x1*y3 + x2* y1 + x3*y2))
    return area

def euclidean_distance(x1, y1, x2, y2):
    distance = ((x1-y1)**2 + (y1 - y2)**2)**0.5 # you made a mistake here--> instead of x1-y1, it should be x1-x2
    return distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = euclidean_distance(x1, y1, x2, y2)
    s2 = euclidean_distance(x2, y2, x3, y3)
    s3 = euclidean_distance(x3, y3, x1, y1)
    perimeter = s1 + s2 + s3
    return perimeter


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 
import math

def deg2rad(deg):
    radian = deg * math.pi / 180
    return radian

def apothem(number_sides, length_side):
   apothemFormula = length_side / (2 * math.tan(180 / number_sides))
   return apothemFormula

def polygon_area(number_sides, length_side):
   n = number_sides
   s = length_side
   a = apothem(number_sides, length_side)
   area = n * s * a
   return area


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = float(input("Enter temperature in fahrenheit: "))
print (what_to_wear(fahrenheit2celsius(fahrenheit)))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))