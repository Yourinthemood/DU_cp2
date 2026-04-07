class Student:
    def __init__(self, name, student_id, grade_level):
        self.name = name
        self.student_id = student_id
        self.grade_level = grade_level
        self.grades = {}
    
    def add_grade(self, assignment_name, score, max_score):
        if assignment_name not in self.grades:
            self.grades[assignment_name] = []
        
        percentage = (score / max_score) * 100
        self.grades[assignment_name].append({
            'score': score,
            'max_score': max_score,
            'percentage': percentage
        })
    
    def get_average_for_assignment(self, assignment_name):
        if assignment_name not in self.grades or len(self.grades[assignment_name]) == 0:
            return 0
        
        total = 0
        for grade in self.grades[assignment_name]:
            total += grade['percentage']
        
        return total / len(self.grades[assignment_name])
    
    def get_overall_average(self):
        if len(self.grades) == 0:
            return 0
        
        all_percentages = []
        for assignment_name in self.grades:
            for grade in self.grades[assignment_name]:
                all_percentages.append(grade['percentage'])
        
        if len(all_percentages) == 0:
            return 0
        
        total = sum(all_percentages)
        return total / len(all_percentages)
    
    def get_academic_status(self):
        average = self.get_overall_average()
        
        if average >= 90:
            return "Excellent"
        elif average >= 80:
            return "Good"
        elif average >= 70:
            return "Satisfactory"
        elif average >= 60:
            return "Needs Improvement"
        else:
            return "Failing"
    
    def display_info(self):
        print(f"\nStudent: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grade Level: {self.grade_level}")
        print(f"Overall Average: {self.get_overall_average():.1f}%")
        print(f"Academic Status: {self.get_academic_status()}")
        
        if self.grades:
            print("\nAssignment Averages:")
            for assignment_name in self.grades:
                avg = self.get_average_for_assignment(assignment_name)
                print(f"  {assignment_name}: {avg:.1f}%")
