def aaa(name):
    def bbb():
        return "hello "
    return bbb()+name

print(aaa("kokot"))