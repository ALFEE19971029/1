import requests

#Connecting to HTTP Server by specific URL
url = 'http://127.0.0.1:8000'
#Read keyword from the client
keyWord = input("Type Keyword : ")
#Using POST to send data to server
x = requests.post(url, data = keyWord)
#Printing response body
print(x.text)