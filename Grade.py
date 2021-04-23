
print("Welcome to grade calculator!!!")
print(" --------")
print("|  -   - |")
print("|   __   |")
print(" --------")

Mathpoint = 0
Socialpoint = 0
Artpoint = 0
Physicspoint = 0
calculating = 0
Mathgrade = 0
Socialgrade = 0
Artgrade = 0
Physicsgrade = 0
credit_Container = 0
Student_Grade_Container = 0
Havepoint = False


#-----------------------------------------------------------#

class Subject:

    def __init__(self, subject, credit,work,score,allscore):
        self.subject = subject
        self.credit = credit
        self.work = work
        self.score = score
        self.allscore = allscore

check_point = input("Did you have all of your scores? [Y/N] : ")

if check_point == "Y" or check_point == "y":
    print("Put your score right here.")
    print("-----------")
    Havepoint = True
elif check_point == "N" or check_point == "n":
    print("Put your score for each work right here.")
    print("-----------")
    Havepoint = False
else:
    print("I guess you don't have it.")
    print("-----------")
    Havepoint = False

Math = Subject("Math", 2,["Book : ", "Test1 : ", "Test2 : ","Midterm : ","Test3 : ", "Test4 : ", "Final : "],[],"Math :")
Social = Subject("Social", 1,["Test3: "],[],"Social : ")
Art = Subject("Art",0.5,["Test4: "],[],"Art : ")
Physics = Subject("Physics",1.5,["Test5: "],[],"Physics : ")

AllSubjects = [Math,Social,Art,Physics]

Point = ({Math.subject : Mathpoint,
    Social.subject : Socialpoint,
    Art.subject : Artpoint,
    Physics.subject : Physicspoint})

Grade = ({Math.subject : Mathgrade,
    Social.subject : Socialgrade,
    Art.subject : Artgrade,
    Physics.subject : Physicsgrade})

for credits in AllSubjects:
    credit_Container = credit_Container + credits.credit

def Grade_Calculator(Student_Point):
    if 100 >= Student_Point >= 80:
        return 4.00
    elif 80 > Student_Point >= 75:
        return 3.50
    elif 75 > Student_Point >= 70:
        return 3.00
    elif 70 > Student_Point >= 65:
        return 2.50
    elif 65 > Student_Point >= 60:
        return 2.00
    elif 60 > Student_Point >= 55:
        return 1.50
    elif 55 > Student_Point >= 50:
        return 1.00
    elif Student_Point < 50:
        return 0
    else:
        print("WTF It's over 100 man...")


def Subject_append(Subject,x):
    #Subject.append(int(input(x)))
    while  True:
        try:
            get_input = int(input(x))
        except ValueError:
            print("Integer please....")
            continue
        else:
            Subject.append(get_input)
            break

def Credit_Calculating(subject_credit, Student_Grade):
    return float(subject_credit * Student_Grade)

def sum_grade(All_Credit,All_Student_Credit):
    return float(All_Student_Credit/All_Credit)

def Extrapoint(Bpoint):
    if (Bpoint + 1)%5 == 0:
        return Bpoint + 1
    else:
        return Bpoint


if Havepoint == False:

    for each_subject in AllSubjects:
        print("This is :", each_subject.subject)
        for work in each_subject.work:                                                                 #Get work from each Subject
            Subject_append(each_subject.score,work)                                                 #Collect point from each work
        for points in each_subject.score:                                                               #Get every point from each Subject
            calculating = calculating + points                                                          #Addition all point
        Point[each_subject.subject] = calculating
        calculating = 0
        for grade_subject in Grade:
            Grade[each_subject.subject] = Grade_Calculator(Point[each_subject.subject])         #Convert Point to GPA
        print("-----------")

        Student_Grade_Container = Student_Grade_Container +  Credit_Calculating(each_subject.credit,Grade[each_subject.subject])

    GPA = sum_grade(credit_Container,Student_Grade_Container)


if Havepoint == True:

    for each_subject in AllSubjects:
        Subject_append(each_subject.score,each_subject.allscore)
        Point[each_subject.subject] = each_subject.score[0]
        calculating = 0
        for grade_subject in Grade:
            Grade[each_subject.subject] = Grade_Calculator(Point[each_subject.subject])
        print("-----------")
        Student_Grade_Container = Student_Grade_Container +  Credit_Calculating(each_subject.credit,Grade[each_subject.subject])

    GPA = sum_grade(credit_Container,Student_Grade_Container)

print("Point :  ", Point)
print("Grade :  ", Grade)
print("GPA :   ", GPA)

print("-----------")

Student_Grade_Container = 0

for each_subject in AllSubjects:

        Point[each_subject.subject] = Extrapoint(Point[each_subject.subject])
        calculating = 0
        for grade_subject in Grade:
            Grade[each_subject.subject] = Grade_Calculator(Point[each_subject.subject])
        Student_Grade_Container = Student_Grade_Container +  Credit_Calculating(each_subject.credit,Grade[each_subject.subject])

newGPA = sum_grade(credit_Container,Student_Grade_Container)

print("After +1 Point")
print("Point :  ", Point)
print("Grade :  ", Grade)
print("GPA :   ", newGPA)

