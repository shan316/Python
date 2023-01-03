print("***** Multi-way with else ******* \n")

x = 20
if x < 2:
    print("smaller")
elif x > 10:
    print("Medium")
else:
    print("Bigger")
print("All Done")

print("***** Multi-way without else******* \n")

x = 5
if x < 2:
    print("smaller")
elif x > 10:
    print("Medium")
print("All done")

print("***** Try/Except ****")

x = input("Enter your number ")
try:
    x = int(x)
except:
    x = -1
if x < 0:
    print("Type Digit, not number in english")
if x > 0:
    print("Well done")

print("***** Review Question - 10 ******* \n")

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)
