from abc import abstractmethod

class TouchScreenLaptop:
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass

class hp(TouchScreenLaptop):
    def scroll(self):
        print("hp scroll")

class dell(TouchScreenLaptop):
    def scroll(self):
        print("dell scroll")

class hplaptop(hp):
    def click(self):
        print("hp laptop click")
    def scroll(self):
        print("hp laptop scroll")

class delllaptop(dell):
    def click(self):
        print("dell laptop click")
    def scroll(self):
        print("dell laptop scroll")

a=hp()
b=dell()
aa=hplaptop()
bb=delllaptop()

a.scroll()
b.scroll()
aa.scroll()
bb.scroll()
aa.click()
bb.click()
