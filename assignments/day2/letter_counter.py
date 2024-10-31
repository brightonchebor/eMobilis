word = str(input('Enter any single word: '))
letter_counter = {}

for letter in word:
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] = 1

for letter, count in letter_counter.items():
    print(f'{letter} : {count}')    