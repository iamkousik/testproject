class PyCharm:
    def execute(self):
        print("Compiling")
        print("Ruing")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Ruing")

class Computer:
    def code(self, ide):
        ide.execute()

#ide = PyCharm()
ide = MyEditor()
c1 = Computer()
c1.code(ide)