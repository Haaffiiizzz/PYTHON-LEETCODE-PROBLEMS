words = ["Hello","Alaska","Dad","Peace"]  # to test
output = []
keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm" ]
for word in words:
    for row in keyboard:
        if set(word.lower()).issubset(set(row)):
            output.append(word)
print(output)   #   return instead of print 