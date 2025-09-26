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
# Decision 2: Choose a study focus
study_options = ["Programming", "Math", "English", "History"]
print("\nChoose a subject to focus on this semester:")
print("Options: Programming, Math, English, History")

subject_choice = input("Enter your chosen subject: ")

# Validate user choice using membership operator
if subject_choice in study_options:
    print(f"You chose to focus on {subject_choice}.")

    # Use logical operators to determine effects
    if subject_choice in ["Programming", "Math"] and stress_level < 50:
        current_gpa += 0.2
        social_points -= 5
        print("Focusing on a technical subject with low stress helped your GPA, but reduced social time.")
    elif subject_choice in ["English", "History"] or stress_level > 60:
        current_gpa += 0.1
        social_points += 5
        print("Focusing on a humanities subject or being highly stressed gave you a balanced outcome.")
    else:
        print("Your choice had a neutral effect this time.")
elif subject_choice not in study_options:
    print("That subject isn't available this semester.")
    current_gpa -= 0.1
    stress_level += 5
    print("Choosing an unapproved subject caused confusion and stress.")