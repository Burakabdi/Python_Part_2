# Ask the user for a number until user enters -1. Keep adding given user numbers before -1.

user_num = int(input("enter a number: "))
total = 0

while user_num != -1:
    total += user_num
    user_num = int(input("enter a number: "))

print(total)
  



