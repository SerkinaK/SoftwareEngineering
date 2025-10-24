import re
def load_forbidden_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        forbidden_words = file.read().split()
    return forbidden_words
def censor_sentence(sentence, forbidden_words):
    for word in forbidden_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)
    return sentence
forbidden_words = load_forbidden_words("censored.txt")
sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is....PYTHON is awesome!!!!"
censored_sentence = censor_sentence(sentence, forbidden_words)
print(censored_sentence)