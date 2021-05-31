class A:
    def __init__(self, data):
        self.data = data
    
    def plus(self, count):
        self.data + count

a = A(2)
b = a
b.plus(2)

print(b)
print(a)