# By Feh's

from src.webhook import Webhook
from src.characters import Characters
from src.utils import brand

characters = Characters()

# Menu add
def MenuMore():
  brand()
  print('=== Select an option')
  print('\n'.join([
    '  - [1]: Add',
    '\n  - [0]: Back'
  ]))

  opt = input(':>>')
  
  if not opt.isdigit():
    return MenuMore()

  if int(opt) == 0:
    return main()
  elif int(opt) == 1:
    brand()
    print("=== Enter the user ...")
    username = input('  - username: ')
    avatar = input('  - avatar: ')
    characters.add({"username": username, "avatar_url": avatar})
    return main()
  
# Select character
def SelectCharacter():
  brand()
  print('=== Select your character')
  for idx, char in enumerate(characters._chars):
    print(f'  - [{idx + 1}]: {char["username"]} -> {char["avatar_url"]}')

  print(f'\n  - [0]: More...')
  
  opt = input('\n:>> ')

  if not opt.isdigit():
    return SelectCharacter()
  
  if int(opt) == 0:
    MenuMore()

  return characters._chars[int(opt) - 1]


def main():
  char = SelectCharacter()
  wh = Webhook(char)
  brand()
  print('Press ctrl + c to stop...')
  while True:
    inp = input('Message: ')
    if not inp.replace(' ', '') == "":
      wh.sendMessage(inp)

if __name__ == "__main__":
  try: 
    main()
  except Exception as e:
    print(e)
    exit(1)
  except KeyboardInterrupt:
    exit(0)