class A:
    def run(self):
        print("AAAAA")
class B(A):
    def disply(self):
        print("BBBB")
class C(B):
    def show(self):
        print("CCCCC")

class test:
    C.C()
    C.run()
    C.disply()