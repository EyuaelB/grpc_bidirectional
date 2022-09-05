import grpc
from concurrent import futures

import ChatService_pb2_grpc 

class ChatService(ChatService_pb2_grpc.ChatServiceServicer):
    def chat(self, request_iterator, context):
        for client_txt in request_iterator:
            print(client_txt)
            yield client_txt

def serve():
    server= grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ChatService_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(),server=server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ =='__main__':
    serve()
