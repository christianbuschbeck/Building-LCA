# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:16:25 2022

@author: cbuschbeck
"""
import os
import shutil

def copy_files(src,dest):

    
    for f in os.listdir(dest):
        os.remove(os.path.join(dest, f))
    
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
            
            

      
        
