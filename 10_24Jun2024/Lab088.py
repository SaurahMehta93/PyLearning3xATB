letters = ['a','b','c','d','e', 'i', 'j', 'o']

def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

result = filter(filter_vowels, letters)
print(list(result))