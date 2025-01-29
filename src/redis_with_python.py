import redis

client = redis.Redis(host="127.0.0.1", port=6379)

# print(client.ping())
#
# print(client.set("mykey", "myvalue", ex=10))

if client.exists("mykey"):
    print(client.get("mykey").decode("utf-8"))
else:
    print("No key")

print(client.keys("*"))



#
# client.lpush("mylist", "1")
# client.lpush("mylist", "2")

# print(client.lrange("mylist", 0, -1))

# print(client.get("mykey").decode("utf-8"))

