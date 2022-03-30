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
      import eliza.en.data as data
    elif lang=="es":
      import eliza.es.data as data
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
  