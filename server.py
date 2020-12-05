from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

print('Server running...')

clients = []


class SimpleChat(WebSocket):

    def handleMessage(self):
        for client in clients:
            if client != self:
                client.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)

    def handleClose(self):
        clients.remove(self)
        print(self.address, 'closed')


server = SimpleWebSocketServer('localhost', 8000, SimpleChat)
server.serveforever()
