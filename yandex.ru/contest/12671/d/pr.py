#!python3
"""
NEXT: fix try { func call } catch
fix parsing
"""
import re
from collections import defaultdict


q_num = int(input().strip())
queries = [int(input().strip()) for _ in range(q_num)]
functions_num = int(input().strip())
body = []
while True:
    try:
        body += [input().strip()]
    except EOFError:
        break

functions = {}

def parse_try(try_match, i):
    print('parse_try', i)
    i += 1
    throws = set()
    while True:
        end_match = re.match(r'}\s+supress\s+(.*)$', body[i])
        if end_match:
            if end_match.groups > 0 and end_match.group(1):
                names = [n.strip() for n in end_match.group(1).split(',')]
                for n in names:
                    throws.remove(n)
            break
        throw_match = re.match(r'maybethrow\s+(\w+)', body[i])
        if throw_match:
            throws.add(throw_match.groups(1))
            i += 1
            continue
        other_try_match = re.match('try {', body[i])
        if other_try_match:
            i, try_throws = parse_try(other_try_match, i)
            throws.union(try_throws)
            i += 1
            continue
        i += 1
    return i, throws

def parse_func(func_match, i):
    print('parse_func', i)
    i += 1
    funcname = func_match.groups(1)
    throws = set()
    func_calls = set()
    while not re.match(r'}', body[i]):
        throw_match = re.match(r'maybethrow (\w+)', body[i])
        if (throw_match):
            throws.add(throw_match.groups(1))
            i += 1
            continue
        try_match = re.match(r'try {', body[i])
        if try_match:
            i, try_throws = parse_try(try_match, i)
            throws.union(try_throws)
            i += 1
            continue
        func_call_match = re.match(r'(\w)\s*\(\s*\)', body[i])
        if func_call_match:
            func_calls.add(func_call_match.group(1))
            i += 1
            continue
    functions[funcname] = (throws, func_calls)
    return i


visited = set()
def get_throws(funcname):
    print('get_throws', i)
    if funcname in visited:
        return set()
    visited.add(funcname)
    if funcname in functions:
        throws, calls = functions[funcname]
        for otherfunction in calls:
            throws.union(get_throws(otherfunction))
    return throws

i = 0
while i < len(body):
    func_match = re.match(r'func\s+(\w+)\s*\(\s*\)\s*{', body[i])
    if func_match:
        i = parse_func(func_match, i)
    i += 1

for line in queries:
    throw_match = re.match(r'maybethrow (\w+)', body[line-1])
    if throw_match:
        print(throw_match.group(1))
        continue
    func_call_match = re.match(r'(\w)\s*\(\s*\)', body[line-1])
    throws = set()
    if func_call_match:
        funcname = func_call_match.group(1)
        visited = set()
        throws = get_throws(funcname)
    print(' '.join(throws))







        
