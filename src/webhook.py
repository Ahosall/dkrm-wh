# By Feh's

import requests

class Webhook:
  def __init__(self, user):
    self._url = "https://discord.com/api/webhooks/1056107728491257897/-WfSEDlzqU2AYE_W0iNIzc-urwRqvziefalN4buGincmT-iMgYccaBDoMqQlcRzkHZMO"
    self._u = user

  def sendMessage(self, message: str) -> None:
    requests.post(self._url, {
      "content": message,
      **self._u
    })
  