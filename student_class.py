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

student_1 = Student('Abubakar Ahmad abubakar', 'cchstz/pt/002/21')
student_1.calculate_cgpa(ctz_101, 68)
student_1.calculate_cgpa(eng_101, 28)
student_1.calculate_cgpa(ict_101, 51)
student_1.calculate_cgpa(ptp_111, 50)
student_1.calculate_cgpa(phy_111, 60)
student_1.calculate_cgpa(chm_111, 35)
student_1.calculate_cgpa(bio_111, 27)
student_1.calculate_cgpa(etp_101, 50)
student_1.calculate_cgpa(bdt_151, 79)
student_1.calculate_cgpa(mth_111, 60)
student_1.calculate_cgpa(bio_112, 26)
student_1.calculate_cgpa(chm_112, 51)
student_1.calculate_cgpa(phy_112, 39)
student_1.calculate_cgpa(mth_112, 50)
student_1.calculate_cgpa(eng_102, 34)
student_1.calculate_cgpa(bdt_152, 50)
student_1.calculate_cgpa(mcb_112, 39)
student_1.calculate_cgpa(aum_122, 42)
# session.add(student_1)
# session.commit()

with open('test.txt', 'a') as f:
    f.write(student_1.test_print())


student_2 = Student('Abubakar Usman', 'cchstz/pt/003/21')
student_2.calculate_cgpa(ctz_101, 65)
student_2.calculate_cgpa(eng_101, 55)
student_2.calculate_cgpa(ict_101, 37)
student_2.calculate_cgpa(ptp_111, 52)
student_2.calculate_cgpa(phy_111, 46)
student_2.calculate_cgpa(chm_111, 35)
student_2.calculate_cgpa(bio_111, 27)
student_2.calculate_cgpa(etp_101, 50)
student_2.calculate_cgpa(bdt_151, 61)
student_2.calculate_cgpa(mth_111, 43)
student_2.calculate_cgpa(bio_112, 30)
student_2.calculate_cgpa(chm_112, 51)
student_2.calculate_cgpa(phy_112, 20)
student_2.calculate_cgpa(mth_112, 50)
student_2.calculate_cgpa(eng_102, 32)
student_2.calculate_cgpa(bdt_152, 30)
student_2.calculate_cgpa(mcb_112, 38)
student_2.calculate_cgpa(aum_122, 50)
with open('test.txt', 'a') as f:
    f.write(student_2.test_print())

student_3 = Student('Bala Patience Bulus', 'cchstz/pt/016/21')
student_3.calculate_cgpa(ctz_101, 64)
student_3.calculate_cgpa(eng_101, 59)
student_3.calculate_cgpa(ict_101, 40)
student_3.calculate_cgpa(ptp_111, 55)
student_3.calculate_cgpa(phy_111, 60)
student_3.calculate_cgpa(chm_111, 40)
student_3.calculate_cgpa(bio_111, 50)
student_3.calculate_cgpa(etp_101, 21)
student_3.calculate_cgpa(bdt_151, 56)
student_3.calculate_cgpa(mth_111, 42)
student_3.calculate_cgpa(bio_112, 50)
student_3.calculate_cgpa(chm_112, 53)
student_3.calculate_cgpa(phy_112, 30)
student_3.calculate_cgpa(mth_112, 14)
student_3.calculate_cgpa(eng_102, 34)
student_3.calculate_cgpa(bdt_152, 50)
student_3.calculate_cgpa(mcb_112, 22)
student_3.calculate_cgpa(aum_122, 50)
with open('test.txt', 'a') as f:
    f.write(student_3.test_print())

