
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

# Generator
def SentenceMethod(string):
    words = string.split()
    index = 0
    
    while index < len(words):
        yield words[index]
        index += 1

my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)

# Output must be:
# This
# is
# a
# test