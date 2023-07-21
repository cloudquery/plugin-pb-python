import logging
import grpc
from cloudquery.plugin_v3 import plugin_pb2, plugin_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = plugin_pb2_grpc.PluginStub(channel)
        response = stub.GetName(plugin_pb2.GetName.Request())
        print(response.name)

if __name__ == '__main__':
    logging.basicConfig()
    run()
