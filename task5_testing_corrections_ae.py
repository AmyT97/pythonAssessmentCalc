#Task 5 
#Test the program using your test plan
#If neccessary make any ammendments to your program. 

#Aurthor Amy Eastcroft 
#Date 09/02/24
#Description - Task 5 Testing and Correction

# Functions
# ---------

def getStudentName(): 
    studentNameInput = input("Please enter your name :\n")
    return studentNameInput

#Correction: float type casting instead of int type casting.   
def getCourseWorkMark():
    courseWorkInput = -1 
    while courseWorkInput < 0 or courseWorkInput > 60 : 
        courseWorkInput = float(input("Please enter your coursework mark :\n"))
    return courseWorkInput

#Correction: float type casting instead of int type casting.    
def getPrelimMark():

    prelimMarkInput = -1 
    while prelimMarkInput < 0 or prelimMarkInput > 90 : 
        prelimMarkInput = float(input("Please enter your prelim mark :\n"))
    return prelimMarkInput
    
def getPercentage(courseWorkMarkInput, prelimMarkInput): 
    percentageCalculated = ((courseWorkMarkInput + prelimMarkInput) * 100 / 150)
    return percentageCalculated

#Correction: use >= and <= rather than = to ensure extreme values are included
def getGrade(percentageCalculated):
    if percentageCalculated >= 70:
        gradeCalculated = "A"
    elif percentage >= 60 and percentage <= 69: 
        gradeCalculated = "B"
    elif percentage >= 50 and percentage <= 59:
        gradeCalculated = "C"
    elif percentage >= 45 and percentage <= 49:
        gradeCalculated = "D"
    else:
        gradeCalculated = "No Award"
    return gradeCalculated

def passOrFail(calculatedGrade):
    if calculatedGrade == "No Award":
        examDecision = "Fail."
    else:
        examDecision = "Pass!"
    return examDecision

def displayResult(studentName, studentPercentage, studentGrade, studentResult):
    print(f"{studentName}, your SCQF level 6 Computing Science Results are: \nCombined Percentage(coursework and prelim) - {studentPercentage:.0f}% \nGrade - {studentGrade} \nResult - {studentResult}")


# Main
# ------

studentName = getStudentName()
courseWorkMark = getCourseWorkMark()
prelimMark = getPrelimMark()
percentage = getPercentage(courseWorkMark, prelimMark)
grade = getGrade(percentage)
decision = passOrFail(grade)
result = displayResult(studentName, percentage, grade, decision)


