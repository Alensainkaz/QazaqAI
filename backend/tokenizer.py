class Tokenizer:
    def __init__(self):
        self.vocab = {
            "Hello": 0, 
            "World": 1,
            "How": 2,
            "are": 3,
            "you": 4,
            "?": 5,
            ".": 6,
            "<UNK>": 7
        }
    def encode(self, text):
        text = text.replace(".", " .")
        text = text.replace("?", " ?")
        tokens = []
        words = text.split()
    
        for word in words: 
            token_id = self.vocab.get(word, self.vocab["<UNK>"])
            tokens.append(token_id)
        return tokens 
    
tokenizer = Tokenizer()
text = "Hello, World"

result = tokenizer.encode(text)

print(result)