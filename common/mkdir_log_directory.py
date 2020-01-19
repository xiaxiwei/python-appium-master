#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月28日

@author: li tao
"""
import os


def mk_dir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    is_exists = os.path.exists(path)

    # 判断结果
    if not is_exists:
        try:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
        except Exception as e:
            print(e)
    else:
        # 如果目录存在则不创建，并提示目录已存在
        pass
