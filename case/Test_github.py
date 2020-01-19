#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xiaxiwei

class Testb():
    def testb(self):
        s=int(input('请输入一个数'))
        if s>0 and s<=10:
            print('整数里小于10')
        elif s>=10:
            print('大于10的整数')
        else:
            print('输入的数小于0')

