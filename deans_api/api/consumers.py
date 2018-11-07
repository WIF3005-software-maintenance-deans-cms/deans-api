# from .models import Crisis
from channels.generic.websocket import JsonWebsocketConsumer, WebsocketConsumer
import json
from .models import Crisis
from .serializer import CrisisSerializer
from rest_framework.response import Response

class CrisesConsumer(WebsocketConsumer):

    def connect(self):
        """
        Perform things on connection start
        """
        self.accept()

    def receive(self, text_data):
        """
        Called when a message is received
        """
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        queryset = Crisis.objects.all()
        serializer = CrisisSerializer(queryset, many=True)
        response = Response(serializer.data) # response is an array of crises
        self.send(json.dumps(list(response.data)));
    
    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass