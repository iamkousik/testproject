
class Student:

    def getInfo(self, name,  roll):
        self.name = name
        self.roll = roll

class Exam(Student):

    def getMarks(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

class Sport:

    def getScore(self, score):
        self.score = score

class Result(Exam, Sport):

    def result(self):

        total = self.m1 + self.m2 + self.score
        print("Roll No. : ", self.roll)
        print("Name : ", self.name)
        print("Marks : ", self.m1,"and", self.m2)
        print("Score : ", self.score, "pt")
        print("Total : ", total)


s1 = Result()
s1.getInfo("asd", 20)
s1.getMarks(56, 56)
s1.getScore(86.36)
s1.result()

