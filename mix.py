palindromes = ['hello', 'sentences where punctuation', 45,'Able was I, ere I saw Elba', 34.0, 78.87, 'found', 'level', '12/11/21', 'radar','stats']

def is_str(a):
    if type(a)==str:
        return a

str = list(filter(is_str, palindromes))

true_palindromes = list(filter(lambda word: word == word[::-1], str))
print(true_palindromes)