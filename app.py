import cmath


p = float(input("Enter P: "))
q = float(input("Enter Q: "))
r = float(input("Enter R: "))

discriminant = cmath.sqrt(q**2 - 4*p*r)

root1 = (-q + discriminant) / (2*p)
root2 = (-q - discriminant) / (2*p)
 
print(f"Roots: {root1} and {root2}")


