# Take input from user
marks = int(input("Enter your marks (0-100): "))

# Check and display grade
if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks < 90:
    print("Grade: B")
elif 60 <= marks < 75:
    print("Grade: C")
elif 40 <= marks < 60:
    print("Grade: D")
elif 0 <= marks < 40:
    print("Grade: Fail")
else:
    print("Invalid marks. Please enter a value between 0 and 100.")
