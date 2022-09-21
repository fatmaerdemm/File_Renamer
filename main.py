#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:29:16 2022

@author: fatmaerdem
"""
import os 

counter = 0
for file in os.listdir("text_files"):
    os.rename(f"text_files/{file}",f"text_files/fatma2-{counter}.txt")
    counter +=1

