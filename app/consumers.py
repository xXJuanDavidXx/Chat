from channels.generic.websocket import WebsocketConsumer
import json


class MyConsumer(WebsocketConsumer):

    def connect(self):
        print("me conecte")
        self.accept()

    def receive(self, text_data):
        print('recibi el mensaje')

        text_data_json = json.loads(text_data)
        message = text_data_json = json.loads(text_data)
    
        self.send(text_data=json.dumps(
            {'message':message}))
        
    def disconnect(self, close_code):
        print('desconectado')
        pass
