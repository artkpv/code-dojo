#!python


class MyStack(object):
    def __init__(self):
        self.size = 10
        self.arr = [None] * self.size
        self.count = 0

    def push(self, e):
        if self.count == self.size:
            self.resize(self.size * 2)
        self.arr[self.count] = e
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise 'empty'
        e = self.arr[self.count - 1]
        self.count -= 1
        if self.count <= self.size // 4:
            self.resize(self.size // 2)
        return e

    def resize(self, newsize):
        self.arr = (self.arr[:min(newsize, self.size)] + [None] *
                    (newsize - min(newsize, self.size)))
        self.size = newsize


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    assert s.count == 1
    assert s.pop() == 1
    assert s.count == 0
    for i in range(20):
        s.push(i + 1)
    assert s.count == 20
    print('tested')
