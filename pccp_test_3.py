from itertools import groupby

def solutions(input_string):
    answer = ''
    p = []
    for i in set(input_string):
        if input_string.count(i) < 2:
            continue
    
        groups = [k for k, _ in groupby(input_string) if k == i]
        if len(groups) >= 2:
            p.append(i)

        answer = ''.join(sorted(p) if p else ['N'])

    return answer

def solution(input_string):
    checked = set()
    result = []

    for ch in input_string:
        if ch in checked:
            continue  # 이미 검사한 문자 건너뛰기
        checked.add(ch)

        count = 0
        in_block = False

        for c in input_string:
            if c == ch:
                if not in_block:
                    count += 1
                    in_block = True
            else:
                in_block = False

        if count >= 2:
            result.append(ch)

    return ''.join(sorted(result) if result else ['N'])


a = 'edeaaabbccd'
k = solutions(a)
kk = solution(a)
print(k)    
print(kk)
