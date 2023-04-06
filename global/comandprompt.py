# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:27:22 2020

@author: cbuschbeck
"""
   
import subprocess, os
cmd = ["C:/jython2.7.2/bin/jython", "C:/Schaffeschaffe/Holzhybrid/skripte/global/create_productsystems.py"]

subprocess.check_output(cmd,env = os.environ)
