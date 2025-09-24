import random

def number_guessing_game():
    number = random.randint(1, 100)  # 1~100 난수 생성
    attempts = 5  # 최대 시도 횟수

    print("숫자 맞추기 게임을 시작합니다! (1~100 사이 숫자)")
    print(f"총 {attempts}번의 기회가 있습니다.\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"{attempt}번째 시도: 숫자를 입력하세요: "))
        except ValueError:
            print("❗ 숫자만 입력해야 합니다!")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ 1~100 사이의 숫자를 입력하세요.")
            continue

        if guess == number:
            print(f"🎉 정답입니다! {attempt}번 만에 맞추셨습니다.")
            break
        elif guess < number:
            print("⬆️ 더 큰 수를 입력하세요.")
        else:
            print("⬇️ 더 작은 수를 입력하세요.")
    else:
        print(f"😢 실패했습니다. 정답은 {number}였습니다.")

# 게임 실행
number_guessing_game()
