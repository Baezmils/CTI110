# CTI 110
# P4HW1 - score lists
# BaezS
# 10/10/23

list = []
scoring = True
num_scores = 0
num_scores = int(input("how many scores do you want to enter? "))
for scores in range(num_scores):
  scores = scores + 1
  score_list = "enter score #" + str(scores)
  print(score_list, end=": ")
  score_ammount = int(input())
  while score_ammount <0 or score_ammount> 100:
    print()
    print("INVALID score entered!!!!") 
    print("score should be between 0 and 100")
    print("enter score #" + str(scores) + " again: ", end="")
    score_ammount = int(input())
  list.append(score_ammount)
average = sum(list) / num_scores
if average >= 90:
 grade = "A"
if average >= 80:
  grade = "B"
if average >= 70:
  grade = "C"
if average >= 60: 
  grade = "D"
else:
  grade = "F"
print("-"*10, "results", "-"*10)
lowest = min(list)
print("Lowest score : ", lowest)
list.remove(lowest) # take the lowest variable out of the list

print("Modified list : ", list)
print("Scores average", average)
print("Grade : ", grade)



