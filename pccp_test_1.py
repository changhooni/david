def solutions(nums):
    answer = 0
    max_su = len(nums) // 2
    p = []

    for i in nums:
        if i not in p: #중복 처리
            p.append(i)
    
    if len(nums) < max_su:
        answer = len(p)
    else:
        answer = max_su
    
    return answer

def solution(nums):
    answer = 0
    max_su = len(nums) // 2 # 리스트에 반으로 나누는 최대치
    p = set(nums) # set 내장 함수 중복처리
    answer = min(len(p), max_su)

    return answer


a = [3,3,3,2,2,4]
k = solutions(a)
kk = solution(a)
print(f"k = {k}, kk = {kk}")