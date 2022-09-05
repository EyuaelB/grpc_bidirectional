from __future__ import print_function
from ast import While
import grpc
import ChatService_pb2, ChatService_pb2_grpc


def make_client_txt(client_txt):
    return ChatService_pb2.ClientTxt(client_txt=client_txt)

def gen_client_txt():
    c_txts = [
        make_client_txt('first client message'),
        make_client_txt('second client message'),
        make_client_txt('third client message')
    ]

    for c_txt in c_txts:
        print('sending server %s' % c_txt.client_txt)
        yield c_txt

def send_txt(stub):
    responses = stub.chat(gen_client_txt())
    for response in responses:
        print('the server has recieved texts %s' %response.server_txt)



def Sending_txt(stub):
    responses = stub.chat(gen_client_txt())
    for response in responses:
        if response.server_txt is None:
            print('no response')
        else:
            print('text has been sent to the server')



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ChatService_pb2_grpc.ChatServiceStub(channel)
        # stub.chat()
        send_txt(stub)
        # Sending_txt(stub)

while True:
    if __name__ =='__main__':
        run()