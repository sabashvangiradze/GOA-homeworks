#input-ნიშნავს იმ მონაცემს ან ინფორმაციას რომელსაც სისტემა იღებს, მაგალითად კლავიატურის,მაუსის ან მიკროფონის გამოყენებით
#output-არის ის შედეგი ან ინფორმაცია რასაც სისტემა გვიბრუნებს input-ის მიღების შემდგომ. output-ის საშუალებებია:მონიტორი,პრინტერი,დინამიკი და სხვა.

age = input("Enter your age: ")
print(type(age))


user = "Saba"
#str

age =  15
#int

score = 12.4
#float

address = "Gldani"
#str

net_worth = 470
#int


user_1 ="Saba"
print(type(user_1))

age_1 = 15
print(type(age_1))

score_1 = 12.4
print(type(score_1))


name = input("Enter your name: ")
surname = input("Enter your surname: ")

print(name + surname)


num = int(input("Enter your number: "))
num1 = float(input("Enter your number: "))
num2 = int(input("Enter your number: "))
num3 = float(input("Enter your number: "))
num4 = int(input("Enter your number: "))

print((num + num1 + num2 + num3 + num4)/2)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
user_age = input("Enter your age: ")
user_height = input("Enter your height: ")
user_bodyweight = input("Enter your bodyweight: ")
print("Hello my name is " + first_name + "my last name is " + last_name + "my age is " + user_age + "my height is " + user_height + "cm " + "and i weigh " + user_bodyweight + "kg")