#Exercise: Python Variables

#Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.

#break = 5 -- It can't be used as a variable because it's a defined word for loops.

#Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables

birthYear = 2003
nowYear = 2024
Year = nowYear - birthYear
print (Year)

#Store your first, middle and last name in three different variables and then print your full name using these variables

firstName = "Rafael"
MiddleName = "Hernández"
LastName = "Silva"

Fullaname = firstName + " " + MiddleName + " " + LastName

print (Fullaname)

#Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue
_nation = 1
#1record = 1 It can't start with numbers
record1 = 1
record_one = 1
#record-one = 1 It can't use dash
#record^one = 1  It can't use that
#continue = 1 Thats a reserved word