student_4 = Student('Fatima Aliyu', 'cchstz/pt/033/21')
student_4.calculate_cgpa(ctz_101, 80)
student_4.calculate_cgpa(eng_101, 54)
student_4.calculate_cgpa(ict_101, 51)
student_4.calculate_cgpa(ptp_111, 58)
student_4.calculate_cgpa(phy_111, 52)
student_4.calculate_cgpa(chm_111, 56)
student_4.calculate_cgpa(bio_111, 50)
student_4.calculate_cgpa(etp_101, 60)
student_4.calculate_cgpa(bdt_151, 61)
student_4.calculate_cgpa(mth_111, 60)
student_4.calculate_cgpa(bio_112, 25)
student_4.calculate_cgpa(chm_112, 40)
student_4.calculate_cgpa(phy_112, 0)
student_4.calculate_cgpa(mth_112, 50)
student_4.calculate_cgpa(eng_102, 39)
student_4.calculate_cgpa(bdt_152, 43)
student_4.calculate_cgpa(mcb_112, 25)
student_4.calculate_cgpa(aum_122, 51)
with open('test.txt', 'a') as f:
    f.write(student_4.test_print())

student_5 = Student('Ibrahim Yusuf', 'cchstz/pt/046/21')
student_5.calculate_cgpa(ctz_101, 60)
student_5.calculate_cgpa(eng_101, 60)
student_5.calculate_cgpa(ict_101, 54)
student_5.calculate_cgpa(ptp_111, 52)
student_5.calculate_cgpa(phy_111, 60)
student_5.calculate_cgpa(chm_111, 50)
student_5.calculate_cgpa(bio_111, 25)
student_5.calculate_cgpa(etp_101, 50)
student_5.calculate_cgpa(bdt_151, 50)
student_5.calculate_cgpa(mth_111, 53)
student_5.calculate_cgpa(bio_112, 22)
student_5.calculate_cgpa(chm_112, 50)
student_5.calculate_cgpa(phy_112, 10)
student_5.calculate_cgpa(mth_112, 50)
student_5.calculate_cgpa(eng_102, 50)
student_5.calculate_cgpa(bdt_152, 43)
student_5.calculate_cgpa(mcb_112, 24)
student_5.calculate_cgpa(aum_122, 23)
with open('test.txt', 'a') as f:
    f.write(student_5.test_print())

student_6 = Student('jacob luka', 'cchstz/pt/049/21')
student_6.calculate_cgpa(ctz_101, 56)
student_6.calculate_cgpa(eng_101, 60)
student_6.calculate_cgpa(ict_101, 50)
student_6.calculate_cgpa(ptp_111, 53)
student_6.calculate_cgpa(phy_111, 62)
student_6.calculate_cgpa(chm_111, 50)
student_6.calculate_cgpa(bio_111, 27)
student_6.calculate_cgpa(etp_101, 50)
student_6.calculate_cgpa(bdt_151, 61)
student_6.calculate_cgpa(mth_111, 35)
student_6.calculate_cgpa(bio_112, 60)
student_6.calculate_cgpa(chm_112, 50)
student_6.calculate_cgpa(phy_112, 36)
student_6.calculate_cgpa(mth_112, 33)
student_6.calculate_cgpa(eng_102, 34)
student_6.calculate_cgpa(bdt_152, 43)
student_6.calculate_cgpa(mcb_112, 32)
student_6.calculate_cgpa(aum_122, 40)
with open('test.txt', 'a') as f:
    f.write(student_6.test_print())

student_7 = Student('Joseph Meekness', 'cchstz/pt/056/21')
student_7.calculate_cgpa(ctz_101, 70)
student_7.calculate_cgpa(eng_101, 40)
student_7.calculate_cgpa(ict_101, 38)
student_7.calculate_cgpa(ptp_111, 55)
student_7.calculate_cgpa(phy_111, 50)
student_7.calculate_cgpa(chm_111, 46)
student_7.calculate_cgpa(bio_111, 36)
student_7.calculate_cgpa(etp_101, 56)
student_7.calculate_cgpa(bdt_151, 82)
student_7.calculate_cgpa(mth_111, 50)
student_7.calculate_cgpa(bio_112, 39)
student_7.calculate_cgpa(chm_112, 38)
student_7.calculate_cgpa(phy_112, 8)
student_7.calculate_cgpa(mth_112, 50)
student_7.calculate_cgpa(eng_102, 54)
student_7.calculate_cgpa(bdt_152, 41)
student_7.calculate_cgpa(mcb_112, 34)
student_7.calculate_cgpa(aum_122, 50)
with open('test.txt', 'a') as f:
    f.write(student_7.test_print())

