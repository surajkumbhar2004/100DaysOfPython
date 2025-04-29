''' Write a program that accepts the lengths of three sides of a triangle 
as inputs. The program output should indicate whether or not the triangle 
is a right triangle (Recall from the Pythagorean Theorem that in a right 
triangle, the square of one side equals the sum of the squares of the 
other two sides). '''

hypo = float(input("Enter length of Hypotenuse: "))
base = float(input("Enter Length Of Base: "))
perp = float(input("Enter length of Perpendicular: "))
if (hypo**2) == ((base**2) + (perp**2)):
    print("It is right Triangle")
else:
    print("Its Not a right Triangle")


