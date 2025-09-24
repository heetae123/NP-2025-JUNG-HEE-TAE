# 10진수를 입력 받아 2진수로 변환하여 출력하는 프로그램

try:
    decimal = int(input("10진수를 입력하세요: "))
    if decimal == 0:
        print("0의 2진수: 0")
    else:
        binary = ""
        num = decimal
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        print(f"{decimal}의 2진수: {binary}")
except ValueError:
    print("숫자만 입력해주세요.")
