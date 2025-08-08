def solutions(nums):
    answer = 0
    max_su = len(nums) // 2
    p = []

    for i in nums:
        if i not in p:
            p.append(i)
    
    if len(nums) < max_su:
        answer = len(p)
    else:
        answer = max_su
    
    return answer

def solution(nums):
    answer = 0
    max_su = len(nums) // 2
    p = set(nums)
    answer = min(len(p), max_su)

    return answer


a = [3,3,3,2,2,4]
k = solutions(a)
kk = solution(a)
print(f"k = {k}, kk = {kk}")