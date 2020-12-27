

student_name="ELİF TONBUL"
count=0
for i in range (0,4):
    entered_name=input("Name-Surname(please write in capital letters) : ")
    if entered_name==student_name:
        print("Welcome {}".format(student_name))
        break
    else :
        count=count+1 
        if count == 3 :
            print("Please try again later !")
            break
        continue
entered_lessons=list()

for j in range(0,5):
    
    entered_lessons.append(input("Enter your lessons(please write in capital letters) :"))
    
wantto_taken_courses=int(input("How many lessons do you want to take? :"))
if wantto_taken_courses<3:
    print("You failed in class...")
    
elif wantto_taken_courses>3 and wantto_taken_courses<5:
    taken_courses=wantto_taken_courses
else :
    print("You can take at least 3 and at most 5 lessons")
notes={"midterm" :70,"final":90,"project":88}

midterm=notes["midterm"]*0.30
final=notes["final"]*0.50
project=notes["project"]*0.20

grade= midterm+final+project 

if grade>90:
    print("Your get AA")
elif grade>70 and grade<90:
    print("Your get BB")
elif grade>50 and grade<70:
    print("You get CC")
elif grade>30 and grade<50:
    print("You get DD")
elif grade<30:
    print("Failure")





