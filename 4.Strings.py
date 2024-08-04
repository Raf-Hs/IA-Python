#Exercise: String in Python

    #Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
street= "Street"
city= "City"
country= "Mexico"
adress = "\n" + street + "\n" + city +"\n" + country
print(adress)
print(f"Estoy es un f string {adress}")   

     #Create a variable to store the string "Earth revolves around the sun"
sentence = "Earth revolves around the sun"

x = slice(6,14)
print(sentence[x])
#print(s[6:14])
#print(s[-3:])
        #Print "revolves" using slice operator
        #Print "sun" using negative index
x= 0
y=0
print(f"I eat {x} veggies and {y} fruits daily ")
    #Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
    #I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
s='maine 200 banana khaye'
x = s.replace("200", "10") 
y = x.replace("banana", "samosa")
print (y)


s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)