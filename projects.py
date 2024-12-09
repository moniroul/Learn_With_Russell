# projects.py

# 1. Calculate the area of a triangle
#ত্রিভুজ ক্ষেত্রের ক্ষেত্রফল নির্ণয়ের প্রোগ্রাম:
def calculate_triangle_area(base, height):
    return 0.5 * base * height





# 2. Sum of odd numbers from 1 to 100
# 2. ১ থেকে ১০০ পর্যন্ত বিজোড় সংখ্যাগুলোর যোগফল:
def sum_of_odd_numbers(): 
    odd = (i for i in range(1, 101) if i % 2 != 0)
    return sum(odd)

# if you want odd => (i for i in range(1, 101) if i % 2 != 0) 

# if you want even => (i for i in range(1, 101) if i % 2 == 0)



# 3. Store data in a file
# 3. একটি ফাইলে ডাটা স্টোর করার প্রোগ্রাম:
def store_data_in_file(filename, data):
    # Write the data to the file
    with open(filename, 'w') as file:
        file.write(data)
   
        
    






# 4. Solve quadratic equation
def solve_quadratic(p, q, r):
    import cmath
    discriminant = cmath.sqrt(q**2 - 4*p*r)
    root1 = (-q + discriminant) / (2*p)
    root2 = (-q - discriminant) / (2*p)
    return root1, root2





# 5. ১ থেকে ১০০ পর্যন্ত ৭ দিয়ে বিভাজ্য সংখ্যাগুলোর যোগফল:
# 5. Sum of numbers divisible by 7 from 1 to 100
def sum_of_numbers_divisible_by_7():
    return sum(i for i in range(1, 101) if i % 7 == 0)





# 6. তিনটি সংখ্যার মাঝে ছোট সংখ্যা নির্ণয়ের ফ্লোচার্ট:
# 6. Find the smallest of three numbers
def smallest_of_three(a, b, c):
    return min(a, b, c)




# 7. রাশিটি Python ভাষায় রূপান্তর:
# 7. Mathematical expression conversion
# x = 2 * (y / 2 - z / 2) ** (3 / 4)
def calculate_expression(y, z):
    return 2 * (y / 2 - z / 2) ** (3 / 4)



# "9. সিরিজ 1 + 3 + 5 + 7 + ⋯ + 99 1+3+5+7+⋯+99-এর যোগফল নির্ণয়:"
# 8. Sum of the series 1 + 3 + 5 + ... + 99
def sum_of_series():
    return sum(range(1, 100, 2))

 


# Main function to run specific tasks
def main():
    
    
    print("1. Calculate Triangle Area")
    
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    
    print(f"Triangle Area  : {calculate_triangle_area(base, height)}")
    
    
    
    
    print("\n2. Sum of Odd Numbers from 1 to 100")
    print(f"Sum: {sum_of_odd_numbers()}")
    
    
    
    
    print("\n3. Store Data in File")
    filename = "data.txt"
    data = input("Enter data to store: ")
    res = store_data_in_file(filename, data)
    print(f"Data stored in {filename} filedata: {res}")
    
    
    
    
    print("\n5. Sum of Numbers Divisible by 7 from 1 to 100")
    print(f"Sum: {sum_of_numbers_divisible_by_7()}")
    
    
    
    
    print("\n6. Smallest of Three Numbers")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print(f"Smallest Number: {smallest_of_three(a, b, c)}")
    
    
    
    
    
    print("\n8. Sum of the Series 1 + 3 + 5 + ... + 99")
    print(f"Sum: {sum_of_series()}")
    
    
    
    
    
    print("\n7. Mathematical Expression")
    y = float(input("Enter value for y: "))
    z = float(input("Enter value for z: "))
    print(f"Result: {calculate_expression(y, z)}")    




    
    # "8. 𝑃 ⋅ 𝑥 2 + 𝑄 𝑥 + 𝑅 = 0 P⋅x 2 +Qx+R=0 সমীকরণের মূল নির্ণয়ের প্রোগ্রাম:"
    print("\n4. Solve Quadratic Equation")
    p = float(input("Enter coefficient P: "))
    q = float(input("Enter coefficient Q: "))
    r = float(input("Enter coefficient R: "))
    roots = solve_quadratic(p, q, r)
    print(f"Roots: {roots[0]} and {roots[1]}")
    
     
    
    


# Execute the main function
if __name__ == "__main__":
    main()
