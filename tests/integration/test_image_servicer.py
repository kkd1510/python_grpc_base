import grpc
import pytest
from unittest.mock import patch
from api.space_telescope_pb2 import ImageRequest


@pytest.fixture(scope='module')
def grpc_add_to_server():
    from api.space_telescope_pb2_grpc import add_ImageServicer_to_server
    return add_ImageServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from servicer.image_servicer.image_servicer import ImageServicer
    return ImageServicer()


@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    from api.space_telescope_pb2_grpc import ImageStub
    return ImageStub

def test_search_by_id(grpc_stub):
    hello_request = ImageRequest(id='heic1118b')
    response = grpc_stub.GetImageInformation(hello_request)
    assert response.id == 'heic1118b'
    assert response.type == "Observation"

def integration_test_GetImageInformation():
    from api.space_telescope_pb2_grpc import ImageStub
    channel = grpc.insecure_channel('localhost:8080')
    response = ImageStub(channel).GetImageInformation(ImageRequest(id='heic1118b'))
    assert response.id == 'heic1118b'