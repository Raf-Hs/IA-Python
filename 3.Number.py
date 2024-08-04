#3. Numbers
#You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
long = 92.0
wide = 48.8
area = long * wide
print(area)
#You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
potatoChips= 9.0
PacketCost = 1.49
Payment= 20.00
Total = potatoChips*PacketCost
Cashback= Payment- Total
print(Cashback)
#You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

bathroomLenght = 5.5
tilesCost= 500.0
area = bathroomLenght ** 2
TotalPrice = area * tilesCost

print(TotalPrice)

#Print binary representation of number 17
num = 17
print('Binary of number 17 is:',format(num,'b'))