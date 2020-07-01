import grpc
from concurrent import futures

import api.space_telescope_pb2_grpc
from servicer.image_servicer.image_servicer import  ImageServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    api.space_telescope_pb2_grpc.add_ImageServicer_to_server(ImageServicer(), server)
    server.add_insecure_port('[::]:27015')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()