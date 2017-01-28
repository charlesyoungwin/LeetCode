import re
def reverseVowels(s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


s = 'leeTCOde'
sList = list(s)
print(reverseVowels(s))

