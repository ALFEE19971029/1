import asyncio
import random

#Making coroutine
@asyncio.coroutine
def handle_conversation(reader, writer):
    while True:
        #Read data from client
        data = yield from reader.read(4096)
        #Decoding message
        message = data.decode()
        #Making random number
        x = random.randrange(1, 11)
        if message == "start" :
            writer.write("Guess the number between 1~10".encode())
            #Give 5 times opportunity
            guessCnt = 5            
            while True:
                #Sending messages depend on recived message from client
                data = yield from reader.read(4096)
                guess = data.decode()
                s_data = b''
                if guess == "end":
                    s_data += b"The game is over"
                    writer.write(s_data)  
                    s_data = b''   
                    break
                elif int(guess) == x :
                    s_data += b"Congratulations you did it." 
                    writer.write(s_data)  
                    s_data = b''                     
                    break
                elif int(guess) < x :
                    s_data += b"You guessed too small!"                     
                    guessCnt = guessCnt - 1
                elif int(guess) > x :
                    s_data += b"You Guessed too high!"                    
                    guessCnt = guessCnt - 1
                
                #Sending you lose when there is no chance anymore
                if guessCnt == 0:
                    s_data += b"You lose!"   
                    writer.write(s_data)  
                    s_data = b''               
                    break
                writer.write(s_data)

        #Sending 'close' when client request 'close'
        elif message == "close": 
            writer.write("Connection Closed".encode())
            writer.close()
            break
        #Sending error message when client request wrong answer
        else :
            writer.write("Type message correctly".encode())
            continue        
        
#Making event loop
loop = asyncio.get_event_loop()
#Start server which provide handle_conversation method
coro = asyncio.start_server(handle_conversation, '127.0.0.1', 2500, loop=loop)
#Server keeps running during coroutines are running 
server = loop.run_until_complete(coro)
try :
    #Server keeps running
    loop.run_forever()
finally :
    #Server closes
    server.close()
    loop.close()


