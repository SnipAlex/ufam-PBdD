import operator
import io
import sys

current_word = None
current_count = 0
word = None
total_unique = 0
palavras_frequentes = {}
# input comes from STDIN
for line in io.TextIOWrapper(sys.stdin.buffer, encoding='latin1'):
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    try:
      count = int(count)
    except ValueError:
      #count was not a number, so silently
      #ignore/discard this line
      continue

    palavras_frequentes[word] = count

    if count == 1:
        total_unique += 1
    

print("============================ Histograma da colecao ============================")
# for word, count in line.items():
#     print(f"{word}:{count}")
palavras_frequentes = sorted(palavras_frequentes.items(), key=operator.itemgetter(1), reverse=True)

for i in range(10):
   print(palavras_frequentes[i])

print("============================ Top 10 ============================")

limite = 0
for word, count in palavras_frequentes:
    print(f"{word}:{count}")
    limite += 1
    if limite >= 10: break

print("Total unique words: %s" %(total_unique))