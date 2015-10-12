import threading
import redis
import time

def handleTask(data):
    print "started " + str(data)
    time.sleep(10)
    print "finished " + str(data)

def main():
    count = 0
    r = redis.client.StrictRedis()
    sub = r.pubsub()
    sub.subscribe('clock')
    while True:
        for m in sub.listen():
            count += 1
            t = threading.Thread(target=handleTask, args=(count,))
            t.start()

if __name__ == '__main__':
    main()
