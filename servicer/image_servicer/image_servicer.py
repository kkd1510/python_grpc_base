import logging

import api.space_telescope_pb2
import api.space_telescope_pb2_grpc

from servicer.image_servicer.search import ImageSearch
from google.protobuf import json_format

logger = logging.getLogger(__name__)


class ImageServicer(api.space_telescope_pb2_grpc.ImageServicer):

    def GetImageInformation(self, request, context):
        image = ImageSearch().search(request.id)
        return api.space_telescope_pb2.ImageReply(**image)
