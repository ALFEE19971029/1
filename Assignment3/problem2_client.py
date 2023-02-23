from unicodedata import category
import zmq

#Creating subscriber socket and connect it to IP and port
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:2500')

#Getting category from user 
answer = input("category : ")
socket.setsockopt_string(zmq.SUBSCRIBE, answer)

#Recieving message and print it
string = socket.recv()
category, messagedata = string.split(b',')
print(messagedata.decode())


