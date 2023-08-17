import sys
import io
import re
import nltk

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
current_count = None
current_word = None
class Mapper:
  def __init__(self):
    H = {}
  def Map(self):
    for line in sys.stdin:
      line = line.strip()
      line = re.sub(r'[^\w\s]', '',line)
      line = line.lower()
      for x in line:
        if x in punctuations:
          line = line.replace(x, " ")
      words = line.split()
      self.H[words] += 1
      
  def Close(self):
    # word, count = line.split('\t', 1)
    for word, count in self.H.items():
      if current_word == word:
        current_count += count
      else:      
        print(f"{word}:{count}")

if __name__ == "__main__":
    despacito = Mapper()
    despacito.Map()
    despacito.Close()
