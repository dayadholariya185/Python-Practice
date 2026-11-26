class bagfactory:
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size
    def  detail(self):
        print("your detail are:")
        print(self.name)
        print(self.color)
        print(self.size)
class my(bagfactory):
    def __init__(self, name, color, size,zip):
        super().__init__(name, color, size)
        self.zip=zip
    def detail(self):
        print(self.zip)
        return super().detail()
        
bag1=bagfactory("zara","black",24,)
bag2=my("xyw","fuf",67,5)

bag1.detail()
bag2.detail()