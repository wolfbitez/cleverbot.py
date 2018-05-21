# cleverbot.py
Cleverbot.io functionality implemented into Python 3.

### Usage example:
```python
>>> import cleverbot
>>> bot = cleverbot.Client(user='user', key='key', nick='nick')
>>> print(bot.ask('Hello!'))
Hi.
```

### How do I get the "user" and "key"?
1. Head on over to https://cleverbot.io/ and click "My Keys"
1. Sign up for an account (or sign in)
1. After signing in, it should bring you to your info.

API User is your `user`, and API Key is your `key`.
