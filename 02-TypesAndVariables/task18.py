a = input("Enter the first side: ")
b = input("Enter the second side: ")
c = input("Enter the third side: ")
a = int(a)
b = int(b)
c = int(c)

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"Area for this triangle is {area}")  