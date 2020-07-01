from data_store.images import ImagesReader

class ImageSearch:
    def __init__(self):
        self.image_reader = ImagesReader()

    def search(self, image_id):
        return self.image_reader.get_by_id(image_id)