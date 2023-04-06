# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:09:29 2020

@author: cbuschbeck
"""

import sys
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")
#from RUNALL import runall
from calculate_building import calculate_building
from copy_files import copy_files
import os
import pandas as pd
import shutil
import time
  
# ts stores the time in seconds
time_start = time.time()

### Choose Modules
modulespath = "C:/Schaffeschaffe/Holzhybrid/skripte/Model_new/Module"


#######################
##       BIM        ###
#######################

BIM = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Holzhybrid/BIM_hh.csv')
    
gebaeude_in  = BIM["phase"].tolist().index("gebaeude_in")
austausch    = BIM["phase"].tolist().index("austausch")
umbau_in     = BIM["phase"].tolist().index("umbau_in")
umbau_out    = BIM["phase"].tolist().index("umbau_out")
gebaeude_out = BIM["phase"].tolist().index("gebaeude_out")
huelle       = BIM["phase"].tolist().index("huelle")

BIM = BIM.fillna(0)

#######################
##     Szenario     ###
#######################

#Welche Bauteile werden betrachtet ?
zirkulierbar = ["lvl","bsh","osb","timb","fibre","concrete","verb","bew","glas","gips"]

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0, delimiter=";", quoting = 3)
all_component_names = comp.columns[1:len(comp.columns)]
selection_component_names = [""]#all_component_names # ["lvl","osb","timb","fibre","concrete","verb","bew","glas","gips","wool","lehm"]#all_component_names 

#Wie können die Bauteile rückgebaut werden ?
comp.loc[comp.loc[:,"vars"]=="rueckbau",all_component_names] = 0

for c in zirkulierbar:   
    
    comp.loc[comp.loc[:,"vars"]=="rueckbau1",c] = 0
    comp.loc[comp.loc[:,"vars"]=="rueckbau2",c] = 0
    if BIM.loc[umbau_out,c] > 0:
        comp.loc[comp.loc[:,"vars"]=="rueckbau1",c] = BIM.loc[umbau_out,c+"_rb"] / BIM.loc[umbau_out,c]
    if BIM.loc[gebaeude_out,c] > 0:
        comp.loc[comp.loc[:,"vars"]=="rueckbau2",c] = BIM.loc[gebaeude_out,c+"_rb"] / BIM.loc[gebaeude_out,c]
   
    
#Welche services werden betrachtet ?
serv = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/services.csv',sep= ';',engine="python",index_col=False, header=0, delimiter=";", quoting = 3)
all_services_names = serv.columns[1:len(serv.columns)]
selection_bauservices_names =  [""]#["kran","bagger","werkzeug"]
selection_energieservices_names = ["strom"]

#Welches Szenario wird betrachtet ?
comp.loc[comp.loc[:,"vars"]=="kaskade",all_component_names] = 0
comp.loc[comp.loc[:,"vars"]=="sekundaer",all_component_names] = 0
comp.loc[comp.loc[:,"vars"]=="CE",all_component_names] = 0
comp.loc[comp.loc[:,"vars"]=="val",all_component_names] = 0
comp.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv",index=False,sep=";")

#Aufwandswerte 
aufwand_aufbau = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/aufwandswerte_aufbau_holz.csv',sep= ';',header=[0],engine = "python")
aufwand_abbau = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/aufwandswerte_abbau_holz.csv',sep= ';',header=[0],engine = "python")


#Modulauswahl
#moduleselection = ["A1-A3","A4","A5","B1","B2","B4","B5_in","B5_out","B6_wohn","B6_park","C1","C2","C3","C4","D_w_g","D_w_k","D_s_g","D_s_k","D_e_k","D_e_g"]
moduleselection = ["B6_wohn","B6_park","D_e_g","D_e_k"]

#######################
## Calculation      ###
#######################
"""
### clear folders ###
for c in all_component_names.tolist()+all_services_names.tolist()+["_scen"]:
    dest= "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Lin/"+c
    for f in os.listdir(dest):
        os.remove(os.path.join(dest, f))
"""
#### clear scenarios ###
"""
d = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/"
for g in ["HH_Lin","HH_Zirk_n_1","HH_Zirk_n_2","HH_Zirk_n_3","HH_Zirk_n_4","HH_Zirk_n_5","SB","HH_Zirk_n_1","HH_Abriss"]:
    dest= d + g + "/_scen"
    for f in os.listdir(dest):
        os.remove(os.path.join(dest, f))
"""

wd_grob = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Lin/"

calculate_building(BIM=BIM,
                   comp=comp,
                   serv=serv,
                   all_component_names=all_component_names,
                   selection_component_names=selection_component_names,
                   all_services_names=all_services_names,
                   selection_bauservices_names=selection_bauservices_names,
                   selection_energieservices_names=selection_energieservices_names,
                   wd_grob=wd_grob,
                   modulespath=modulespath,
                   aufwand_abbau=aufwand_abbau,
                   aufwand_aufbau=aufwand_aufbau,
                   moduleselection=moduleselection)




#######################
## Kopieren         ###
#######################
"""
for c in all_component_names.tolist()+all_services_names.tolist()+["_scen"]:
    for n in range(1,6):
        copy_files("C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Lin/"+c, "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Zirk_n_" +str(n)+"/"+c )



time_end =   time.time() 

print((time_end - time_start)/(60*60))  # in Stunden
"""