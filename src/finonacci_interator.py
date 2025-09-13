# %%
class Fibanocci:
    def __init__(self):
        self.n1, self.n2 = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.n1
        self.n1, self.n2 = self.n2, self.n1 + self.n2
        return current

fibanocci = Fibanocci()
myiter = iter(fibanocci)

for _ in range(10):
    print(next(myiter), end=' ')
# %%
