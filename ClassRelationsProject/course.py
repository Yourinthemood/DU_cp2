class Course:
    def __init__(self, course_name, teacher, max_students):
        self.course_name = course_name
        self.teacher = teacher
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
    
    def remove_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                return True
        return False
    
    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def get_class_average(self):
        if len(self.students) == 0:
            return 0
        
        total = 0
        for student in self.students:
            total += student.get_overall_average()
        
        return total / len(self.students)
    
    def display_course_info(self):
        print(f"\nCourse: {self.course_name}")
        print(f"Teacher: {self.teacher}")
        print(f"Students: {len(self.students)}/{self.max_students}")
        print(f"Class Average: {self.get_class_average():.1f}%")
        
        if self.students:
            print("\nEnrolled Students:")
            for student in self.students:
                print(f"  {student.name} (ID: {student.student_id}) - {student.get_academic_status()}")
