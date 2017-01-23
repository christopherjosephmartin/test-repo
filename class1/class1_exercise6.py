import yaml
import json

def create_yaml_json_files():
    
    dict1 = {'Name': 'chris', 'Country': 'Australia'}
    
    list1 = [range(4), dict1, 'some string', 104]

    with open('yaml_file.yml', 'w') as f:
        f.write(yaml.dump(list1, default_flow_style=False))

    with open('json_file.json', 'w') as f:
        json.dump(list1, f)

create_yaml_json_files()
