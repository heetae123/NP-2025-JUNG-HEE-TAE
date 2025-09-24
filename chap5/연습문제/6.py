# 6. 재귀로 1부터 100까지 합 계산
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n-1)

# 예시
print(recursive_sum(100))  # 5050
