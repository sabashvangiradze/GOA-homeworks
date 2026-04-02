# 2)


# < (ნაკლებობა)
# > (მეტობა)
# >= (მეტია ან ტოლია)
# <= (ნაკლებია ან ტოლია)
# != (არ არის ტოლი)
# == (ტოლობა)

# ნაკლებობა

print(2 < 6) # True

# მეტობა 

print(10 > 5) # True

# ტოლობა

print(5 == 5) # True

# მეტია ან ტოლია

print(8 >= 8) # True

# ნაკლებია ან ტოლია

print(7 <= 2) # False

# 3)

# Logical operators - გამოიყენება ლოგიკური მნიშვნელობებისთვის
# True, False, And, Or 
# True - ჭეშმარიტია
# False - მცდარია
# And - გამოიტანს ჭეშმარიტს, თუ ორივე პირობა სწორია, დანარჩენ სხვა შემთხვევაში იგი მცდარია
# Or - გამოიტანს ჭეშმარიტს, თუ ერთ-ერთი პირობა სწორია, დანარჩენ სხვა შემთხვევაში ეს მცდარია

# 4)

#1

age = 20
has_id = True

print(age >= 18 and has_id)  # True

#2

is_raining = False
has_umbrella = True

print(is_raining or has_umbrella) #True

#3

is_logged_in = True
has_permission = False

print(is_logged_in and has_permission) #False



# 5)

number = 15
number1= int(input("Enter your number: "))
print(number1 >= number)



# 6) 

name = "Saba"
name1 = input("Enter your name: ")
print(name == name1)



# 7)

age = 18
age1 = int(input("Enter your age: "))
print(age1 >= age)