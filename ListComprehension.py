sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(" ")
word_length = [len(word) for word in words if word!="the"]

print word_length