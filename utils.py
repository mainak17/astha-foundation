import json

class ReadJsonFile:

    @staticmethod
    def read_json_file(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    
    @staticmethod
    def get_keys(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            keys = data[0].keys()
        return keys
    
    @staticmethod
    def get_notifications(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    