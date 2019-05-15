#!python3


def bubble(arr):
    def sort():
        issorted = True
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                issorted = False
        return issorted
    while not sort():
        pass


if __name__ == '__main__':
    test1 = [3,2,1]
    test1copy = test1[:]
    bubble(test1copy)
    assert test1copy == sorted(test1), "%s should be sorted" % str(test1copy)
    print('tests pass')
