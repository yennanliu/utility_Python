import json

def load_json(josn_file):
    with open(josn_file) as f:
        print('josn_file = ' + str(josn_file))
        json_data = json.load(f)
        print(type(json_data))
        #print(json_data)
        return json_data

def modify(update_json_file, json_data):
    to_update = load_json(update_json_file)
    if len(to_update) == 0:
        return json_data
    for k, v in to_update.items():
        if k in json_data.keys():
            json_data[k] = v
    #return json_data
    mydict = {}
    return {**json_data, **mydict}
    #return {**json_data}

def modifyV2(conf_dict, to_update_conf_dict):
    return {**conf_dict, **to_update_conf_dict}   

if __name__ == '__main__':

    #load_json('conf.json')
    #print('')
    #load_json('conf_dev.json')

    json_data = load_json('conf.json')
    print('json_data = ' + str(json_data))
    #updated_json_data = modify('conf_qa.json', json_data)
    #updated_json_data = modify('conf_dev.json', json_data)
    to_update_data = load_json('conf_qa.json')
    print('to_update_data = ' + str(to_update_data))
    # updated_json_data = modify(to_update_data, json_data)
    # print('updated_json_data = ' + str(updated_json_data))

    res = modifyV2(json_data, to_update_data)
    print('updated_json_data = ' + str(res))