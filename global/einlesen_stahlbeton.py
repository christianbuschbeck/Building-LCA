# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:19:19 2020

@author: cbuschbeck
"""

def einlesen_stahlbeton():

    import pandas as pd
    import numpy as np
    import re
    ### Components ####
    
    #Tragwerk#
    tragwerk = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Stahlbeton/Tragwerksstützenliste-Vergleichsmodell.csv',sep= ';',header=[0],engine = "python")
    
    tragwerk_con = tragwerk
    tragwerk_con_vol=[]
    
    tragwerk_stahl_kg = []
    
    
    for i in range(1,len(tragwerk_con.index)):
        tragwerk_con_vol.append(float(tragwerk_con.loc[i,"Anzahl"]) * float(re.findall("\d+\.\d+",tragwerk_con.loc[i,"Volumen"])[0]))
        tragwerk_stahl_kg.append(float(tragwerk_con.loc[i,"Anzahl"]) * float(re.findall("\d+\.\d+",tragwerk_con.loc[i,"Volumen"])[0])* 65)
    
    #Decke
    decke = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Stahlbeton/Geschossdecken-Liste-Vergleichsmodell.csv',sep= ';',header=[0],engine = "python")
    
    decke_con = decke
    decke_con_vol=[]
    
    decke_stahl_kg = []
    
    for i in range(1,len(decke_con.index)):
        decke_con_vol.append(float(decke_con.loc[i,"Anzahl"]) * float(re.findall("\d+\.\d+",decke_con.loc[i,"Volumen"])[0]))
        decke_stahl_kg.append(float(decke_con.loc[i,"Anzahl"]) * float(re.findall("\d+\.\d+",decke_con.loc[i,"Volumen"])[0])* float(re.findall("\d+\ ",decke_con.loc[i,"Bewehrungsanteil Geschätzt"])[0]) )
    
    
    #wand

    wand = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Stahlbeton/Wandliste- Vergleichsmodell.csv',sep= ';',header=[0],engine = "python")
    
    wand_con = wand
    wand_con_vol=[]
    wand_stahl_kg=[]
    
    for i in range(1,len(wand_con.index)):
        wand_con_vol.append(float(wand_con.loc[i,"Anzahl"]) * float(re.findall("\d+\.\d+",wand_con.loc[i,"Volumen"])[0]))
        wand_stahl_kg.append(float(wand_con.loc[i,"Anzahl"]) * float(re.findall("\d+\.\d+",wand_con.loc[i,"Volumen"])[0]) * float(re.findall("\d+\ ",wand_con.loc[i,"Geschätzter Bewehrungsanteil"])[0]))
    
        
        
    con_vol = np.nansum(tragwerk_con_vol) + np.nansum(decke_con_vol) + np.nansum(wand_con_vol) 
    stahl_kg =  np.nansum(decke_stahl_kg) + np.nansum(wand_stahl_kg) 
    stahl_vol = stahl_kg / 7850 
    
    con_vol = con_vol - stahl_vol
    
    
    con_gebaeude_in = con_vol
    con_gebaeude_out = con_vol
    
    stahl_gebaeude_in = stahl_kg
    stahl_gebaeude_out= stahl_kg
    
    
    ### Services ####
    #aufwand = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/aufwandswerte.csv',sep= ';',header=[0],engine = "python")
    
    stuetze_gebaeude_in =  np.nansum(tragwerk.loc[:,"Länge"]/1000*tragwerk.loc[:,"Anzahl"]) #!!!  Im moment nur noch drin wegen komma fehler des BIMs  -> in lfm
    decke_gebaeude_in   =     sum(([float(re.findall("\d+\.\d+",i)[0]) for i in decke.loc[:,"Fläche"].tolist()])*decke.loc[:,"Anzahl"]) #in m2
    wand_gebaeude_in    =      sum(([float(re.findall("\d+\.\d+",i)[0]) for i in wand.loc[:,"Fläche"].tolist()])*wand.loc[:,"Anzahl"])  #in m2

    stuetze_gebaeude_out =   sum(([float(re.findall("\d+\.\d+",i)[0]) for i in tragwerk.loc[:,"Volumen"].tolist()])*tragwerk.loc[:,"Anzahl"]) # in m3
    decke_gebaeude_out   =   sum(([float(re.findall("\d+\.\d+",i)[0]) for i in decke.loc[:,"Volumen"].tolist()])*decke.loc[:,"Anzahl"])         # in m3
    wand_gebaeude_out    =      sum(([float(re.findall("\d+\.\d+",i)[0]) for i in wand.loc[:,"Volumen"].tolist()])*wand.loc[:,"Anzahl"])         # in m3  
    
    
   ###  Austausch ###
    
    con_austausch        = 0
    stahl_austausch      = 0
    stuetze_austausch    = 0
    decke_austausch      = 0 
    wand_austausch       = 0 
    
    
    ### Umbau ###
    
    con_umbau_in       = con_gebaeude_in
    stahl_umbau_in     = stahl_gebaeude_in
    stuetze_umbau_in   = stuetze_gebaeude_in
    decke_umbau_in     = decke_gebaeude_in 
    wand_umbau_in      = wand_gebaeude_in 
    
    con_umbau_out      = con_gebaeude_out
    stahl_umbau_out    = stahl_gebaeude_out
    stuetze_umbau_out  = stuetze_gebaeude_out
    decke_umbau_out    = decke_gebaeude_out 
    wand_umbau_out     = wand_gebaeude_out 
    
    con_huelle     = 0
    stahl_huelle   = 0 
    stuetze_huelle = 0
    decke_huelle   = 0
    wand_huelle    = 0
    
    
    data = {'concrete' :["m³" , con_gebaeude_in    , con_austausch     , con_umbau_out     , con_umbau_in     , con_gebaeude_out ,  con_huelle],
            "bew"     :["kg" , stahl_gebaeude_in  , stahl_austausch   , stahl_umbau_out   , stahl_umbau_in   , stahl_gebaeude_out , stahl_huelle],
            'stuetze'  :['lfm | m³', stuetze_gebaeude_in, stuetze_austausch , stuetze_umbau_out , stuetze_umbau_in , stuetze_gebaeude_out , stuetze_huelle],
            'decke'    :['m2 | m³' , decke_gebaeude_in  , decke_austausch   , decke_umbau_out   , decke_umbau_in   , decke_gebaeude_out , decke_huelle],
            'wand'     :['m2 | m³' , wand_gebaeude_in   , wand_austausch    , wand_umbau_out    , wand_umbau_in    , wand_gebaeude_out , wand_huelle],
            
            "phase"  : [""   ,"gebaeude_in"       , "austausch"       , "umbau_out"       , "umbau_in"      , "gebaeude_out"           ,  "huelle"]
            }
    
    BIM = pd.DataFrame(data, columns = ["concrete","bew","stuetze","decke","wand","phase"])  
    
    
    return(BIM)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


