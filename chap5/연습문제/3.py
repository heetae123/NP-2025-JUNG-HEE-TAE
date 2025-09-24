# 3. 두 문자열이 다른 첫 위치 반환
def first_diff_position(str1, str2):
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i] != str2[i]:
            return i
    if len(str1) != len(str2):
        return min_len
    return -1

# 예시
print(first_diff_position("abcde", "abfde"))  # 2
print(first_diff_position("abc", "abc"))      # -1
