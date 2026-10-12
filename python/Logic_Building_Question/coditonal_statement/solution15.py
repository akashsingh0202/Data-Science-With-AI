# [ ] 15. Classify a triangle as equilateral, isosceles, or scalene.
# Example: Sides: 5, 5, 8 → Isosceles

n1=int(input("enter first side :"))
n2=int(input("enter second side :"))
n3=int(input("enter third side :"))

if (n1==n2==n3):
    print("euilateral triangle")

elif(n1==n2 or n1==n3 or n2==n3):
    print("isosceles triangle")

else:
    print("Scalen")