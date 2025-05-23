import json

def write_json(filename, data):
    with open(filename,'w') as file:
        json.dump(data, file, indent=4)
        
def read_json(filename):
    with open(filename, 'r') as file:
        save_data = json.load(file)
    return save_data