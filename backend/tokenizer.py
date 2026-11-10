import re
class Tokenizer:
    def __init__(self):
        self.vocab = {
            "<UNK>": 0,

            # English
            "Hello": 1,
            "world": 2,
            "How": 3,
            "are": 4,
            "you": 5,

            # Русский
            "Привет": 6,
            "мир": 7,
            "Как": 8,
            "дела": 9,

            # Қазақша
            "Сәлем": 10,
            "әлем": 11,
            "Қалайсың": 12,

            # Знаки препинания
            ".": 13,
            ",": 14,
            "!": 15,
            "?": 16
        }
        self.reverse_vocab = {
            token_id: word
            for word, token_id in self.vocab.items()
        }
    def encode(self, text):
        text = text.replace(".", " .")
        text = text.replace("?", " ?")
        tokens = []
        words = re.findall(r"\w+|[^\w\s]", text)
    
        for word in words: 
            token_id = self.vocab.get(word, self.vocab["<UNK>"])
            tokens.append(token_id)
        return tokens 
    def decode(self, tokens):
        words = []
        for token_id in tokens:
            word = self.reverse_vocab.get(token_id, "<UNK>")
            words.append(word)
        result =  " ".join(words)    
        result = re.sub(r"\s+([,.!?])", r"\1", result)

        return result    
tokenizer = Tokenizer()
text = "Hello, world, Сәлем әлем"

result = tokenizer.encode(text)

print(result)