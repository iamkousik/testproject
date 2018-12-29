class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C():

    def feature5(self):
        print("Feature 5 working")

    def feature6(self):
        print("Feature 6 working")

class D(B, C):

    def feature7(self):
        print("Feature 7 working")

    def feature8(self):
        print("Feature 8 working")
c = C()
d = D()
c.feature5()
d.feature2()
d.feature6()


