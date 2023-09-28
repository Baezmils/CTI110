"""
CTI 110
P3LAB2 - Letter grades
BaezS
9/28/2023

convert a number grade into a letter grade. (ten point scale)
"""
#get the number grade
print("enter the number grade: " , end="")
num_grade = int(input())

letter_grade = "G"
# do the convertion
if num_grade >= 90:
  letter_grade = "A"
elif num_grade >= 80:
  letter_grade = "B"
elif num_grade >= 70:
  letter_grade = "C"
elif num_grade >= 60:
  letter_grade = "D"
else: # or elif num_grade < 60:
  letter_grade = "F"

# print the letter grade
print("a grade of", num_grade, "is a", letter_grade)


