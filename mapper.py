import sys
import io
import re
import nltk

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

class Mapper:
  def __init__(self):
    self.H = {}
  def Map(self):
    for line in io.TextIOWrapper(sys.stdin.buffer, encoding='latin1'):
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
    for word in self.H.items():
      # print(f"{word}:{count}")
      print("%s\t%s"%(word,self.H[word]))

if __name__ == "__main__":
  despacito = Mapper()
  despacito.Map()
  despacito.Close()