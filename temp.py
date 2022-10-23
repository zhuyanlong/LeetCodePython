class Temp:
    def __init__(self):
        self.length=0
    def getlen(self):
        return self.length
    def addlen(self):
        self.length+=1

def main():
    t=Temp()
    t.addlen()
    print(t.getlen())

main()