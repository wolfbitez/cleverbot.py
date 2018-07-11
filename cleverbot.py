import json, asyncio, requests
from aiohttp import ClientSession

class Client(object):
    def __init__(self, user, key, nick):
        self.user = user
        self.key = key
        self.nick = nick

        body = {
            'user': user,
            'key': key,
            'nick': nick
        }

        
        requests.post('https://cleverbot.io/1.0/create', json=body)

    def ask(self, text):
        body = {
            'user': self.user,
            'key': self.key,
            'nick': self.nick,
            'text': text
        }

        r = requests.post('https://cleverbot.io/1.0/ask', json=body)
        r = json.loads(r.text)

        if r['status'] == 'success':
            return r['response']
        else:
            return False

    async def async_ask(self, text):
        body = {
            'user': self.user,
            'key': self.key,
            'nick': self.nick,
            'text': text
        }
        
        async with ClientSession() as session:
            async with session.post('https://cleverbot.io/1.0/ask', json=body) as response:

                response = await response.read()
                r = json.loads(response)

                if r['status'] == 'success':
                    return r['response']
                else:
                    return False
