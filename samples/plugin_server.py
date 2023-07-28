import logging
from concurrent import futures

import grpc

from cloudquery.plugin_v3 import plugin_pb2, plugin_pb2_grpc


class PluginServicer(plugin_pb2_grpc.PluginServicer):
    def __init__(self):
        pass

    def GetName(self, request, context):
        return plugin_pb2.GetName.Response(name="plugin test")

    def GetVersion(self, request, context):
        return plugin_pb2.GetVersion.Response(version="0.0.1")

    def Init(self, request, context):
        return plugin_pb2.Init.Response()

    def GetTables(self, request, context):
        return plugin_pb2.GetTables.Response(tables=[])

    def Sync(self, request, context):
        return plugin_pb2.Sync.Response()

    def Read(self, request, context):
        return plugin_pb2.Read.Response()

    def Write(self, request_iterator, context):
        for request in request_iterator:
            print(request)
        return plugin_pb2.Write.Response()

    def Close(self, request, context):
        return plugin_pb2.Close.Response()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    plugin_pb2_grpc.add_PluginServicer_to_server(PluginServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Starting server. Listening on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
