# this is going to be my newton problem solution

desired_num = float(input("what number to find square root?  don't be a jerk, only use positive numbers!! "))
guess = float(input("what is a close guess?  "))
new_guess = ((desired_num / guess) + guess) / 2

new_guess2 = ((desired_num / new_guess) + new_guess) / 2

new_guess3 = ((desired_num / new_guess2) + new_guess2) / 2

new_guess4 = ((desired_num / new_guess3) + new_guess3) / 2

new_guess5 = ((desired_num / new_guess4) + new_guess4) / 2

new_guess6 = ((desired_num / new_guess5) + new_guess5) / 2

new_guess7 = ((desired_num / new_guess6) + new_guess6) / 2

new_guess8 = ((desired_num / new_guess7) + new_guess7) / 2

new_guess9 = ((desired_num / new_guess8) + new_guess8) / 2

new_guess10 = ((desired_num / new_guess9) + new_guess9) / 2

print("the square root of {} is {} +/-.01").format(desired_num, round(new_guess10, 2))
