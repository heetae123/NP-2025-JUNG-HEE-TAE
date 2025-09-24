# 4. 숫자의 약수 리스트 반환
def divisors(number):
    return [i for i in range(1, number+1) if number % i == 0]

# 예시
print(divisors(12))  # [1, 2, 3, 4, 6, 12]
