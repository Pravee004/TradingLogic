
class myclass:
    h=10
    fruits=["mango","orange"]
    def __init__(self,name,age,address,contact):
        self.a=name
        self.b=age
        self.c=address
        self.d=contact
        print("name:",name)
        print("age:",age)
        print("address:",address)
        print("contact:",contact)
    def data2(self):
        print("user data")
        print("name:",self.a)
    def __del__(self):
      self.fruits.clear()
      print("destructor")
      print("age:",self.b)
    def data3(self):
      print("yes")
obj=myclass("ram",13,"ffgg",8667537)
obj.data2()
obj.data3()
jj=obj.fruits
jj.insert(0,"graphs")
jj.append("apple")
obj.a="tree"
print("the value h",obj.a)
print("fruits",jj)
obj.__del__()
