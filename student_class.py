class Student:
    """defines instances of students"""
    def __init__(self, std_full_name, reg_no):
        self.std_full_name = std_full_name.upper()
        self.reg_no = reg_no.upper()
        self.tcur = 0
        self.tcue = 0
        self.cgpa = 0

    def calculate_cgpa(self, subject, score):
        self.tcur += subject.credit_unit
        
        if score >= 70:
            grade_point = 4.00
        elif score >= 65:
            grade_point = 3.50
        elif score >= 60:
            grade_point = 3.00
        elif score >= 55:
            grade_point = 2.50
        elif score >= 50:
            grade_point = 2.00
        else:
            grade_point = 0.00
        
        cue = float(grade_point * subject.credit_unit)
        self.tcue += cue
        self.cgpa = round(self.tcue/self.tcur, 2)
        



