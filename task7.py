

##1####
for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

###2#####
num = int(input("Enter a number: "))
sum = 0

for i in range(1, 10 + 1):
    sum += i

print("Sum of numbers from 1 to", 10, "is:", sum)



###3####
name = input("Enter Your name: ")

length = len(name)

for i in range(1, length + 1):
    print(name[:i].lower())

for i in range(length - 1, 0, -1):
    print(name[:i].lower())


####4######

word = input("Input a word to reverse: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)


####5######
n = int(input("Enter range: "))

while n >= 1:
    print('10','9','8','7','6','5','4','3','2','1')
    n -= 1
    print('\n')
###6######
i=11
for i in range(1, 11):
    i = 5 * i
    print(i,end="")
print('\n')
###7####

Limit_number = int(input("Enter the Limit_number: "))
Max_display_on_screen = int(input("Enter the Max_display_on_screen: "))
Target_number = int(input("Enter the Target_number: "))

count = 0
num = Target_number

while num <= Limit_number and count < Max_display_on_screen:
    print(num, end=" ")
    num += Target_number
    count += 1