student_8 = Student('Mathias Faith', 'cchstz/pt/064/21')
student_8.calculate_cgpa(ctz_101, 58)
student_8.calculate_cgpa(eng_101, 33)
student_8.calculate_cgpa(ict_101, 31)
student_8.calculate_cgpa(ptp_111, 53)
student_8.calculate_cgpa(phy_111, 60)
student_8.calculate_cgpa(chm_111, 56)
student_8.calculate_cgpa(bio_111, 29)
student_8.calculate_cgpa(etp_101, 50)
student_8.calculate_cgpa(bdt_151, 52)
student_8.calculate_cgpa(mth_111, 63)
student_8.calculate_cgpa(bio_112, 50)
student_8.calculate_cgpa(chm_112, 51)
student_8.calculate_cgpa(phy_112, 33)
student_8.calculate_cgpa(mth_112, 52)
student_8.calculate_cgpa(eng_102, 34)
student_8.calculate_cgpa(bdt_152, 42)
student_8.calculate_cgpa(mcb_112, 38)
student_8.calculate_cgpa(aum_122, 54)
with open('test.txt', 'a') as f:
    f.write(student_8.test_print())


student_9 = Student('Rejoice Josiah', 'cchstz/pt/078/21')
student_9.calculate_cgpa(ctz_101, 67)
student_9.calculate_cgpa(eng_101, 41)
student_9.calculate_cgpa(ict_101, 44)
student_9.calculate_cgpa(ptp_111, 60)
student_9.calculate_cgpa(phy_111, 67)
student_9.calculate_cgpa(chm_111, 66)
student_9.calculate_cgpa(bio_111, 50)
student_9.calculate_cgpa(etp_101, 58)
student_9.calculate_cgpa(bdt_151, 85)
student_9.calculate_cgpa(mth_111, 54)
student_9.calculate_cgpa(bio_112, 38)
student_9.calculate_cgpa(chm_112, 53)
student_9.calculate_cgpa(phy_112, 40)
student_9.calculate_cgpa(mth_112, 65)
student_9.calculate_cgpa(eng_102, 30)
student_9.calculate_cgpa(bdt_152, 50)
student_9.calculate_cgpa(mcb_112, 51)
student_9.calculate_cgpa(aum_122, 10)
with open('test.txt', 'a') as f:
    f.write(student_9.test_print())


student_10 = Student('Shobande Oladayo', 'cchstz/pt/082/21')
student_10.calculate_cgpa(ctz_101, 61)
student_10.calculate_cgpa(eng_101, 28)
student_10.calculate_cgpa(ict_101, 72)
student_10.calculate_cgpa(ptp_111, 60)
student_10.calculate_cgpa(phy_111, 51)
student_10.calculate_cgpa(chm_111, 50)
student_10.calculate_cgpa(bio_111, 42)
student_10.calculate_cgpa(etp_101, 59)
student_10.calculate_cgpa(bdt_151, 30)
student_10.calculate_cgpa(mth_111, 50)
student_10.calculate_cgpa(bio_112, 38)
student_10.calculate_cgpa(chm_112, 50)
student_10.calculate_cgpa(phy_112, 38)
student_10.calculate_cgpa(mth_112, 50)
student_10.calculate_cgpa(eng_102, 30)
student_10.calculate_cgpa(bdt_152, 51)
student_10.calculate_cgpa(mcb_112, 44)
student_10.calculate_cgpa(aum_122, 44)
with open('test.txt', 'a') as f:
    f.write(student_10.test_print())



