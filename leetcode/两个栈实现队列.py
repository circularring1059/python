class CQueue():
    def __init__(self):
        self.A = []
        self.B = []

    def append(self, val):
        self.A.append(val)

    def delete(self):
        if self.B: return self.B.pop()

        if not self.A: return -1

        while self.A:
            self.B.append((self.A.pop()))
        return self.B.pop()

