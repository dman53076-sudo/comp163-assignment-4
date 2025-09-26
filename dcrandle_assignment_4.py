#Student starting stats
student_name = "Daniel Crandle"
current_gpa = 3.5
study_hours = 12
social_points = 75
stress_level = 40
#Welcome message and stats display
print(f"Welcome, {student_name}!")
print(f"Your current GPA is: {current_gpa}")
print(f"Your study hours this week: {study_hours}")
print(f"Your social points: {social_points}")
print(f"Your stress level: {stress_level}")
#Course Load Options
print("\nChoose your course load for the semester:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Enter A, B, or C: ")
#if-elif-else structure to handle course load choice
if choice == "A":
    course_load = "Light (12 credits)"
    study_hours += 2
    social_points += 5
    stress_level += 5
elif choice == "B":
    course_load = "Standard (15 credits)"
    study_hours += 4
    social_points += 10
    stress_level += 10
elif choice == "C":
    course_load = "Heavy (18 credits)"
    study_hours += 6
    social_points += 15
    stress_level += 15
else:
    course_load = "Invalid" 