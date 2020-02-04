#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:31:49 2020

@author: ttumuon
"""

from matplotlib.ticker import StrMethodFormatter
import matplotlib.pyplot as plt
import numpy as np
import csv 

def removeLine(inputFileName, outputFileName, line_opener):
    input = open(inputFileName, "r")
    output = open(outputFileName, "w")
    output.write(input.readline())
    for line in input:
        if not line.lstrip().startswith(line_opener):
            output.write(line)
    input.close()
    output.close()


def read_data(fname, oname):
    all_muons = [] #mother array
    ind_muons = [] #daughter array
    steps = []
    part = [] #mu+ or mu-
    ke = []
    edep = [] 
    pos = [] # x,y,z as elements
    depth = [] 
    loc = []
    mvol = [] #mother volume
    status = []
    substr = "E" 
    
    with open(fname, "r+") as a:
        for line in a:
            if substr in line:
                line = line.split('\n')
                line = line[0]
                line = line.split('=')
                line = line[1]
                line = line.split(',')
           #     muon_id.append(int(line[0])) #event num
           #     num_pid.append(int(line[1])) #number of muons generated in event   
        removeLine(fname, oname, "E")
        
        print(line)       
    """          
    with open(fname,'r') as csvfile:
            event = csv.reader(csvfile, delimiter=',')
            for row in event:
                print(row)
    """
    
read_data('data_trial_control_20k.txt', 'processed_data_trial_control_20k.txt')