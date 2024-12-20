
# -*- encoding: UTF-8 -*-
'''
@filename    : configuration.py
@description : 从项目的settings文件夹中读取.ini,.json,.yaml,.txt 等配置文件,并解析配置文件内容。
@time        : 2024/12/20
@author      : Zhao Pengpeng
'''

import os
import json
import yaml
from configparser import RawConfigParser

def read_file(path:str, mode='r', encoding='utf-8'):
    """
    Summary : 读取文件内容，返回字符串。
              param / type / descrption
    Input   : path / [str] / [文件路径]
              mode / [str] / [读写模式，默认'r']
              encoding / [str] / [编码格式，默认'utf-8']
    Output  : content / [type] / [文件内容]
    """
    try:
        with open(path, mode, encoding=encoding) as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        return None

def parse_config(content, parser_func, path):
    """
    Summary : 解析配置文件。
              param / type / descrption
    Input   : content / [type] / [description]
              parser_func / [type] / [description]
              path / [type] / [description]
    Output  : param / [type] / [description]
    """
    try:
        return parser_func(content)
    except Exception as e:
        print(f"Error parsing file {path}: {e}")
        return None

def read_ini(path):
    """
    Summary : 读取ini文件，返回 RawConfigParser 对象。
              param / type / descrption
    Input   : path / [type] / [description]
    Output  : content / [type] / [description]
    """
    try:
        content = RawConfigParser()
        content.read(filenames=path, encoding='utf-8')
        # 输出 RawConfigParser 对象的内容

        # for section in content.sections():
        #     print(f"Section: {section}")
        #     for option in content.options(section):
        #         value = content.get(section, option)
        #         print(f"  {option}: {value}")
        return content
    except Exception as e:
        print(f"Error reading ini file {path}: {e}")
        return None

def read_json(path):
    """
    Summary : 读取json文件，返回字典对象。
              param / type / descrption
    Input   : path / [type] / [description]
    Output  : content / [type] / [description]
    """
    content = read_file(path)
    content = json.loads(content) if content else None
    return content

    # return parse_config(content, json.loads, path) if content else None

def read_yaml(path):
    """
    Summary : 读取yaml文件，返回字典对象。
              param / type / descrption
    Input   : path / [type] / [description]
    Output  : content / [type] / [description]
    """
    content = read_file(path)
    content = yaml.safe_load(content) if content else None
    return content

    # return parse_config(content, yaml.safe_load, path) if content else None

def write_file(path, data, mode='w', encoding='utf-8'):
    """
    Summary : 写入文件内容。
              param / type / descrption
    Input   : path / [type] / [description]
              data / [type] / [description]
              mode / [str] / [读写模式，默认'w']
              encoding / [str] / [编码格式，默认'utf-8']
    Output  : param / [type] / [description]
    """
    try:
        with open(path, mode, encoding=encoding) as f:
            f.write(data)
        return True
    except Exception as e:
        print(f"Error writing file {path}: {e}")
        return False

def convert_json_to_yaml(json_path, yaml_path):
    """
    Summary : 转换json文件为yaml文件。
              param / type / descrption
    Input   : json_path / [type] / [description]
              yaml_path / [type] / [description]
    Output  : param / [type] / [description]
    """
    data = read_json(json_path)
    if data:
        yaml_data = yaml.dump(data, default_flow_style=False, allow_unicode=True)
        if write_file(yaml_path, yaml_data):
            print(f"文件已成功转换并保存到 {yaml_path}")

def convert_yaml_to_json(yaml_path, json_path):
    """
    Summary : 转换yaml文件为json文件。
              param / type / descrption
    Input   : yaml_path / [type] / [description]
              json_path / [type] / [description]
    Output  : param / [type] / [description]
    """
    data = read_yaml(yaml_path)
    if data:
        json_data = json.dumps(data, ensure_ascii=False, indent=4)
        if write_file(json_path, json_data):
            print(f"文件已成功转换并保存到 {json_path}")

def read_txt(path):
    """
    Summary : 读取txt文件，返回列表。
              param / type / descrption
    Input   : path / [type] / [description]
    Output  : content / [type] / [description]
    """
    content = read_file(path)
    return content.split('\n') if content else None


def read_file_by_path(path):
    """
    Summary : 根据文件路径读取文件内容，并根据文件后缀名选择相应的解析函数。
              param / type / descrption
    Input   : path / [type] / [description]
    Output  : content / [type] / [description]
    """
    dir_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(dir_path, path)
    
    if path.endswith('.json'):
        return read_json(full_path)
    elif path.endswith('.yaml') or path.endswith('.yml'):
        return read_yaml(full_path)
    elif path.endswith('.ini'):
        return read_ini(full_path)
    elif path.endswith('.txt'):
        return read_txt(full_path)
    else:
        return read_file(full_path)

def main()->None:

    # 从此文件的上一级文件夹中读取settings文件夹中的配置文件
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    print(f"dir_path: {dir_path}")
    setting_path = os.path.join(dir_path, 'settings')
    print(f"setting_path: {setting_path}")

    # 判断settings文件夹是否存在
    if not os.path.exists(setting_path):
        print(f"settings文件夹不存在，请检查路径是否正确。")
        return
    
    # 读取data文件夹中的指定文件
    file_name = 'data1.xlsx'
    file_path = os.path.join(setting_path, file_name)
    config = read_file_by_path(file_path)
    print(f"config:\n{config}")
    
if __name__ == '__main__':
    main()