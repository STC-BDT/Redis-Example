import redis

client = redis.Redis(host="127.0.0.1", port=6379)

print(client.ping())

print(client.get("mykey").decode("utf-8"))

