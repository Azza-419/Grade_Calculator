import math

total_marks = float(input("What was your total amount of marks?: "))
out_of = float(input("What were those marks out of?: "))


if total_marks > out_of:
    print("Invalid: Total marks cannot be greater than the total possible marks.")
elif out_of <= 0:
    print("Invalid: Total marks out of should be greater than zero.")
else:
  
    percentage = round(total_marks / out_of * 100)
    print(f"Your score was {percentage}%")

    if percentage <= 0:
        print("Yeah buddy, better luck next time!")
        print("Your grade would be an: E")
    elif percentage < 50:
        print("You failed")
        print("Your grade would be a D")
    elif 50 <= percentage <= 65:
        print("Congrats! I mean, it's alright like")
        print("Your grade will be a: C")
    elif 65 < percentage < 75:
        print("Good job!")
        print("Your grade would be a B")
    elif percentage >= 75:
        print("You got an A I think!")



