# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:19:19 2020

@author: cbuschbeck
"""

def einlesen_holzhybrid():

    import pandas as pd
    import numpy as np
    
    ### Components ####
    
    #Tragwerk#
    tragwerk = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Tragwerksstuetzenliste.csv',sep= ';',skiprows = [0],header=[0],engine = "python")
    
    tragwerk_lvl = tragwerk[tragwerk.loc[:,"Familie"]== "Baubuche Stütze"]
    tragwerk_lvl_vol=[]
    for i in range(1,len(tragwerk_lvl.index)):
        tragwerk_lvl_vol.append(float(tragwerk_lvl.loc[i,"Anzahl"]) * float(tragwerk_lvl.loc[i,"Volumen [m³]"]))
    
    
    #Decke
    decke = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Geschossdeckenliste.csv',sep= ';',header=[0],engine = "python")
    
    decke_bsh = decke[decke.loc[:,"Tragendes Material: Beschreibung"]== "Baubuche S (Test)"]
    decke_lvl = decke[decke.loc[:,"Tragendes Material: Beschreibung"]== "Brettsperrholz"]
    
    decke_bsh_vol=[]
    decke_lvl_vol=[]
    for i in range(1,len(decke_bsh.index)):
        decke_bsh_vol.append(float(decke_bsh.loc[i,"Anzahl"]) * float(decke_bsh.loc[i,"Volumen [m³]"]))
    for i in range(1,len(decke_lvl.index)):
       decke_lvl_vol.append(float(decke_lvl.loc[i,"Anzahl"]) * float(decke_lvl.loc[i,"Volumen [m³]"]))
    
    #Wände
    wand = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Wandliste.csv',sep= ';',header=[0],engine = "python")
    wand_bsh = wand[wand.loc[:,"Bauelement"]== "Brettsperrholzwand"]
    wand_bsh_vol=[]
    for i in range(1,len(wand_bsh.index)):
        wand_bsh_vol.append(float(wand_bsh.loc[i,"Anzahl"]) * float(wand_bsh.loc[i,"Volumen [m³]"]))
   
    
    #Verbindungen
    verb = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Tragwerksverbindungen.csv',sep= ';',header=[0],engine = "python")
    verb_verb = verb[verb.loc[:,"Beschreibung"]== "Passverb"]
    verb_verb_stahl = verb_verb[verb_verb.loc[:,"Material main"]== "Steel"]
    verb_verb_stahl_kg =[]
    for i in range(0,len(verb_verb_stahl.index)):
        verb_verb_stahl_kg.append(float(verb_verb_stahl.loc[i,"Gewicht"]))
    
    
    lvl_gebaeude_in = np.nansum(tragwerk_lvl_vol) + np.nansum(decke_lvl_vol)
    bsh_gebaeude_in = np.nansum(decke_bsh_vol) + np.nansum(wand_bsh_vol)
    verb_gebaeude_in = np.nansum(verb_verb_stahl_kg)
        
    
    ### Services ####
    #aufwand = pd.read_csv('C:/Schaffeschaffe/Holzhybrid/daten/forprogramming/aufwandswerte.csv',sep= ';',header=[0],engine = "python")
    
    stuetze_gebaeude_in =  np.nansum(tragwerk.loc[:,"Länge [m]"]/1000*tragwerk.loc[:,"Anzahl"]) #!!!  Im moment nur noch drin wegen komma fehler des BIMs
    decke_gebaeude_in = np.nansum(decke.loc[:,"Fläche [m²]"]*decke.loc[:,"Anzahl"])
    wand_gebaeude_in = np.nansum(wand.loc[:,"Fläche [m²]"]*wand.loc[:,"Anzahl"])
    
    ###  Austausch ###
    
    lvl_austausch        = 0
    bsh_austausch        = 0
    verb_austausch       = 0
    stuetze_austausch    = 0
    decke_austausch      = 0 
    wand_austausch       = 0 
    
    
    ### Umbau ###
    
    lvl_umbau_in        = 1/4 * lvl_gebaeude_in
    bsh_umbau_in        = 1/4 * bsh_gebaeude_in
    verb_umbau_in       = 1/4 * verb_gebaeude_in
    stuetze_umbau_in    = 1/4 * stuetze_gebaeude_in
    decke_umbau_in      = 1/4 * decke_gebaeude_in 
    wand_umbau_in       = 1/4 * wand_gebaeude_in 
    
    lvl_umbau_out        = 1/8 * lvl_gebaeude_in
    bsh_umbau_out        = 1/8 * bsh_gebaeude_in
    verb_umbau_out       = 1/8 * verb_gebaeude_in
    stuetze_umbau_out    = 1/8 * stuetze_gebaeude_in
    decke_umbau_out      = 1/8 * decke_gebaeude_in 
    wand_umbau_out       = 1/8 * wand_gebaeude_in 
    
    ### EOL ###
    
    lvl_gebaeude_out     = lvl_gebaeude_in + lvl_umbau_in - lvl_umbau_out
    bsh_gebaeude_out     = bsh_gebaeude_in + bsh_umbau_in - bsh_umbau_out
    verb_gebaeude_out    = verb_gebaeude_in + verb_umbau_in - verb_umbau_out
    stuetze_gebaeude_out = stuetze_gebaeude_in + stuetze_umbau_in - stuetze_umbau_out
    decke_gebaeude_out   = decke_gebaeude_in + decke_umbau_in - decke_umbau_out
    wand_gebaeude_out    = wand_gebaeude_in + wand_umbau_in - wand_umbau_out
    
    lvl_huelle = 200
    bsh_huelle = 400
    verb_huelle = 0
    stuetze_huelle = 0
    decke_huelle = 0
    wand_huelle = 0
    
    data = {'lvl'    :["m³"  , lvl_gebaeude_in    , lvl_austausch     , lvl_umbau_out     , lvl_umbau_in     , lvl_gebaeude_out    , lvl_huelle],
            'bsh'    :["m³"  , bsh_gebaeude_in    , bsh_austausch     , bsh_umbau_out     , bsh_umbau_in     , bsh_gebaeude_out    , bsh_huelle],
            'verb'   :['kg'  , verb_gebaeude_in   , verb_austausch    , verb_umbau_out    , verb_umbau_in    , verb_gebaeude_out   , verb_huelle],
            
            'stuetze': ['lfm', stuetze_gebaeude_in, stuetze_austausch , stuetze_umbau_out , stuetze_umbau_in , stuetze_gebaeude_out, stuetze_huelle],
            'decke'  : ['m2' , decke_gebaeude_in  , decke_austausch   , decke_umbau_out   , decke_umbau_in   , decke_gebaeude_out  , decke_huelle],
            'wand'   : ['m2' , wand_gebaeude_in   , wand_austausch    , wand_umbau_out    , wand_umbau_in    , wand_gebaeude_out   , wand_huelle],
            
            "phase"  : [""   ,"gebaeude_in"       , "austausch"       , "umbau_out"       , "umbau_in"      , "gebaeude_out"       , "huelle"]
            }
    
    BIM = pd.DataFrame(data, columns = ['lvl',"bsh",'verb',"stuetze","decke","wand","phase","huelle"])  
    BIM.to_csv("C:/Schaffeschaffe/Holzhybrid/daten/Bauteile/Holzhybrid/BIM_HH.csv",index=False,sep=";")

    return(BIM)



