# By Feh's 
import json

from time import time

def loadChars():
  f = open('chars.json', 'r', encoding='utf-8')
  d = json.loads(f.read())
  f.close()
  return d

def saveChars(datas):
  try:
    f = open('chars.json', 'w+')
    f.write(json.dumps(datas))
    f.close()
    return True
  except:
    return False

class Characters:
  '''
  `character`: enter the character identifier.
  '''
  def __init__(self):
    self._chars = loadChars()['chars']
  
  def get(self, cid:str) -> object:
    try:
      return [char for char in self._chars if char['id'] == cid][0]
    except:
      return None
  
  def add(self, data):
    new = {
      "uid": int(time()),
      "username": None,
      "avatar_url": None,
      **data
    }

    self._chars.append(new)
    saveChars({"chars": self._chars})

  def edt(self, cid:str, data:object):
    char = self.get(cid)
    mod = {**char, **data}
    self._chars[[idx for idx, char in enumerate(self._chars) if char['id'] == cid][0]] = mod
    saveChars({"chars": self._chars})
    
  def rem(self, cid:str):
    del self._chars[[idx for idx, char in enumerate(self._chars) if char['id'] == cid][0]]
    saveChars({"chars": self._chars})