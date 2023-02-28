import json

def load_json(josn_file):
    with open(josn_file) as f:
        print('josn_file = ' + str(josn_file))
        json_data = json.load(f)
        print(type(json_data))
        print(json_data)

if __name__ == '__main__':
    load_json('conf_qa.json')
    load_json('conf_dev.json')