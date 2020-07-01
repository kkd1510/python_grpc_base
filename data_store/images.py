import json
import os

JSON_DATA_FILE = 'images_data.json'

class ImagesReader:
    def __init__(self):
        abspath = os.path.abspath(__file__)
        dir_name = os.path.dirname(abspath)
        os.chdir(dir_name)
        self.images = self.read()

    def read(self):
        with open(JSON_DATA_FILE) as json_file:
            return json.load(json_file).get('images')

    def get_by_id(self, id):
        return next((item for item in self.images if item['id'] == id), None)
