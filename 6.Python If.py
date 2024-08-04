# Exercise: Python If Condition
# Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]



#     Write a program that asks user to enter a city name and it should tell which country the city belongs to
print("Hey, give me a city name and I'll tell you wich country is from")
city=input()

for i in india:
    if i == city:
        print("Your country is India"),
        break

for i in pakistan:
        if i == city:
            print("Your country is Pakistan"),
            break
    
for i in bangladesh:
        if i == city:
            print("Your country is Bangladesh"),
            break

#     Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
print("Hey, give me a city name and I'll tell you if they are from the same country")
city1=input()
print("Now give me the second")
city2=input()

for i in india:
    if i == city1:
        city1Country= "india"
    if i == city2:
        city2Country= "india"  

for i in pakistan:
        if i == city1:
            city1Country= "pakistan"
        if i == city2:
            city2Country= "pakistan" 

for i in bangladesh:
        if i == city1:
            city1Country= "bangladesh"
        if i == city2:
            city2Country= "bangladesh"

if city1Country == city2Country :
        if city1Country == "india":
            print ("They are from the india")
        if city1Country == "pakistan":
            print ("They are from the pakistan")
        if city1Country == "bangladesh":
            print ("They are from the bangladesh")
else:
    print("They don't belong to same country")

# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.

#     Ask user to enter his fasting sugar level
#     If it is below 80 to 100 range then print that sugar is low
#     If it is above 100 then print that it is high otherwise print that it is normal

print("Hey, give me your sugar level")
sugarlvl=int(input())
if sugarlvl > 100 :
        print("Your sugar level is high")
else:
    if sugarlvl < 80 :
        print("Your sugar level is low")
    else:
        print("Your sugar level is normal")