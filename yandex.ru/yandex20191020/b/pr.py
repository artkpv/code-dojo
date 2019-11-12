#!python3

def run(code, params):
    s = []
    def calc(a, b, op):
        assert isinstance(a, int)
        assert isinstance(b, int)
        assert isinstance(op, str)
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a // b
        if op == '<':
            return a < b
        if op == '=':
            return a == b

    def call():
        # print('call', s)
        op = s.pop()
        issuccess = False
        if isinstance(op, int) or isinstance(op, bool):
            s.append(op)
            issuccess = True
        elif op in '+-*/<=':
            if call():
                b = s.pop()
                if call():
                    a = s.pop()
                    if isinstance(a, int) and isinstance(b, int):
                        s.append(calc(a, b, op))
                        issuccess = True
                    else:
                        s.append(b)
                        s.append(a)
                else:
                    s.append(b)
        elif op == '?':
            if call():
                c = s.pop()
                if call():
                    b = s.pop()
                    if call():
                        a = s.pop()
                        assert isinstance(a, bool)
                        s.append(b if a else c)
                        issuccess = True
                    else:
                        s.append(b)
                        s.append(c)
                else:
                    s.append(c)
        else:
            if params:
                i = ord(op) - ord('a')
                assert i < len(params)
                s.append(params[i])
                issuccess = True
        if not issuccess:
            s.append(op)

        return issuccess

    for e in code:
        if isinstance(e, str) and e[-1].isdigit():
            s.append(int(e))
        else:
            s.append(e)
        call()

    return s


K = int(input().strip())
code = input().strip().split(' ')
# Run till arguments.
code = run(code, [])
N = int(input().strip())
for _ in range(N):
    params = [int(i) for i in input().strip().split(' ')]
    # print('test', code, params)
    out = run(code, params)
    assert out
    assert len(out) == 1
    print(out[0])

