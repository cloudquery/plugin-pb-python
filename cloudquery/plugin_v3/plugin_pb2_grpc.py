# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from cloudquery.plugin_v3 import plugin_pb2 as cloudquery_dot_plugin__v3_dot_plugin__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in cloudquery/plugin_v3/plugin_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PluginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetName = channel.unary_unary(
                '/cloudquery.plugin.v3.Plugin/GetName',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetName.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetName.Response.FromString,
                _registered_method=True)
        self.GetVersion = channel.unary_unary(
                '/cloudquery.plugin.v3.Plugin/GetVersion',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetVersion.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetVersion.Response.FromString,
                _registered_method=True)
        self.GetSpecSchema = channel.unary_unary(
                '/cloudquery.plugin.v3.Plugin/GetSpecSchema',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetSpecSchema.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetSpecSchema.Response.FromString,
                _registered_method=True)
        self.Init = channel.unary_unary(
                '/cloudquery.plugin.v3.Plugin/Init',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Init.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Init.Response.FromString,
                _registered_method=True)
        self.GetTables = channel.unary_unary(
                '/cloudquery.plugin.v3.Plugin/GetTables',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetTables.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetTables.Response.FromString,
                _registered_method=True)
        self.Sync = channel.unary_stream(
                '/cloudquery.plugin.v3.Plugin/Sync',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Sync.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Sync.Response.FromString,
                _registered_method=True)
        self.Read = channel.unary_stream(
                '/cloudquery.plugin.v3.Plugin/Read',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Read.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Read.Response.FromString,
                _registered_method=True)
        self.Write = channel.stream_unary(
                '/cloudquery.plugin.v3.Plugin/Write',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Write.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Write.Response.FromString,
                _registered_method=True)
        self.Close = channel.unary_unary(
                '/cloudquery.plugin.v3.Plugin/Close',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Close.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Close.Response.FromString,
                _registered_method=True)
        self.TestConnection = channel.unary_unary(
                '/cloudquery.plugin.v3.Plugin/TestConnection',
                request_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.TestConnection.Request.SerializeToString,
                response_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.TestConnection.Response.FromString,
                _registered_method=True)


class PluginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetName(self, request, context):
        """Get the name of the plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
        """Get the current version of the plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSpecSchema(self, request, context):
        """Get plugin spec schema.
        This will allow validating the input even before calling Init.
        Should be called before Init.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Init(self, request, context):
        """Configure the plugin with the given credentials and mode
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTables(self, request, context):
        """Get all tables the source plugin supports. Must be called after Init
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sync(self, request, context):
        """Start a sync on the source plugin. It streams messages as output.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Start a Read on the source plugin for a given table and schema. It streams messages as output.
        The plugin assume that that schema was used to also write the data beforehand
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request_iterator, context):
        """Write resources. Write is the mirror of Sync, expecting a stream of messages as input.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Send signal to flush and close open connections
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestConnection(self, request, context):
        """Validate and test the connections used by the plugin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PluginServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetName,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetName.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetName.Response.SerializeToString,
            ),
            'GetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersion,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetVersion.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetVersion.Response.SerializeToString,
            ),
            'GetSpecSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSpecSchema,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetSpecSchema.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetSpecSchema.Response.SerializeToString,
            ),
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Init.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Init.Response.SerializeToString,
            ),
            'GetTables': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTables,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetTables.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.GetTables.Response.SerializeToString,
            ),
            'Sync': grpc.unary_stream_rpc_method_handler(
                    servicer.Sync,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Sync.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Sync.Response.SerializeToString,
            ),
            'Read': grpc.unary_stream_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Read.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Read.Response.SerializeToString,
            ),
            'Write': grpc.stream_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Write.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Write.Response.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Close.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.Close.Response.SerializeToString,
            ),
            'TestConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.TestConnection,
                    request_deserializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.TestConnection.Request.FromString,
                    response_serializer=cloudquery_dot_plugin__v3_dot_plugin__pb2.TestConnection.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cloudquery.plugin.v3.Plugin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cloudquery.plugin.v3.Plugin', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Plugin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/GetName',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.GetName.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.GetName.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/GetVersion',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.GetVersion.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.GetVersion.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSpecSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/GetSpecSchema',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.GetSpecSchema.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.GetSpecSchema.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/Init',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Init.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Init.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/GetTables',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.GetTables.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.GetTables.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Sync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/Sync',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Sync.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Sync.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/Read',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Read.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Read.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Write(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/cloudquery.plugin.v3.Plugin/Write',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Write.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Write.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/Close',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Close.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.Close.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TestConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cloudquery.plugin.v3.Plugin/TestConnection',
            cloudquery_dot_plugin__v3_dot_plugin__pb2.TestConnection.Request.SerializeToString,
            cloudquery_dot_plugin__v3_dot_plugin__pb2.TestConnection.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
