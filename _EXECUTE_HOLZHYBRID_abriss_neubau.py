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

### Choose Modules
modulespath = "C:/Schaffeschaffe/Holzhybrid/skripte/Model_new/Module"


#######################
##       BIM        ###
#######################

BIM = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Holzhybrid/BIM_hh_abriss.csv')

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
comp = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv',sep= ';',engine="python",index_col=False, header=0, delimiter=";", quoting = 3)
all_component_names = comp.columns[1:len(comp.columns)]
selection_component_names = all_component_names

#Wie können die Bauteile rückgebaut werden ?       -> Gar nicht

for c in all_component_names:   
    BIM.loc[:,c+"_rb"] = 0 

comp.loc[comp.loc[:,"vars"]=="rueckbau",all_component_names] = 0

#Welche services werden betrachtet ?
serv = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/services.csv',sep= ';',engine="python",index_col=False, header=0, delimiter=";", quoting = 3)
all_services_names = serv.columns[1:len(serv.columns)]
selection_bauservices_names = ["kran","bagger","werkzeug"]
selection_energieservices_names = ["strom"]

#Welches Szenario wird betrachtet ?
comp.loc[comp.loc[:,"vars"]=="kaskade",all_component_names] = 1
comp.loc[comp.loc[:,"vars"]=="sekundaer",all_component_names] = 0
comp.loc[comp.loc[:,"vars"]=="CE",all_component_names] = 0
comp.loc[comp.loc[:,"vars"]=="val",all_component_names] = 0
comp.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/components.csv",index=False,sep=";")

#Aufwandswerte 
aufwand_aufbau = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/aufwandswerte_aufbau_holz.csv',sep= ';',header=[0],engine = "python")
aufwand_abbau = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/aufwandswerte_abbau_holz.csv',sep= ';',header=[0],engine = "python")

#Modulauswahl

moduleselection = ["A1-A3","A4","A5","B1","B2","B4","B5_in","B5_out","B6_wohn","B6_park","C1","C2","C3","C4"]
#moduleselection = ["C4"]
#######################
## Calculation      ###
#######################
wd_grob = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Abriss/"

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

### Alles Fichte


wd_grob = "C:/Schaffeschaffe/Holzhybrid/results/Analyse/Gebaeude/HH_Abriss_Fichte/"

BIM.loc[gebaeude_in,"bsh"]   = BIM.loc[gebaeude_in,"bsh"] + BIM.loc[gebaeude_in,"lvl"]
BIM.loc[austausch,"bsh"]     = BIM.loc[austausch,"bsh"]   + BIM.loc[austausch,"lvl"]
BIM.loc[umbau_out,"bsh"]     = BIM.loc[umbau_out,"bsh"]   + BIM.loc[umbau_out,"lvl"]
BIM.loc[umbau_in,"bsh"]      = BIM.loc[umbau_in,"bsh"]    + BIM.loc[umbau_in,"lvl"]
BIM.loc[gebaeude_out,"bsh"]  = BIM.loc[gebaeude_out,"bsh"]+ BIM.loc[gebaeude_out,"lvl"]
BIM.loc[huelle,"bsh"]        = BIM.loc[huelle,"bsh"]      + BIM.loc[huelle,"lvl"]

BIM.loc[gebaeude_in,"lvl"]   = 0
BIM.loc[austausch,"lvl"]     = 0
BIM.loc[umbau_out,"lvl"]     = 0
BIM.loc[umbau_in,"lvl"]      = 0
BIM.loc[gebaeude_out,"lvl"]  = 0
BIM.loc[huelle,"lvl"]        = 0


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

