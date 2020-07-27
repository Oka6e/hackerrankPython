import re

def find_2_vowels(S):
    vowels = '[aeiou]'
    consonants = '[qwrtypsdfghjklzxcvbnm]'
    # ?<= matches a vowel only if preceded by a consonant
    pattern = r'(?<=' + consonants + ')(' + vowels + '{2,})' + consonants

    m = re.findall(pattern, S, re.I)
    print('\n'.join(m or ['-1']))

if __name__ == '__main__':
    S = input()

    find_2_vowels(S)
