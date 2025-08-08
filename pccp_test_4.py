#학교 체육대회에는 여러 종목이 있다.
#각 반의 학생들이 종목별로 능력치를 갖고 있다.
#각 종목에 1명씩만 출전 가능,
#한 학생은 하나의 종목에만 출전 가능하다.
#학생 수 ≥ 종목 수
#이때, 출전한 학생들의 총 능력치 합이 최대가 되도록 대표를 선발한다.

from itertools import permutations

def solutions(ability):
    n = len(ability)
    m = len(ability[0])

    if n < m:
        raise ValueError('학생 수가 종목 수보다 적어서 배정이 불가능합니다.')
    
    answer = 0

    # 학생 인덱스를 종목 개수만큼 순열로 뽑기 (학생 수 = 종목 수)
    for order in permutations(range(n), m):
        score = 0
        for i in range(m):  # i = 종목 번호
            student = order[i]
            score += ability[student][i]
        answer = max(answer, score)

    return answer

def solution(ability):
    n = len(ability)      # 학생 수
    m = len(ability[0])   # 종목 수

    visited = [False] * n
    max_score = 0

    def dfs(subject_idx, score_sum):
        nonlocal max_score

        # 모든 종목에 배정 완료
        if subject_idx == m:
            max_score = max(max_score, score_sum)
            return

        # 모든 학생 중 한 명을 현재 종목에 배정
        for student in range(n):
            if not visited[student]:
                visited[student] = True
                dfs(subject_idx + 1, score_sum + ability[student][subject_idx])
                visited[student] = False  # 백트래킹

    dfs(0, 0)
    return max_score


students = [
    [20, 30],
    [30, 20],
    [20, 30]
]

print(solutions(students))  
print(solution(students))  


