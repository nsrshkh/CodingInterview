def reverseVowels(s: str) -> str:
    vowel_list = set("aeiouAEIOU")
    vowels = [i for i in s if i in vowel_list]
    result = [i if i not in vowel_list else vowels.pop() for i in s]
    return ''.join(result)

s = "IceCreAm"
print(reverseVowels(s))
