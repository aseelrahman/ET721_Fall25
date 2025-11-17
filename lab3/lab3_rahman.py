"""
Aseel Rahman
lab 3, mastering git workflow
Sep 8, 2025
"""

"""
modify example 1:
- use while loop to validate if the user_number is between 1 and 9
- user can only guess three times. This can be done using a for loop or a while
"""
print("\n ----- Example 1:  -----")
# guess a number between 1 and 9
GUESS_NUM = 8
# collect the number
user_number = int(input("Guess a number: "))

attempt_num = 1

while 0 < user_number < 10:
    if user_number == GUESS_NUM:
        print(f"Great Job! {user_number} is the guess number")
        break
    elif user_number > GUESS_NUM:
        attempt_num += 1
        if attempt_num <= 3:
            print(f"{user_number} should be lower")
            user_number = int(input("Guess a number again: "))
        else:
            break
    elif user_number < GUESS_NUM:
        attempt_num += 1
        if attempt_num <= 3:
            print(f"{user_number} should be higher")
            user_number = int(input("Guess a number again: "))
        else:
            break
    else:
        break

"""
example 2:
- children under the age of 9 are only given milk for breakfast
- children from 10 to 14 are given sandwich
- children from 15 to 17 are given a burger
"""

age_student = int(input("Enter an age: "))
lunch = "None"
if age_student < 9 and age_student >= 5:
    lunch = "milk"
elif age_student >= 10 and age_student <= 14:
    lunch = "sandwich"
elif age_student >= 15 and age_student <= 17:
    lunch = "burger"
else:
    lunch = "None"

print(f"At age {age_student} the food is {lunch}")

print("\n ----- Example 3: for loop as a counter ------")
# 'for' loops enables the program to execute a code block multiple times
for n in range(2, 10):
    print(n)

print("\n ----- Example 4: for loop in a list -----")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"Year {index+1} = {years[index]}")

print("\n ----- Example 5: while loop as a counter -----")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\n ----- Example 6: while loop to validate a number -----")
# validate if a number is between -5 and 5 (inclusive)
num = int(input("Enter a number between -5 and 5: "))
# use a while to recollect if the num is not between -5 and 5
while num < -5 or num > 5:
    num = int(input("ERROR! Enter a number between -5 and 5: "))

print(f"Entered number = {num}")
