#평년과 윤년 구분하는 프로그램
#• 년도가 4로 나뉘어지고 100으로 나뉘어지지 않거나
#• 400으로 나뉘어지면 윤년이다


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# 사용자 입력
try:
    year = int(input("연도를 입력하세요: "))
    if leap_year(year):
        print(f"{year}년은 윤년입니다.")
    else:
        print(f"{year}년은 평년입니다.")
except ValueError:
    print("숫자만 입력해주세요.")
