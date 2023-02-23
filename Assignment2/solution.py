import json
import zlib
import socket
import ssl


class Solution():
    
    def special_bits(self, L=1, R=2, k=1):
        num = -2
        # Write your code between start and end for solution of problem 1
        # Start
        num = L
        while True:
            if str(bin(num)).count('1') == k:
                break
            num += 1
            if num > R:
                num = -1
                break
        # End
        return num

    def toggle_string(self, S):
        s = ""
        # Write your code between start and end for solution of problem 2
        # Start
        for i in range(len(S)):
            if S[i].isupper():
                s = s + S[i].lower()
            else:
                s = s + S[i].upper()
        # End
        return s

    def send_message(self, message):
        message = self.to_json(message)
        message = self.encode(message)
        message = self.compress(message)
        return message

    def recv_message(self, message):
        message = self.decompress(message)
        message = self.decode(message)
        message = self.to_python_object(message)
        return message
    
    # String to byte
    def encode(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        return str(message).encode('utf-8')
        # End
        
    
    # Byte to string
    def decode(self,message):
        # Write your code between start and end for solution of problem 3
        # Start
        return message.decode('utf-8')
        # End 

    # Convert from python object to json string
    def to_json(self, message):
        # Write your code between start and end for solution of problem 3
        # Start        
        return json.dumps(message)
        # End 

    # Convert from json string to python object
    def to_python_object(self, message):
        # Write your code between start and end for solution of problem 3
        # Start        
        return json.loads(message)
        # End 
    
    # Returns compressed message 
    def compress(self, message):
        # Write your code between start and end for solution of problem 3
        # Start        
        return zlib.compress(message)
        # End 

    # Returns decompressed message
    def decompress(self, compressed_message):
        # Write your code between start and end for solution of problem 3
        # Start
        return zlib.decompress(compressed_message)
        # End 


    def client(self, host, port, cafile=None):
        # Write your code between start and end for solution of problem 4
        # Start
        cert = "" # Variable to store the certificate received from server 
        cipher = "" # Variable to store cipher used for connection
        msg = "" # Variable to store message received from server
        ssl.match_hostname = lambda cert, hostname: True

        purpose = ssl.Purpose.SERVER_AUTH
        context = ssl.create_default_context(purpose, cafile=cafile)

        raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        raw_sock.connect((host,port))
        ssl_sock = context.wrap_socket(raw_sock, server_hostname=host)

        cert = ssl_sock.getpeercert()
        cipher = ssl_sock.cipher()

        tmpMsg = b""
        while True :
            data = ssl_sock.recv(1024)
            tmpMsg += data
            if not data:
                break
        msg = tmpMsg.decode('ascii')
        # End
        return cert, cipher, msg
    
    

    
