# -*- coding: utf-8 -*-
"""
Created on 2020/5/20
@author : weibinwu
@file : middleware.py
"""
import sys
import subprocess


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv)
    subprocess.Popen(sys.argv[1], shell=True)
    sys.exit(0)

