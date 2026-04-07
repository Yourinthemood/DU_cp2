from student import Student
from course import Course
from gradebook import Gradebook

def main():
    gradebook = Gradebook()
    
    while True:
        print("\n=== GRADEBOOK SYSTEM ===")
        print("1. Add Course")
        print("2. Add Student to Course")
        print("3. Add Grade for Student")
        print("4. View Course Details")
        print("5. View All Courses")
        print("6. View Grade Statistics")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            course_name = input("Enter course name: ")
            teacher = input("Enter teacher name: ")
            
            try:
                max_students = int(input("Enter maximum students: "))
                course = Course(course_name, teacher, max_students)
                gradebook.add_course(course)
                print(f"\nCourse '{course_name}' added successfully!")
            except ValueError:
                print("\nInvalid input. Please enter a number for max students.")
        
        elif choice == "2":
            course_name = input("Enter course name: ")
            course = gradebook.find_course(course_name)
            
            if not course:
                print("\nCourse not found.")
                continue
            
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            grade_level = input("Enter grade level (9-12): ")
            
            student = Student(name, student_id, grade_level)
            
            if course.add_student(student):
                print(f"\n{name} added to {course_name}!")
            else:
                print(f"\nCourse is full. Cannot add {name}.")
        
        elif choice == "3":
            course_name = input("Enter course name: ")
            course = gradebook.find_course(course_name)
            
            if not course:
                print("\nCourse not found.")
                continue
            
            student_id = input("Enter student ID: ")
            student = course.get_student(student_id)
            
            if not student:
                print("\nStudent not found in this course.")
                continue
            
            assignment_name = input("Enter assignment name: ")
            
            try:
                score = float(input("Enter score earned: "))
                max_score = float(input("Enter maximum possible score: "))
                
                if score > max_score:
                    print("\nScore cannot exceed maximum score.")
                    continue
                
                student.add_grade(assignment_name, score, max_score)
                print(f"\nGrade added for {student.name}!")
                
            except ValueError:
                print("\nInvalid input. Please enter numbers for scores.")
        
        elif choice == "4":
            course_name = input("Enter course name: ")
            course = gradebook.find_course(course_name)
            
            if course:
                course.display_course_info()
            else:
                print("\nCourse not found.")
        
        elif choice == "5":
            gradebook.display_all_courses()
        
        elif choice == "6":
            course_name = input("Enter course name: ")
            gradebook.get_grade_statistics(course_name)
        
        elif choice == "7":
            print("\nThank you for using the Gradebook System!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

main()
