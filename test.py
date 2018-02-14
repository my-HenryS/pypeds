
class A(object):

    def func(self):
        print(type(self))

class B(A):
    pass


a = B()
a.func()