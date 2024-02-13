#Task 7
#Alter your program to enable it to find out how many 'A' passes are in the class by using the "Count Occurences" standard algorithm. 
#Alter your program to enable it to find out the best percentage in the class by using "Finding Max" standard algorithm. 
#Use internal commentary to describe how the count occurences and finding max algorithms work. 

#Aurthor Amy Eastcroft 
#Date 11/02/24
#Description - Task 7 Count Occurences & Finding Max

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


def readFiles(fileName):
    with open(fileName,'r') as file:
        itemList = file.read().splitlines()
        return itemList
    
def combineLists():
    combinedList = list(zip(names, mark1, mark2))
    return combinedList


def countOccurences():
    countA = 0
    for grade in gradeList:
        if grade == 'A':
            countA += 1
    return countA


# Main
# ------
names = readFiles('names.txt')
mark1 = readFiles('mark1.txt')
mark2 = readFiles('mark2.txt')
combinedList = combineLists()
gradeList = []
maxResult = 0
for item in combinedList:
    courseWorkMark = int(item[1])
    prelimMark = int(item[2])
    percentage = getPercentage(courseWorkMark, prelimMark)
    grade = getGrade(percentage)
    gradeList.append(grade)
    if maxResult < percentage:
        maxResult = percentage
countA = countOccurences()
print(f"The number of 'A' passes in the class is: {countA}")
print(f"The best percentage in the class is: {maxResult}%")

#In this program I use a 'count occurences' and a 'finding max' algorithm.
 
#The count occurences algorithm was used in my countOccurences() function:
#Initial countA is set to 0 
#Using a for loop I can iterate through each grade in gradeList
#Everytime there is an 'A' grade 1 is added to the countA variable 
#Once each item in the list has been iterated through the function returns the final countA value. 
#I can then print out this value. 

#The finding max algorithm was used in my main:
#Inital maxResult was set to 0 
#Using an if statement I compare the maxResult with the percentage 
#In cases where percentage is greater than the maxResult then the maxResult value is replaced by the percentage value. 
#If the percentage is smaller maxResult stays the same. 
#Since the if statement is within the for loop this comparison will be done for each item in the list as we iterate through it. 
#Once each item in the list has been iterated through the maxResult can be returned and printed out. 