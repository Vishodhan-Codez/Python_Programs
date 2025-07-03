class V:
    def __init__(self, c):
        self.c = c
    def f(self):
        return self.c * 100

class B(V):
    def f(self):
        bf = super().f()
        ec = 0.1 * bf
        tf = bf + ec
        return f"Total fare: {tf} (Base fare: {bf} + Maintenance charge: {ec})\nSorry for the inconvience caused !! "
b = B(50)
print(b.f())