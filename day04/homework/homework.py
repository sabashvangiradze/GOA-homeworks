#მომხმარებელს შემოაყვანინე სამი რიცხვი, ხოლო პროგრამამ დაბეჭდოს მათი საშუალო არითმეტიკული.

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
num3 = int(input("Enter any number: "))
num4 = num1 + num2 + num3
print(num4 // 3)

#მომხმარებელს შემოატანინე ორი რიცხვი და დაბეჭდე მათი ჯამი.

num_1 = int(input("Enter any number: "))
num_2 = int(input("Enter any number: "))
num_3 = num_1 + num_2
print(num_3)

#input ფუნქციის საშუალებით შემოიყვანეთ თქვენი და თქვენი ოჯახის წევრების სახელები და დაპრინტეთ ერთი დიდი წინადადება კონკატენაციის სახით.

user1 = input("Enter your name: ")
user2 = input("Enter your name: ")
user3 = input("Enter your name: ")
print("Hello my name is " + user1 + " my mother name is " + user2 + " my father name is " + user3)

#მომხმარებელს შემოატანინეთ მისი ქალაქის, უბნის, კორპუსის და სართულის შესახებ ინფორმაცია (რომლებიც უნდა შეინახოთ ცალ-ცალკე ცვლადებში). მაგ. city = "Tbilisi", District = "{თქვენი უბანი}" და ა.შ. საბოლოოდ print() ბრძანების საშუალებით ტერმინალში გამოიტანეთ მომხმარებლის სრული მისამართი.

city = input("Enter your city name: ")
district = input("Enter your district: ")
building = input("Enter your building: ")
floor = input("Enter your floor: ")
print("Hello i live in " + city + " my district is " + district + " my building is " + building + " im living on " + floor + " floor")

#მომხმარებელს შემოატანინეთ ასაკი და გამოყენებით მსგავსი ფორმატის წინადადება: "You are ასაკი years old".
ასაკი = input("Enter your age: ")
print("You're " + ასაკი + " years old" )