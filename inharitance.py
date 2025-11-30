class parent:
    def fun1(self):
        print("Hello")

class child(parent):
    def fun2(self):
        print("welcome")

obj = child()
obj.fun1()
obj.fun2()