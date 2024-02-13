#Task 6 
#Your program only works for one candidate at present.
#Alter your program so that it will read the name, coursework mark and prelim mark for all the 15 studentes in your class from external files. 

#Aurthor Amy Eastcroft 
#Date 09/02/24
#Description - Task 6 Multiple Students

# Functions
# ---------

    
def getPercentage(courseWorkMarkInput, prelimMarkInput): 
    percentageCalculated = ((courseWorkMarkInput + prelimMarkInput) * 100 / 150)
    return percentageCalculated

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

def readFiles(fileName):
    with open(fileName,'r') as file:
        itemList = file.read().splitlines()
        return itemList
    
# Open is a built in function and file operation in python which requires filename and mode parameters i.e. open(filename, mode). 
# Within the function I have used the variable fileName to allow me to reuse it in my main for all three files.
# The mode is 'r' which means read mode. 
# This open function needs to be stored into a variable here it is returned as the variable itemList.

def combineLists():
    combinedList = list(zip(names, mark1, mark2))
    return combinedList

def displayResult(studentName, studentPercentage, studentGrade, studentResult):
    print(f"{studentName}, Combined Percentage: {studentPercentage:.0f}%, Grade: {studentGrade}, Result: {studentResult}\n")

# Main
# ------

names = readFiles('names.txt')
mark1 = readFiles('mark1.txt')
mark2 = readFiles('mark2.txt')
combinedList = combineLists()
for item in combinedList:
    studentName = item[0]
    courseWorkMark = int(item[1])
    prelimMark = int(item[2])
    percentage = getPercentage(courseWorkMark, prelimMark)
    grade = getGrade(percentage)
    decision = passOrFail(grade)
    result = displayResult(studentName, percentage, grade, decision)
