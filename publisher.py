import redis

connection = redis.Redis(host="127.0.0.1", port=6379)

connection.publish("my-channel", "ciao")
