class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.a++self.b
        return self.a
    def __iter__(self):
        return self
iterator=Fibs()
l=[]
for i in iterator:
    l.append(i)
    if i>100:
        print(l)
        print(i)
        break
