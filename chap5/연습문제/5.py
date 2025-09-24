# 5.문자열에서 특정 문자의 위치 반환
def find_all_positions(string, char):
    return [i for i, c in enumerate(string) if c == char]

# 예시
print(find_all_positions("hello world", "l"))  # [2, 3, 9]
