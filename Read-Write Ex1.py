word_stats = {}

with open("poem.txt","r") as f:
    for line in f:
      words = line.split(' ')
      for word in words:
        if word in word_stats:
          word_stats[word] += 1
        else:
          word_stats[word] = 1

print(word_stats)

# STUDY THIS AGAIN PROPERLY + CONTINUE FROM Ex13 - READ/WRITE FILES