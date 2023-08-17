from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
total_unique = 0
palavras_frequentes = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line=line.lower()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    try:
      count = int(count)
    except ValueError:
      #count was not a number, so silently
      #ignore/discard this line
      continue


    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # coloca no dic as palavras e as frequencias que aparecem
            if current_word in palavras_frequentes:
                palavras_frequentes[current_word] += current_count
            else:
                palavras_frequentes[current_word] = current_count
            
            # write result to STDOUT
            print ('%s\t%s' % (current_word, current_count))
            # Contar palavras que nao repetem
            # total_unique += 1
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print( '%s\t%s' % (current_word, current_count))
       
if current_word != word:
    if current_word is not None and current_count == 1:
        total_unique += 1


# print("============================ Histograma da colecao ============================")
# for word, count in palavras_frequentes.items():
#     print(f"{word}:{count}")

# print("============================ Top 10 ============================")
# palavras_frequentes = dict(sorted(palavras_frequentes.items(), key=lambda item:item[1], reverse=True))
# limite = 0
# for word, count in palavras_frequentes.items():
#     print(f"{word}:{count}")
#     limite += 1
#     if limite >= 10: break

# print("Total unique words: %s" %(total_unique))