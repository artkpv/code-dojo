#!python3
for game in range(int(input().strip())):
    n = int(input().strip())
    b = input().strip()

    def ishappy():
        for i,e in enumerate(b):
            if (not (i > 0 and e == b[i-1]) and
                not (i < n-1 and e == b[i+1])):
                return False
        return True

    if ishappy():
        print("YES")
    else:
        colors = {c: sum(1 for e in b if e == c) for c in set(b)}
        hasempty = '_' in colors and colors['_'] > 0
        if not hasempty:
            print("NO")
        else:
            if any(colors[c] == 1 and c != '_' for c in colors):
                print("NO")
            else:
                print("YES")

