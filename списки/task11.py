# задания 11
sentence = input()
words = sentence.split()
longest_word = words[0]
shortest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word
longest_index = words.index(longest_word)
shortest_index = words.index(shortest_word)
words[longest_index], words[shortest_index] = words[shortest_index], words[longest_index]
new_sentence = ' '.join(words)
print( new_sentence)