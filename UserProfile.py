# UserProfile.py
# --- USER PROFILE ---
user_name = "Jonathan G. Junio"       # String
user_age = 22                     # Integer
user_height = 1.75                # Float
user_city = "Bayambang"            # String
is_student = True                 # Boolean

print("=== USER PROFILE ===")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Height: {user_height} meters")
print(f"City: {user_city}")
print(f"Student Status: {is_student}")
print()

# --- SIMPLE CALCULATOR ---
print("=== SIMPLE CALCULATOR ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nResults for {num1} and {num2}:")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} × {num2} = {num1 * num2}")
print(f"Division: {num1} ÷ {num2} = {num1 / num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponentiation: {num1} ^ {num2} = {num1 ** num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print()

# --- STRING OPERATIONS ---
print("=== STRING OPERATIONS ===")
greeting = "Hello, " + user_name + " from " + user_city + "!"
print("Concatenated greeting:", greeting)
print("-" * 30)
print("Name in uppercase:", user_name.upper())
print("Name in lowercase:", user_name.lower())
print("Name length:", len(user_name), "characters")
print(f"Formatted user info: {user_name} is {user_age} years old, {user_height}m tall, and lives in {user_city}.")
print()

# --- DATA TYPE INFORMATION ---
print("=== DATA TYPE INFORMATION ===")
print("Type of user_name:", type(user_name))
print("Type of user_age:", type(user_age))
print("Type of user_height:", type(user_height))
print("Type of is_student:", type(is_student))
print("Type of addition result:", type(num1 + num2))
print()

# --- COMPARISON OPERATIONS ---
print("=== COMPARISON OPERATIONS ===")
print(f"Is {num1} equal to {num2}? {num1 == num2}")
print(f"Is {num1} greater than {num2}? {num1 > num2}")
print(f"Is {num1} less than or equal to {num2}? {num1 <= num2}")
print()

print("=== ACTIVITY COMPLETE ===")
