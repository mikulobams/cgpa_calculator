#REcords for 2021 entrants
from sqlalchemy import create_engine, Column, String, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from subject_class import *

Base = declarative_base()

class Student(Base):
    __tablename__ = "student_records"

    regno = Column("regno" , String, primary_key = True, nullable=False, unique=True)
    fullname = Column("fullname", String, nullable=False)
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
            if subject.course_code in self.remarks:
                update = self.remarks.replace(subject.course_code, '')
                self.remarks = update
        elif score >= 65:
            grade_point = 3.50
            if subject.course_code in self.remarks:
                update = self.remarks.replace(subject.course_code, '')
                self.remarks = update
        elif score >= 60:
            grade_point = 3.00
            if subject.course_code in self.remarks:
                update = self.remarks.replace(subject.course_code, '')
                self.remarks = update
        elif score >= 55:
            grade_point = 2.50
            if subject.course_code in self.remarks:
                update = self.remarks.replace(subject.course_code, '')
                self.remarks = update
        elif score >= 50:
            grade_point = 2.00
            if subject.course_code in self.remarks:
                update = self.remarks.replace(subject.course_code, '')
                self.remarks = update
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
            REMARKS:    {self.remarks}"""
    
    def test_print(self):
        return f"""
            NAME:       {self.fullname}
            REG NO:     {self.regno}
            TCUR:       {self.tcur} 
            TCUE:       {self.tcue} 
            CGPA:       {self.cgpa}
            REMARKS:    {self.remarks}\n\n"""
        

engine = create_engine("sqlite:///test.db", echo = True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

test = session.query(Student).all()
print(test[14])

#query and then update student
# update_record = session.query(Student).filter(Student.regno == 'cchstz/pt/104/21'.upper()).first()
# update_record.calculate_cgpa(hcp_361, 90)
# session.commit()


#DELETING DATA
# query = session.query(Student)
# query = query.filter(Student.regno == "cchstz/pt/xxx/xx")
# dcc_cookie = query.first()
# session.delete(dcc_cookie)
# session.commit()
# dcc_cookie = query.first()
# print(dcc_cookie)