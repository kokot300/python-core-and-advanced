class Student:
    def __init__(self,id,name,testscore):
        self.id=id
        self.name=name
        self.score=testscore
    def disp(self):
        print(self.id)
        print(self.name)
        print(self.score)