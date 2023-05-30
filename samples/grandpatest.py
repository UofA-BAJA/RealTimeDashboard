class A:
    def __init__(self) -> None:
        self.a = 1

class B(A):

    def __init__(self) -> None:
        self.a = 2

class C(B):

    def __init__(self) -> None:
        A.__init__(self)

test = C()

print(test.a)
        
