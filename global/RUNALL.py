# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:41:15 2020

@author: cbuschbeck
"""

#---------------------------------------- R U N   T H E   W H O L E   T H I N G ----------------------

PROC=False
PRODSYS = False
CALC = True
def runall(wd,modules,modulespath,GWP500=False,OEKOBDT=False,BIO=False,ECOINV=True,PROC=True,PRODSYS =True,CALC=True):
    
    
     import sys
    
     sys.path =    ['C:\\Users\\cbuschbeck\\Anaconda3\\python38.zip',
                    'C:\\Users\\cbuschbeck\\Anaconda3\\DLLs',
                    'C:\\Users\\cbuschbeck\\Anaconda3\\lib',
                    'C:\\Users\\cbuschbeck\\Anaconda3',
                    '',
                    'C:\\Users\\cbuschbeck\\Anaconda3\\lib\\site-packages',
                    'C:\\Users\\cbuschbeck\\Anaconda3\\lib\\site-packages\\win32',
                    'C:\\Users\\cbuschbeck\\Anaconda3\\lib\\site-packages\\win32\\lib',
                    'C:\\Users\\cbuschbeck\\Anaconda3\\lib\\site-packages\\Pythonwin',
                    'C:\\Users\\cbuschbeck\\Anaconda3\\lib\\site-packages\\IPython\\extensions',
                    'C:\\Users\\cbuschbeck\\.ipython']
     
     for p in ["A1-A3","A4","A5","B1","B2","B3","B4","B5","B6","B7","C1","C2","C3","C4","D"]:
         if modulespath+p not in sys.path:
             sys.path.append(modulespath+"/"+p+"/")
     
     
     import runpy
     home_dir = "C:/Users\cbuschbeck/AppData/Local/Programs/Python/Python38-32/Lib/site-packages"
     if home_dir not in sys.path:
         sys.path.append(home_dir)   
     import olca
     import pandas as pd
   
     client = olca.Client(8080)
 
     comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0, quoting = 3)
  
    
     #########################################
     ### Create Processes                  ####
     ##########################################
     if PROC == True:   
        for processname in modules:
            if client.find(olca.ProductSystem,processname):
                todelete= client.get(olca.ProductSystem,client.find(olca.ProductSystem,processname).id)
                todelete.olca_type = olca.schema.ProductSystem.__name__
                client.delete(todelete)
                
        ### Reparatur und Umbau braucht verschiedenes ###
        
        if "B4" in modules:
            modules = ["A1-A3","A4","A5","C1","C2","C3","C4","B4"]
                    
        if "B5_in" in modules:
            modules = ["A1-A3","A4","A5","B5_in"]
        
        if "B5_out" in modules:
            modules = ["C1","C2","C3","C4","B5_out"]
        
        
        ### A1.3 ###    
        if "A1-A3" in modules:
                      
            if float(comp.loc[comp.loc[:,"vars"]=="include","lvl"]) == 0:
                print("skip lvl")
            else:
                try:
                    runpy.run_module(mod_name="lvl_primaer") 
                except Exception as e:
                    print(e)    
                
                try:
                    runpy.run_module(mod_name="lvl_sekundaer")
                except Exception as e:
                    print(e)    
            
            if float(comp.loc[comp.loc[:,"vars"]=="include","bsh"]) == 0:
                print("skip bsh")
            else:
                try:    
                    runpy.run_module(mod_name="bsh_primaer")
                except Exception as e:
                    print(e)    
                
                try:    
                    runpy.run_module(mod_name="bsh_sekundaer")
                except Exception as e:
                    print(e)    

            if float(comp.loc[comp.loc[:,"vars"]=="include","timb"]) == 0:
                print("skip timb")
            else:
                try:    
                    runpy.run_module(mod_name="timb_primaer")
                except Exception as e:
                    print(e)    
                
                try:    
                    runpy.run_module(mod_name="timb_sekundaer")
                except Exception as e:
                    print(e)    

            if float(comp.loc[comp.loc[:,"vars"]=="include","osb"]) == 0:
                print("skip osb")
            else:
                try:    
                    runpy.run_module(mod_name="osb_primaer")
                except Exception as e:
                    print(e)    
                
                try:    
                    runpy.run_module(mod_name="osb_sekundaer")
                except Exception as e:
                    print(e)    

            
            if float(comp.loc[comp.loc[:,"vars"]=="include","verb"]) == 0:
                print("skip verb")
            else:            
                try:
                    runpy.run_module(mod_name="verb_primaer")
                except Exception as e:
                    print(e)    
                       
                try:
                    runpy.run_module(mod_name="verb_sekundaer")
                except Exception as e:
                    print(e)    
            
            if float(comp.loc[comp.loc[:,"vars"]=="include","concrete"]) == 0:
                print("skip con")
            else:            
                try:    
                    runpy.run_module(mod_name="con_primaer")
                except Exception as e:
                    print(e)    
            
                try:    
                    runpy.run_module(mod_name="con_sekundaer")
                except Exception as e:
                    print(e)    
 
            
            if float(comp.loc[comp.loc[:,"vars"]=="include","glas"]) == 0:
                print("skip glas")
            else:            
                try:    
                    runpy.run_module(mod_name="glas_primaer")
                except Exception as e:
                    print(e)    
 
                try:    
                    runpy.run_module(mod_name="glas_sekundaer")
                except Exception as e:
                    print(e)    

            if float(comp.loc[comp.loc[:,"vars"]=="include","bew"]) == 0:
                print("skip bew")
            else:            
                try:    
                    runpy.run_module(mod_name="bew_primaer")
                except Exception as e:
                    print(e)    
 
                try:    
                    runpy.run_module(mod_name="bew_sekundaer")
                except Exception as e:
                    print(e)    


            if float(comp.loc[comp.loc[:,"vars"]=="include","gips"]) == 0:
                print("skip gips")
            else:            
                try:    
                    runpy.run_module(mod_name="gips_primaer")
                except Exception as e:
                    print(e)    
 
                try:    
                    runpy.run_module(mod_name="gips_sekundaer")
                except Exception as e:
                    print(e)    


            if float(comp.loc[comp.loc[:,"vars"]=="include","wool"]) == 0:
                print("skip wool")
            else:            
                try:    
                    runpy.run_module(mod_name="wool_primaer")
                except Exception as e:
                    print(e)    
 
                try:    
                    runpy.run_module(mod_name="wool_sekundaer")
                except Exception as e:
                    print(e)    

            if float(comp.loc[comp.loc[:,"vars"]=="include","lehm"]) == 0:
                print("skip lehm")
            else:            
                try:    
                    runpy.run_module(mod_name="lehm_primaer")
                except Exception as e:
                    print(e)    
 
                try:    
                    runpy.run_module(mod_name="lehm_sekundaer")
                except Exception as e:
                    print(e)    


    
            if float(comp.loc[comp.loc[:,"vars"]=="include","hp"]) == 0:
                print("skip hp")
            else:            
                try:    
                    runpy.run_module(mod_name="hp")
                except Exception as e:
                    print(e)    
            
            if float(comp.loc[comp.loc[:,"vars"]=="include","elev"]) == 0:
                print("skip elev")
            else:            
                try:    
                    runpy.run_module(mod_name="elev")
                except Exception as e:
                    print(e)    
            
            if float(comp.loc[comp.loc[:,"vars"]=="include","pv"]) == 0:
                print("skip pv")
            else:            
                try:    
                    runpy.run_module(mod_name="pv")
                except Exception as e:
                    print(e)    
            
           
            
            try:
                runpy.run_module(mod_name="A1_A3")
            except Exception as e:
                print(e)    
            
            print("process created: A1-A3")
        
        ### A4 ###
        if "A4" in modules:
            try:
                runpy.run_module(mod_name="A4")
            except Exception as e:
                print(e)
            
            print("process created: A4")
        
        ### A5 ###
        
        if "A5" in modules:
            
            try:
                runpy.run_module(mod_name="A5")
            except Exception as e:
                print(e)    
            
            print("process created: A5")
        
        ### B1 ###
        
        if "B1" in modules:
            if float(comp.loc[comp.loc[:,"vars"]=="include","concrete"]) > 0:
                try:
                    runpy.run_module(mod_name="B1")
                except Exception as e:
                    print(e)    

        ### B2 ###
        if "B2" in modules:
            if float(comp.loc[comp.loc[:,"vars"]=="include","osb"]) > 0:
                try:
                    runpy.run_module(mod_name="B2")
                except Exception as e:
                    print(e)    

         
        ### B6 ###
        
        if "B6_wohn" in modules or "B6_park" in modules :
            
            try:
                runpy.run_module(mod_name="B6")
            except Exception as e:
                print(e)    
                
            print("process created: B6")


        ### C1 ###
        
        if "C1" in modules:
            
            try:
                runpy.run_module(mod_name="C1")
            except Exception as e:
                print(e)    
            
            print("process created: C1")
        

            
        ### C2 ###
        
        if "C2" in modules:
            
            try:
                runpy.run_module(mod_name="C2")
            except Exception as e:
                print(e)    
            
            print("process created: C2")
        
        ### C3 ###
        
        if "C3" in modules:
            
           
            try:
                runpy.run_module(mod_name="C3")
            except Exception as e:
                print(e)    
            
        
        
            print("process created: C3")
        
        ### C4 ###
        
        if "C4" in modules:
            
          
            try:
                runpy.run_module(mod_name="C4")
            except Exception as e:
                print(e)    
            
            print("process created: C4")
        
        
        ### D ###
        
        if "D_e_g" in modules or "D_e_k" in modules: 
            
         
            try:
                runpy.run_module(mod_name="D_energie")
            except Exception as e:
                print(e)    
            
            print("process created: D_e")
            
        if "D_s_g" in modules or "D_s_k" in modules:     
            
           
            try:
                runpy.run_module(mod_name="D_stoff")
            except Exception as e:
                print(e)    
            
            print("process created: D_s")
        
        if "D_w_g" in modules or "D_w_k" in modules:     
            
            try:
                runpy.run_module(mod_name="D_wieder")
            except Exception as e:
                print(e)    
               
          
            print("process created: D_w")
            

        ### B4 ###
        
        if "B4" in modules:
            
            try:
                runpy.run_module(mod_name="B4")
            except Exception as e:
                print(e)    
            
            print("process created: B4")
            modules = ["B4"]
                

        ### B5 ###
        if "B5_in" in modules:
                        
            try:
                runpy.run_module(mod_name="B5_in")
            except Exception as e:
                print(e)    
            
            print("process created: B5_in")
            modules = ["B5_in"]
                
        if "B5_out" in modules:
                        
            try:
                runpy.run_module(mod_name="B5_out")
            except Exception as e:
                print(e)    
            
            print("process created: B5_out")
            modules = ["B5_out"]
            
    ##########################################
    ###     Create Productystems          ####
    ##########################################
     if PRODSYS == True:
         sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")
        
         from cps import cps_fun
        
         for i in modules:
             cps_fun(i)
    ##########################################
    ###     Calculate                     ####
    ##########################################
     if CALC == True:
         from calculate import calculate_res
        
         for i in modules:
             calculate_res(i,OEKOBDT=OEKOBDT,ECOINV=ECOINV,wd=wd)
        
