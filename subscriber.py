import redis

connection = redis.Redis(host="127.0.0.1", port=6379)
pubsub = connection.pubsub()

pubsub.subscribe("my-channel")
while True:
    message = pubsub.get_message()
    if message:
        print(message)
