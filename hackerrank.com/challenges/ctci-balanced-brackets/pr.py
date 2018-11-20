#!python3

n = int(input())
opens = "{[("
closes = "}])"
for query in range(n):
    s = input().strip()
    st = []
    is_good = True
    for i in range(len(s)):
        if s[i] in opens:
            st.append(s[i])
        else:
            left = opens[closes.index(s[i])]
            if len(st) == 0 or st[-1] != left:
                is_good = False
                break
            else:
                st.pop()
    if len(st) != 0:
        is_good = False
    print("YES" if is_good else "NO")



