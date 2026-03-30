class Gradebook:
    def __init__(self):
        self.courses = []
    
    def add_course(self, course):
        self.courses.append(course)
    
    def find_course(self, course_name):
        for course in self.courses:
            if course.course_name.lower() == course_name.lower():
                return course
        return None
    
    def display_all_courses(self):
        if not self.courses:
            print("\nNo courses available.")
            return
        
        print("\n=== ALL COURSES ===")
        for course in self.courses:
            print(f"\n{course.course_name} (Teacher: {course.teacher})")
            print(f"Students: {len(course.students)}/{course.max_students}")
            print(f"Class Average: {course.get_class_average():.1f}%")
    
    def get_grade_statistics(self, course_name):
        course = self.find_course(course_name)
        
        if not course:
            print("\nCourse not found.")
            return
        
        if len(course.students) == 0:
            print("\nNo students in this course.")
            return
        
        averages = []
        for student in course.students:
            averages.append(student.get_overall_average())
        
        highest = max(averages)
        lowest = min(averages)
        average = sum(averages) / len(averages)
        
        print(f"\n=== Grade Statistics for {course.course_name} ===")
        print(f"Highest Grade: {highest:.1f}%")
        print(f"Lowest Grade: {lowest:.1f}%")
        print(f"Class Average: {average:.1f}%")
        
        status_count = {"Excellent": 0, "Good": 0, "Satisfactory": 0, 
                        "Needs Improvement": 0, "Failing": 0}
        
        for student in course.students:
            status = student.get_academic_status()
            status_count[status] += 1
        
        print("\nGrade Distribution:")
        for status, count in status_count.items():
            if count > 0:
                print(f"  {status}: {count} student(s)")
