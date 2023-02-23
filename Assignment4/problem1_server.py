from wsgiref.simple_server import make_server
import csv

def simple_app(environ, start_response):
    #Setting response
    status = '200 OK'
    response_headers = [('Content-type','text/plain; charset=utf-8')]
    start_response(status, response_headers)
    #Receiving data from client through wsgi
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    request_body = environ['wsgi.input'].read(request_body_size)
    #Reading .csv file to give definition to client
    f = open('problem1_csv.csv','r',encoding='utf-8')
    rdr = csv.reader(f)
    #Read by line 
    for line in rdr:
        #If keyword is same, send proper response
        if line[0] == request_body.decode():
            response = [line[1].encode('utf-8')]
            return response
    #If no keyword found, send no keyword message and send response
    response = ["No keyword!".encode('utf-8')]
    return response

if __name__ == '__main__':
    #Binding http socket to localhost:8000
    try:
        httpd = make_server('127.0.0.1',8000, simple_app)
        host, port = httpd.socket.getsockname()
        print('serving on',host,'port',port)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Goodbye.")


















# from http.server import HTTPServer, BaseHTTPRequestHandler

# class helloHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('content-type','text/html')
#         self.end_headers()
#         self.wfile.write('Hello'.encode())
    
# if __name__ == '__main__':
#     PORT = 8000
#     server = HTTPServer(('',PORT), helloHandler)
#     print('Server running on port %s' % PORT)
#     server.serve_forever()