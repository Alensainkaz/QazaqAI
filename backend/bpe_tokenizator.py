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