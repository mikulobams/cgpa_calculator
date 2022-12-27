from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from subject_class import *

Base = declarative_base()



class Student(Base):
    __tablename__ = "student_records"

    regno = Column("regno" , String, primary_key = True)
    fullname = Column("fullname", String)
    tcur = Column('tcur', REAL)
    tcue = Column('tcue', REAL)
    cgpa = Column('cgpa', REAL)
    remarks = Column('remarks', String)


    
    """defines instances of students"""
    def __init__(self, std_full_name, reg_no):
        self.fullname = std_full_name.upper()
        self.regno = reg_no.upper()
        self.tcur = 0
        self.tcue = 0
        self.cgpa = 0
        self.remarks = ''
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
            self.remarks += subject.course_code
        
        cue = float(grade_point * subject.credit_unit)
        self.tcue += cue
        self.cgpa = round(self.tcue/self.tcur, 2)
    def __repr__(self):
        return f"""
            NAME:       {self.fullname}
            REG NO:     {self.regno}
            TCUR:       {self.tcur} 
            TCUE:       {self.tcue} 
            CGPA:       {self.cgpa}
            REMARKS:    {self.remarks})"""
    
    def test_print(self):
        return f"""
            NAME:       {self.fullname}
            REG NO:     {self.regno}
            TCUR:       {self.tcur} 
            TCUE:       {self.tcue} 
            CGPA:       {self.cgpa}
            REMARKS:    {self.remarks}\n\n\n"""
        

engine = create_engine("sqlite:///test.db", echo = True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

student_1 = Student('Michael Bamikunle', 'u09ph1055')

student_1.calculate_cgpa(bio_111, 60)
student_1.calculate_cgpa(aum_321, 71)
student_1.calculate_cgpa(bdt_152, 40)
student_1.calculate_cgpa(hcp_361, 70)
student_1.calculate_cgpa(bio_112, 70)

# session.add(student_1)
# session.commit()

with open('test.txt', 'a') as f:
    f.write(student_1.test_print())
