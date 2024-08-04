# Exercise: Python for loop

#     After flipping a coin 10 times you got this result,

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

# Using for loop figure out how many times you got heads
count= 0
for i in result:
    if i == "heads":
        count += 1

print(count)

#     Print square of all numbers between 1 to 10 except even numbers
count1= 0
for i in range(10):
    if i % 2 == 1:
        value=i*2
        print(value)
        count1 += 1



#     Your monthly expense list (from Jan to May) looks like this,

expense_list = [2340, 2500, 2100, 3100, 2980]

# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.
print("Hey, give me a expense")
expense=int(input())

for i in expense_list:
    if i == expense:
        print("Yeah, we have those")
        break
    else:
        print("Nah")
        break

#     Lets say you are running a 5 km race. Write a program that,
#         Upon completing each 1 km asks you "are you tired?"
#         If you reply "yes" then it should break and print "you didn't finish the race"
#         If you reply "no" then it should continue and ask "are you tired" on every km
#         If you finish all 5 km then it should print congratulations message


for i in range(4):
    print("Are you tired?")
    response=input()
    if response == "yes":
        print("you didn't finish the race")
        break
print("congratulations")
        
        
#     Write a program that prints following shape
q="*"
for i in range(6):
    print(q*i)
    
# *
# **
# ***
# ****
# *****
