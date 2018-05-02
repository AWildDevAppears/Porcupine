import json


class JSONLoader:
    @staticmethod
    def load_json_file(path):
        return json.loads(open(path).read())

    @staticmethod
    def save_json_file(path, data):
        with open(path, 'w') as outfile:
            json.dump(data, outfile)
