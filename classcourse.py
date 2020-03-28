class Course:
    def __init__(self,naming,rating): #name i rating are parametarized constructor
        self.name=naming
        self.rank=rating

    def averadge(self): #instance method
        num_ratings=len(self.rank)
        sum_ratings=sum(self.rank)
        averr=sum_ratings/num_ratings
        print("averige ratings are: ",averr)

c1=Course("java",[1,2,3,4,5])
print(c1.name)
print(c1.rank)
c1.averadge() #invoking instance method

print("\n")

c2=Course("c++",[1,2,3,4,5,6,7,8,9,10])
print(c2.name)
print(c2.rank)
c2.averadge()