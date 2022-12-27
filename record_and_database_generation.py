from subject_class import *
from student_class import Student





student_1 = Student('Michael Bamikunle', 'u09ph1055')

student_1.calculate_cgpa(bio_111, 60)
student_1.calculate_cgpa(aum_321, 71)
student_1.calculate_cgpa(bdt_152, 40)
student_1.calculate_cgpa(hcp_361, 70)
print(student_1.cgpa)