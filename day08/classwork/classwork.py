# 1

# Logical operators - გამოიყენება ლოგიკური მნიშვნელობებისთვის
# (True / False) - ერთმანეთთან შესადარებლად ან დასაკავშირებლად.
# (And / or ) - და / ან კავშირი 


# and აბრუნებს True-ს მხოლოდ მაშინ,როცა ორივე პირობა არის True.სხვა ყველა შემთხვევაში აბრუნებს False-ს.

# or აბრუნებს True-ს მაშინ,როცა მინიმუმ ერთი პირობა მაინც არის True.False იქნება მხოლოდ მაშინ, როცა ორივე False-ია.


# 2

#  ==  (ტოლია)
print(5 == 5)      # True
print(10 == 7)     # False
print("hi" == "hi") # True

# !=  (არ არის ტოლი)
print(5 != 3)      # True
print(8 != 8)      # False
print("a" != "b")  # True

#  >  (მეტია)
print(10 > 5)      # True
print(3 > 9)       # False
print(7 > 7)       # False

# <  (ნაკლებია)
print(2 < 6)       # True
print(9 < 4)       # False
print(5 < 5)       # False

#  >=  (მეტია ან ტოლია)
print(8 >= 8)      # True
print(10 >= 3)     # True
print(2 >= 6)      # False

# <=  (ნაკლებია ან ტოლია)
print(4 <= 4)      # True
print(3 <= 9)      # True
print(7 <= 2)      # False

# 3

# 1)

age = 20
has_id = True

print(age >= 18 and has_id)  

# 2)

is_raining = False
has_umbrella = True

print(is_raining or has_umbrella)