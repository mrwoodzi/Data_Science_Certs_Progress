class Dummy:
    def func(x):
        """ An instance method that returns `x` unchanged.
            This is a bad version of this instance method!"""
        return x

inst = Dummy()
out = inst.func()
print(inst.func())
print(inst is out)