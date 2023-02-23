import socket

#Making address
port = 2500
address = ("localhost",port)
BUFSIZE = 4096

#Making socket and connect it to address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
while True:
    #Reading input from users and interacts with server by recieving and sending each other.
    msg = input()
    s.send(msg.encode())
    answer = s.recv(BUFSIZE)
    r_msg = answer.decode()
    #If 'closed' message is triggered by server, breaking while loop and finishing client program.
    if r_msg == "Connection Closed":
        print(r_msg)
        break
    #Printing message.
    print(r_msg)