student_11 = Student('Thomas Juliet', 'cchstz/pt/087/21')
student_11.calculate_cgpa(ctz_101, 50)
student_11.calculate_cgpa(eng_101, 20)
student_11.calculate_cgpa(ict_101, 50)
student_11.calculate_cgpa(ptp_111, 50)
student_11.calculate_cgpa(phy_111, 73)
student_11.calculate_cgpa(chm_111, 50)
student_11.calculate_cgpa(bio_111, 29)
student_11.calculate_cgpa(etp_101, 50)
student_11.calculate_cgpa(bdt_151, 65)
student_11.calculate_cgpa(mth_111, 41)
student_11.calculate_cgpa(bio_112, 37)
student_11.calculate_cgpa(chm_112, 32)
student_11.calculate_cgpa(phy_112, 45)
student_11.calculate_cgpa(mth_112, 50)
student_11.calculate_cgpa(eng_102, 30)
student_11.calculate_cgpa(bdt_152, 56)
student_11.calculate_cgpa(mcb_112, 41)
student_11.calculate_cgpa(aum_122, 37)
with open('test.txt', 'a') as f:
    f.write(student_11.test_print())


student_12 = Student('Yusuf Andrawus', 'cchstz/pt/102/21')
student_12.calculate_cgpa(ctz_101, 77)
student_12.calculate_cgpa(eng_101, 43)
student_12.calculate_cgpa(ict_101, 43)
student_12.calculate_cgpa(ptp_111, 52)
student_12.calculate_cgpa(phy_111, 50)
student_12.calculate_cgpa(chm_111, 50)
student_12.calculate_cgpa(bio_111, 40)
student_12.calculate_cgpa(etp_101, 51)
student_12.calculate_cgpa(bdt_151, 67)
student_12.calculate_cgpa(mth_111, 52)
student_12.calculate_cgpa(bio_112, 32)
student_12.calculate_cgpa(chm_112, 50)
student_12.calculate_cgpa(phy_112, 40)
student_12.calculate_cgpa(mth_112, 50)
student_12.calculate_cgpa(eng_102, 33)
student_12.calculate_cgpa(bdt_152, 35)
student_12.calculate_cgpa(mcb_112, 29)
student_12.calculate_cgpa(aum_122, 50)
with open('test.txt', 'a') as f:
    f.write(student_12.test_print())


student_13 = Student("Zahara'u Nasiru", 'cchstz/pt/104/21')
student_13.calculate_cgpa(ctz_101, 58)
student_13.calculate_cgpa(eng_101, 50)
student_13.calculate_cgpa(ict_101, 55)
student_13.calculate_cgpa(ptp_111, 53)
student_13.calculate_cgpa(phy_111, 50)
student_13.calculate_cgpa(chm_111, 50)
student_13.calculate_cgpa(bio_111, 24)
student_13.calculate_cgpa(etp_101, 50)
student_13.calculate_cgpa(bdt_151, 30)
student_13.calculate_cgpa(mth_111, 60)
student_13.calculate_cgpa(bio_112, 29)
student_13.calculate_cgpa(chm_112, 39)
student_13.calculate_cgpa(phy_112, 40)
student_13.calculate_cgpa(mth_112, 50)
student_13.calculate_cgpa(eng_102, 39)
student_13.calculate_cgpa(bdt_152, 32)
student_13.calculate_cgpa(mcb_112, 26)
student_13.calculate_cgpa(aum_122, 36)
with open('test.txt', 'a') as f:
    f.write(student_13.test_print())



student_14 = Student('Zainab Dauda', 'cchstz/pt/105/21')
student_14.calculate_cgpa(ctz_101, 64)
student_14.calculate_cgpa(eng_101, 18)
student_14.calculate_cgpa(ict_101, 40)
student_14.calculate_cgpa(ptp_111, 50)
student_14.calculate_cgpa(phy_111, 55)
student_14.calculate_cgpa(chm_111, 41)
student_14.calculate_cgpa(bio_111, 50)
student_14.calculate_cgpa(etp_101, 50)
student_14.calculate_cgpa(bdt_151, 62)
student_14.calculate_cgpa(mth_111, 62)
student_14.calculate_cgpa(bio_112, 60)
student_14.calculate_cgpa(chm_112, 55)
student_14.calculate_cgpa(phy_112, 47)
student_14.calculate_cgpa(mth_112, 0)
student_14.calculate_cgpa(eng_102, 37)
student_14.calculate_cgpa(bdt_152, 33)
student_14.calculate_cgpa(mcb_112, 34)
student_14.calculate_cgpa(aum_122, 40)
with open('test.txt', 'a') as f:
    f.write(student_14.test_print())

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