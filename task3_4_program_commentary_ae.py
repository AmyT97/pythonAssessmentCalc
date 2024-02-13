#Task 3 and 4 
#write a program based on your design. 
#You should be using subprograms (functions) and parameter passing within the program. 
#Remember to use meaningful variable names, internal commentary and indentation. 
#Use internal commentary to explain the purpose of using subprograms (functions) and parameter passing and how they work. 

#Aurthor Amy Eastcroft 
#Date 23/01/24
#Description - Task 3 & 4 Grading Program

# Functions
# ---------

#this function gets students name
def getStudentName(): 
    studentNameInput = input("Please enter your name :\n")
    return studentNameInput

#this function gets students coursework mark and validates input against the highest possible mark of 60. 
#assigning the variable with an initial value that is true so that the prompt from the while loop is displayed. 
#if user enters a value of -1 or 61 for example the while loop will be true and they will be prompted again for a valid input within the 0 - 60 range.  
def getCourseWorkMark():
    courseWorkInput = -1 
    while courseWorkInput < 0 or courseWorkInput > 60 : 
        courseWorkInput = int(input("Please enter your coursework mark :\n"))
    return courseWorkInput

#this function gets students prelim mark and validates input against the highest possible mark of 90.
#assigning a variable to the output of the input() function.
#assigning initial true value to variable.    
def getPrelimMark():

    prelimMarkInput = -1 
    while prelimMarkInput < 0 or prelimMarkInput > 90 : 
        prelimMarkInput = int(input("Please enter your prelim mark :\n"))
    return prelimMarkInput
    
#this function uses parameter passing, it takes two parameters and uses these in the calculation then returns percentage.
def getPercentage(courseWorkMarkInput, prelimMarkInput): 
    percentageCalculated = ((courseWorkMarkInput + prelimMarkInput) * 100 / 150)
    return percentageCalculated

#This function compares percentage against grading metric to give grade A - D. 
#Note that the parameter percentCalculated is independant to this function and not the same as the return value percentageCalculated from the previous function despite having the same name. 
def getGrade(percentageCalculated):
    if percentageCalculated >= 70:
        gradeCalculated = "A"
    elif percentage > 60 and percentage < 69: 
        gradeCalculated = "B"
    elif percentage > 50 and percentage < 59:
        gradeCalculated = "C"
    elif percentage > 45 and percentage < 49:
        gradeCalculated = "D"
    else:
        gradeCalculated = "No Award"
    return gradeCalculated

#This function determines whether the student has passed or failed their SCQF level 6. 
def passOrFail(calculatedGrade):
    if calculatedGrade == "No Award":
        examDecision = "Fail."
    else:
        examDecision = "Pass!"
    return examDecision

#This function displays the students percentage, grade and pass or fail result for their SCQF level 6. 
def displayResult(studentName, studentPercentage, studentGrade, studentResult):
    print(f"{studentName}, your SCQF level 6 Computing Science Results are: \nCombined Percentage(coursework and prelim) - {studentPercentage:.0f}% \nGrade - {studentGrade} \nResult - {studentResult}")


# Main
# ------

#calling the functions having assigned variable names to their outputs e.g., getCourseWorkMark() function output assigned to courseWorkMark
#using parameter passing to get the output of a function by using the output of a previous function(s) e.g., passOrFail() function requires output from getGrade() function.
studentName = getStudentName()
courseWorkMark = getCourseWorkMark()
prelimMark = getPrelimMark()
percentage = getPercentage(courseWorkMark, prelimMark)
grade = getGrade(percentage)
decision = passOrFail(grade)
result = displayResult(studentName, percentage, grade, decision)


