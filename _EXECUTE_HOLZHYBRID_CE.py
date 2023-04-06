# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:09:29 2020

@author: cbuschbeck
"""

import sys
sys.path.append("C:/Schaffeschaffe/Holzhybrid/skripte/global/")
#from RUNALL import runall
from calculate_building import calculate_building

import pandas as pd
import os
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



#######################
##     Szenario     ###
#######################
    
#Welche Bauteile werden betrachtet ?
zirkulierbar = ["lvl","osb","timb","concrete","verb","bew","glas","wool","fibre","gips"]

comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0, delimiter=";", quoting = 3)
all_component_names = comp.columns[1:len(comp.columns)]
selection_component_names = [""]#zirkulierbar

#Wie können die Bauteile rückgebaut werden ?
comp.loc[comp.loc[:,"vars"]=="rueckbau",all_component_names] = 0

for c in zirkulierbar:   
    
    comp.loc[comp.loc[:,"vars"]=="rueckbau1",c] = 0
    comp.loc[comp.loc[:,"vars"]=="rueckbau2",c] = 0
    if BIM.loc[umbau_out,c] > 0:
        comp.loc[comp.loc[:,"vars"]=="rueckbau1",c] = BIM.loc[umbau_out,c+"_rb"] / BIM.loc[umbau_out,c]
    if BIM.loc[gebaeude_out,c] > 0:
        comp.loc[comp.loc[:,"vars"]=="rueckbau2",c] = BIM.loc[gebaeude_out,c+"_rb"] / BIM.loc[gebaeude_out,c]


#Welche services werden betrachtet ?      -> Keine da selben wie im Linearen -> wird kopiert
serv = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/services.csv',sep= ';',engine="python",index_col=False, header=0, delimiter=";", quoting = 3)
all_services_names = serv.columns[1:len(serv.columns)]
selection_bauservices_names = [""] 
selection_energieservices_names =[""]

#Welches Szenario wird betrachtet ?
comp.loc[comp.loc[:,"vars"]=="kaskade",all_component_names] = 0
comp.loc[comp.loc[:,"vars"]=="sekundaer",all_component_names] = 0
comp.loc[comp.loc[:,"vars"]=="CE",all_component_names] = 1
comp.loc[comp.loc[:,"vars"]=="val",all_component_names] = 0
comp.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv",index=False,sep=";")

#Aufwandswerte 
aufwand_aufbau = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/aufwandswerte_aufbau_holz.csv',sep= ';',header=[0],engine = "python")
aufwand_abbau = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/aufwandswerte_abbau_holz.csv',sep= ';',header=[0],engine = "python")

"""
#Modulauswahl
moduleselection = ["A1-A3","B5_in","B5_out","C3","C4"]
#moduleselection = ["C4"]
#######################
## Calculation      ###
#######################
#Welches Szenario wird betrachtet ?
comp.loc[comp.loc[:,"vars"]=="sekundaer",zirkulierbar] = (2-1)/2
comp.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv",index=False,sep=";")
wd_grob = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Zirk_n_2/zirkulierbar/"

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


comp.loc[comp.loc[:,"vars"]=="sekundaer",zirkulierbar] = (3-1)/3
comp.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv",index=False,sep=";")
wd_grob = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Zirk_n_3/zirkulierbar/"

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

comp.loc[comp.loc[:,"vars"]=="sekundaer",zirkulierbar] = (4-1)/4
comp.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv",index=False,sep=";")
wd_grob = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Zirk_n_4/zirkulierbar/"

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


comp.loc[comp.loc[:,"vars"]=="sekundaer",zirkulierbar] = (5-1)/5
comp.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv",index=False,sep=";")
wd_grob = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Zirk_n_5/zirkulierbar/"

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
"""
####################
####  Copy Files  ##
####################

for n in range(2,6):

    hh_ce_folder = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Zirk_n_" + str(n) + "/"

    zirk_folder = hh_ce_folder + "zirkulierbar/"
    
    for fold in zirkulierbar + ["_scen"]:
        
        for file in os.listdir(zirk_folder+fold):
            #os.remove(os.path.join(hh_ce_folder+fold+"/", file))
            shutil.copy(src= zirk_folder+fold+"/"+file, dst= hh_ce_folder+fold+"/"+file)
        


time_end =   time.time() 

print((time_end - time_start)/(60*60))  # in Stunden
