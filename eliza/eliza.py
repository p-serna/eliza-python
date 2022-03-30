import re
import random

class Eliza():
  '''
    Class for an E.L.I.Z.A chatbot

    Input:
     - lang: language 
  '''
  def __init__(self, lang="en"):
    self.lang = lang
    if lang=="en":
      from en import data
    elif lang=="es":
      from es import data
    else:
      raise Exception("Not implement yet!")

    self.vocabulary = data.reflections
    self.vocabulary_keys = self.vocabulary.keys()

  def translate(self, text):
    words = text.lower().strip().split()
    newwords = [self.vocabulary[word] 
                if word in self.vocabulary_keys else word
                  for word in words
                  ]
    return " ".join(newwords)
  
  def respond(self, text):
    pass

if __name__=="__main__":
  therapist = Eliza()
  