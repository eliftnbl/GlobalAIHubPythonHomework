name = input("Enter your first name:")
surname = input("Enter your last name:")
age = int(input("Enter your age:"))
birth = int(input("Enter your date of birth(in year):"))
liste = [name, surname, age, birth]

for i in liste:
    print("First name {} ".format(name))
    print("Surname {} ".format(surname))
    print("Age {} ".format(age))
    print("Birth {} ".format(birth))

if age < 18 :
    print("You can't go out because it is too dangerous!")
else :
    print("You can go out to the street")
