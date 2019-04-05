"""
Knuth-Morris-Pratt algorithm for substring search
"""

def charat(c, chars):
    return chars.index(c)

def construct_dfa(pattern, chars):
    """
    Constructs DFA by running the partially constructed
    DFA on pattern itself till current char. Thus we
    get the largest prefix that matches largest suffix ending
    on that char.
    Example. Pattern: ABABACA
    ABABAC  at state 4 (ABABA)
      ABA   largest prefix, hence from 4 the same
            states as from 2 but with A to 5.
    """
    X = 0  # state of partially constructed DFA
    dfa = [[0] * len(pattern) for _ in range(len(chars))]
    dfa[charat(pattern[0], chars)][0] = 1
    for i in range(1, len(pattern)):
        e = charat(pattern[i], chars)
        # copy from previous state:
        for j in range(len(chars)):
            dfa[j][i] = dfa[j][X]
        # next success state
        dfa[e][i] = i + 1
        # run the partial dfa
        X = dfa[e][X]
    return dfa

def kmp(text, pattern):
    chars = list(sorted(set(pattern)))
    # First construct DFA from pattern
    dfa = construct_dfa(pattern, chars)
    state = 0
    # Run this DFA on text in ~N time
    # If state reaches M then we found
    # else if end of text: not found
    for i,e in enumerate(text):
        if e in chars:
            state = dfa[charat(e, chars)][state]
        else:
            state = 0
        if state == len(pattern):
            return i - len(pattern) + 1
    else:
        return -1  # not found


if __name__ == '__main__':
    assert(kmp('ABAABBA', 'BB') == 4)
    assert(kmp('ABAABBA', 'C') == -1)
    assert(kmp('ABAABABACA', 'ABABACA') == 3)
    assert(kmp('ABAABABACC', 'ABABACA') == -1)
    assert(kmp('1 2 3 4 5 890', '890') == 10)
    assert(kmp('1 ! 3 4 5 8!0', '890') == -1)
    print('All tests pass')

