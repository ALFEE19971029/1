import zmq
import time
import random

#Creating publisher socket and bind it to IP and port
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:2500')

while True:
    #Reproducing situation that server publishes news by categories
    ranNum = random.randrange(0,3)
    categories = ['sports','technology','science']
    messagedata = ['sports news : blahblahblah','technology news : blahblahblah','science news : blahblahblah']
    socket.send_string("%s,%s" % (categories[ranNum], messagedata[ranNum]))
    time.sleep(1)