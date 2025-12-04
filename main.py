import numpy as np

student = int(input("Enter the count of student: "))
subject = int(input("Enter the marks of student each subject: "))
arr = []
print("\n Enter the each subject marks: ")
for i in range(student):
    subject_wise = list(map(int, input().split()))
    arr.append(subject_wise)
data = np.array(arr)
print(data)

## each subject wise highest, lowest and avgerage 

highest = np.max(data, axis = 0)
lowest = np.min(data, axis = 0)
avg = np.mean(data, axis = 0)
for i in range(subject):
    print(f"Subject {i + 1} : highest = {highest[i]}, lowest = {lowest[i]}, avg = {avg[i]:.2f}")


##overall subject highest, lowest, and mean


overall_highest = np.max(data)
overall_lowest = np.min(data)
overall_avg = np.mean(data)

print("overall subject highest marks:", overall_highest)
print("overall subject lowest marks:", overall_lowest)
print("overall subject average marks:", overall_avg)


##find passed_student and percentage

passed_marks = 35
passed_student = np.sum(np.all(data >= passed_marks, axis = 1))
passed = (passed_student / student) * 100

print("passed_students : ",passed_student)
print("passed student percentage:", passed)



##find the total marks in top three rankers

total_marks = np.sum(data, axis = 1)
sorted_marks = np.argsort(total_marks)[::-1]
for i in range(3):
    idx = sorted_marks[i]
    print(f"Rank {i + 1} : student {idx + 1} - Total marks = {total_marks[idx]}")


## add grace marks 5

grace_marks = data + 5
print("after adding grace_marks", grace_marks)


## after adding grace marks find passed_student and percentage
passed_marks = 35

passed_percentage_after = np.sum(np.all(grace_marks >= passed_marks, axis = 1))
after_passed_marks = (passed_percentage_after / student * 100)

print("after adding grace marks passed student :", passed_percentage_after)
print("after adding grace marks passed student:", after_passed_marks)

## comparsion of both before and after adding grace marks

print("before passed marks", passed_student)
print("after passed marks", passed_percentage_after)
print("final passed_marks newly passed", passed_percentage_after - passed_student)


print("before passed percentage {:.2f}".format(passed))
print("after passed percentage {:.2f}".format(after_passed_marks))
#print("final passed_marks newly passed", passed_percentage_after - passed_student)
print("final passed percentage increase:{:.2f} ".format(after_passed_marks - passed) )

