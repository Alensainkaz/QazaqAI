from collections import Counter

words = [
    "low",
    "lowest",
    "lower"
]

def get_pairs(words):
    pairs = []

    for word in words:
        chars = list(word)

        for i in range(len(chars) - 1):
            pair = (chars[i], chars[i + 1])
            pairs.append(pair)

    return pairs

pairs = get_pairs(words)

counter = Counter(pairs)

print('Все пары:', pairs)
print('Кол-во повторений', counter)
print('Самая частая пара', counter.most_common(1))

def merge_pair(words, pair):
    new_words = []

    for word in words:
        new_word = []
        i = 0

        
        while i < len(word):
            if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
                new_word.append(word[i] + word[i + 1])
                i += 2
            else:
                new_word.append(word[i])
                i += 1

        new_words.append(new_word)
    return new_words
words = [
    list("low"),
    list("lowest"),
    list("lower")
]

merged_words = merge_pair(words, ("l", "o"))

print("До объединения:", words)
print("После объединения:", merged_words)    