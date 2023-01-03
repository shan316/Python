
print("***** Conditional Steps ******* \n")

x = 5
if x < 10:
    print('Smaller')
if x > 10:
    print('Bigger')
print("Finish\n\n")

print("**** Comparison Operator *****\n")

x = 2
if x == 5:
    print("Equal to 5")
if x >= 4:
    print("greater than 4")
if x <= 3:
    print("It could be 1, 2 or 3")
if x != 0:
    print("It is a positive integer\n\n")

print("**** Nested Decision Example 1*****\n")

x = 5
if x > 2:
    print("Bigger than 2")
    print("Still bigger than 2")
print("Done with 2")

for i in range (5):
    print(i)
    if i > 2:
        print("Bigger than 2")
    print("Done with i", i)
print("All Done")

print("**** Nested Decision Example 2 *****\n")

x = 42
if x > 1:
    print("More than one")
    if x < 100:
        print("Less than 100")
print("All Done")

print("**** Two Way Decision *****\n")

x = 1
if x > 2:
    print("Bigger")
else:
    print("Smaller")
print("All Done")

print("**** Review Question 7 *****\n")

x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

