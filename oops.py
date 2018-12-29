
class Student:

    school = 'xyz'

    def __init__(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.sub = self.Subject

    def avg(self):          #instance method
        return (self.n1 + self.n2 + self.n3)/3


    @classmethod
    def getSchool(Cls):         #class metho
        return Cls.school

    @staticmethod
    def info():
        print("This is student class")

    class Subject:
        def __init__(self):
            self.ben='Bengali'
            self.math='English'
            self.his='History'



s1 = Student(34,68,85)
s2 = Student(54,65,55)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
sub1 = s1.sub()
sub2 = Student.Subject()
print(id(sub1))
print(id(sub2))