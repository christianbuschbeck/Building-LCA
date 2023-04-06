# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:26:59 2020

@author: cbuschbeck
"""
import sys
import os

home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
sys.path.append(home_dir)
import olca
#In openLCA: Tools -> Entwicklerwerkzeuge -> IPC server
client = olca.Client(8080)

def calculate_res(processname, ECOINV=True,OEKOBDT=False,wd=False,filename=False):
    
    
    if wd==False:
        print("need wd -.-")
    os.chdir(wd)
    if filename == False:
        filename = processname
    
    setup = olca.CalculationSetup()
    setup_oekobdt = olca.CalculationSetup()
    
    
    setup.calculation_type = olca.CalculationType.CONTRIBUTION_ANALYSIS
    setup_oekobdt.calculation_type = olca.CalculationType.CONTRIBUTION_ANALYSIS
        
    if ECOINV == True:
        #setup.impact_method = client.get(olca.ImpactMethod,client.find(olca.ImpactMethod,"EN15804 all indicators ").id) #EN15804_A1_2020
        #setup.impact_method = client.get(olca.ImpactMethod,client.find(olca.ImpactMethod,"EN15804_A1_2020").id) #EN15804_A1_2020
        setup.impact_method = client.get(olca.ImpactMethod,client.find(olca.ImpactMethod,"EN15804_A2_2020_3").id) #EN15804_A1_2020
        
        
        setup.product_system = client.find(olca.ProductSystem, processname)
        result = client.calculate(setup)
        client.excel_export(result, filename+'.xlsx')
        client.dispose(result)

    if OEKOBDT == True:
        setup_oekobdt.impact_method = client.get(olca.ImpactMethod,client.find(olca.ImpactMethod,"EN 15804:2012 - Alle").id)
        setup_oekobdt.product_system = client.find(olca.ProductSystem, processname)
        result_oekobdt = client.calculate(setup_oekobdt)
        client.excel_export(result_oekobdt, filename+'_oekobdt.xlsx')
        client.dispose(result)
    
    print("calculated:"+processname)
    
    
    