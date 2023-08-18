import sys
import io
import re
import nltk

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

class Mapper:
  def __init__(self):
    self.H = {}
  def Map(self):
    for line in sys.stdin:
      line = line.strip()
      # line = re.sub(r'[^\w\s]', '',line)
      line = line.lower()
      for x in line:
        if x in punctuations:
          line = line.replace(x, " ")
      words = line.split()
      for word in words:
        if word in self.H:
          self.H[word] += 1
        else:
          self.H[word] = 1
      
  def Close(self):
    for word, count in self.H.items():
      print(f"{word}:{count}")

if __name__ == "__main__":
    despacito = Mapper()
    despacito.Map()
    despacito.Close()
