import yaml
import json

from pprint import pprint as pp

def output_format(my_file, my_string):

    print '\n\n'
    print '#' * 35
    print my_string
    print '#' * 35
    pp(my_file)

def main():
    #Create variables for each of my files im going to read
    yaml_file = 'yaml_file.yml'
    json_file = 'json_file.json'

    #Use 'with as' command to open each file as 'f'
    #'f' becomes the open file in memory
    #Use the yaml 'load' option to load the file and associate with new variable 'new_yaml_list'
    with open(yaml_file) as f:
         new_yaml_list = yaml.load(f)

    with open(json_file) as f:
        new_json_list = json.load(f)

    output_format(new_yaml_list, 'New list from imported YAML code')
    output_format(new_json_list, 'New list from imported JSON code')
    print '\n'

if __name__ == '__main__':
    main()

