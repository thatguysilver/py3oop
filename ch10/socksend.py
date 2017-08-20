# We look at an example of using decorators with the socket library.

import socket

def respond(client):
    response = input('Enter a value: ')
    client.send(bytes(response, 'utf8'))
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2403))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(LogSocket(client))
finally:
    server.close()

class LogSocket:
    'A decorator that outputs our data before sending it to sockrec.'
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print(f'sending {data} to {self.socket.getpeername()[0]}')
    self.socket.send(data)

    def close(self):
        self.socket.close()

