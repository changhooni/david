from itertools import combinations

def solutions(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    count = 0
    n = len(nums)

    def count_prime_sums(nums):
        # 3중 for문으로 서로 다른 3개 선택
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    total = nums[i] + nums[j] + nums[k]
                    if is_prime(total):
                        count += 1

        return count
    answer = count_prime_sums(nums)

    return answer

def solution(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    count = 0
    def count_prime_sums(nums):
        for comb in combinations(nums, 3):  # 3개 조합
            total = sum(comb)
            if is_prime(total):
                count += 1
        return count

    answer = count_prime_sums(nums)

    return answer

nums = [1, 2, 3, 4]
print(solutions(nums))  # 출력: 1
