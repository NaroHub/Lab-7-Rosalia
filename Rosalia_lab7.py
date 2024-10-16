name = (input ("Your name: "))
section = (input ("Your section: "))
prelim = float(input("Prelim Grade: "))
midterm = float(input("Midterm Grade: "))
final = float(input("Final Grade: "))

if prelim < 40.0 or prelim > 100.0:
    print("Grade must be between 40 and 100.")
elif midterm < 40.0 or midterm > 100.0:
    print("Grade must be between 40 and 100.")
elif final < 40.0 or final > 100.0:
    print("Grade must be between 40 and 100.")
    
fgrade = prelim+midterm+final
final_grade = round(fgrade/3)
if final_grade>=99.0 and final_grade<=100.0:
    grade = 1.00
elif final_grade>=96.0 and final_grade<=99.0:
    grade = 1.25
elif final_grade>=93.0 and final_grade<=96.0:
    grade = 1.50
elif final_grade>=90.0 and final_grade<=93.0:
    grade = 1.75
elif final_grade>=87.0 and final_grade<=90.0:
    grade = 2.00
elif final_grade>=84.0 and final_grade<=87.0:
    grade = 2.25
elif final_grade>=81.0 and final_grade<=84.0:
    grade = 2.50
elif final_grade>=78.0 and final_grade<=81.0:
    grade = 2.75
elif final_grade>=75.0 and final_grade<=78.0:
    grade = 3.00
else:
    grade = 5.00


print(f"Final Grade: {final_grade}")
print(f"This is your final GPA: {grade}")