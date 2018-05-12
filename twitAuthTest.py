import twitter

api = twitter.Api(consumer_key= 'PvOiahL2mZhilZQm249PdMGOv', consumer_secret= 't4XdV4AK61CtUV8QxA1s8HVtK2uFAIh31wRAOEahAMFzR0xbnV', access_token_key = '995332330800664577-fERWtYzOGpQgvzVgBI0pDORo92Ucbo4', access_token_secret='nAF5QyakEyEgqV9yjOTZB8cFxsmPc8UhBLZWEfU6Bu0j5'  )

print(api.VerifyCredentials())

help(twitter.api)