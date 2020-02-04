#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:10:39 2020

@author: ttumuon
"""
arr = [(1, 'E=1,1\n'),
(10, 'E=2,1\n'),
(12, 'E=3,1\n'),
(58, 'E=4,2\n'),
(75, 'E=5,1\n'),
(92, 'E=6,1\n'),
(109, 'E=7,1\n'),
(111, 'E=8,1\n'),
(113, 'E=9,1\n'),
(137, 'E=10,1\n'),
(149, 'E=100,1\n'),
(149, 'E=10000,1')]


def string2num(st):
    st = st.split("\n")
    st = st[0]
    st = st.split("=")
    st = st[1]
    return st

for i in range(len(arr)):
    data = arr[i][1]
    print(string2num(data))


