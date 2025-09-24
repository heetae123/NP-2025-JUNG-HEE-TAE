# 2. 숫자의 자리 합 구하기
def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

# 예시
print(sum_of_digits(123))  # 6
