# -*- encoding: UTF-8 -*-
'''
@filename    : package.py
@description : 自定义常用的函数
@time        : 2024/12/19
@author      : SomeoneLearning
'''

import os
import numpy as np
import pandas as pd


def read_data(file_path:str)->pd.DataFrame:
    """
    Summary : 读取excel数据,根据文件后缀,自动识别文件类型。
              param / type / descrption
    Input   : file_path / [str] / [文件路径]
    Output  : data / [DataFrame] / [读取的数据]
    """
    if not os.path.exists(file_path):
        print(f"文件{file_path}不存在，请检查路径是否正确。")
        return
    file_suffix = os.path.splitext(file_path)[1]
    if file_suffix == '.csv':
        return pd.read_csv(file_path , coding='gbk')
    elif file_suffix == '.xls' or file_suffix == '.xlsx':
        return pd.read_excel(file_path)
    else:
        print(f"不支持的文件类型{file_suffix}，请检查文件后缀是否正确。")
        return


def process_data(data:pd.DataFrame)->pd.DataFrame:
    """
    Summary : 处理excel数据,包括去除无效数据、去除重复数据、重命名列名、转换数据列的
              格式、重置索引等操作。
              param / type / descrption
    Input   : data / [DataFrame] / [原数据]
    Output  : data / [DataFrame] / [处理后的数据]
    """

    # 去除无效数据
    data = data.dropna()
    # 去除重复数据
    data = data.drop_duplicates()
    # 重命名列名
    rename_cols = {'日期':'日期', '时间':'时间', '压力(MPa)':'压力', '流量(m^3/h)':'流量'}
    data = data.rename(columns=rename_cols)
    # data.columns = ['日期', '时间', '压力', '流量']
    # 转换数据列的格式
    data['压力'] = data['压力'].astype(float)
    data['流量'] = data['流量'].astype(float)
    # 重置索引
    data = data.reset_index(drop=True)

    return data

# 定义函数，从data文件夹中读取所有excel文件，并处理数据
def read_all_data(folder_path:str)->pd.DataFrame:
    """
    Summary : 读取文件夹中的所有excel文件，并处理数据，返回DataFrame对象。
              param / type / descrption
    Input   : folder_path / [str] / [文件夹路径]
    Output  : data / [DataFrame] / [处理后的数据]
    """
    
    # 读取文件夹中的所有excel文件
    file_list = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.xlsx')]
    # 读取所有excel文件，并合并
    data = pd.concat([pd.read_excel(os.path.join(folder_path, file_name)) for file_name in file_list])
    # 处理数据
    data = process_data(data)
    return data


def main()->None:
    
    # 从此文件的上一级文件夹中读取data文件夹中的数据
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    data_path = os.path.join(dir_path, 'data')
    print(f"data_path: {data_path}")
    # 判断data文件夹是否存在
    if not os.path.exists(data_path):
        print(f"data文件夹不存在，请检查路径是否正确。")
        return
    
    # 读取data文件夹中的指定文件
    file_name = 'data1.xlsx'
    file_path = os.path.join(data_path, file_name)
    data = read_data(file_path)
    print(f"data:\n{data}")

if __name__ == '__main__':
    main()