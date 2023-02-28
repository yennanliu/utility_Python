import json

def load_json(josn_file):
    with open(josn_file) as f:
        print('josn_file = ' + str(josn_file))
        json_data = json.load(f)
        #print(type(json_data))
        #print(json_data)
        return json_data

def modify(update_json_file, json_data):
    to_update = load_json(update_json_file)
    if len(to_update) == 0:
        return json_data
    for k, v in to_update.items():
        json_data[k] = v
    return json_data


if __name__ == '__main__':
    #load_json('conf.json')
    #print('')
    #load_json('conf_dev.json')
    json_data = load_json('conf.json')
    print('json_data = ' + str(json_data))
    updated_json_data = modify('conf_qa.json', json_data)
    print('updated_json_data = ' + str(updated_json_data)) 
