class Course:
    course_name:str
    active_status:bool

    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")

    def __str__(self):
        return self.course_name



class Batch:
    course:Course
    batch_code:str
    start_date:str
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code



class Student:
    student_name:str
    roll_no:str
    batch:Batch
    def add_batch(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.roll_no=kwargs.get("roll_no")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name




django=Course()
django.add_course(course_name="django",active_status=True)
testing=Course()
testing.add_course(course_name="testing",active_status=True)
bigdata=Course()
bigdata.add_course(course_name="bigdata",active_status=True)
mrnstk=Course()
mrnstk.add_course(course_name="mrnstk",active_status=True)
print(django)
print(testing)
print(mrnstk)
print(bigdata)


db1=Batch()
db1.add_batch(course=django,batch_code="db2k22",start_date="18-05-2022")
tc1=Batch()
tc1.add_batch(course=testing,batch_code="tc2k22",start_date="18-05-2022")
ms1=Batch()
ms1.add_batch(course=mrnstk,batch_code="ms2k22",start_date="18-05-2022")
bd1=Batch()
bd1.add_batch(course=bigdata,batch_code="bd2k22",start_date="18-05-2022")
print(db1)


vipin=Student()
vipin.add_batch(student_name="vipin",roll_no="123",batch="BCom")
print(vipin)
kochu=Student()
kochu.add_batch(student_name="kochu",roll_no="124",batch="MSc")
print(kochu)
allu=Student()
allu.add_batch(student_name="allu",roll_no="125",batch="BEd")
print(allu)

