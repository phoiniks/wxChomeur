#!/usr/bin/python3
#-*- coding: utf-8 -*-

import locale
import logging
import os
from os.path import basename, exists, splitext
from pathlib import Path
import re
from shutil import copy, move
import sys
from time import strftime, sleep

import csv
from glob import glob
from pprint import pprint
import sqlite3
import yaml

from jinja2 import Template, Environment, FileSystemLoader
from redis import Redis
import MySQLdb


programm = sys.argv[0]

base = splitext(basename(programm))[0].upper()
logbuch = base + ".LOG"
db = base + ".DB"
csvDatei = base + ".CSV"

logging.basicConfig(filename = logbuch, level = logging.DEBUG, format = '%(name)s %(asctime)s %(message)s %(funcName)s %(lineno)d')
log = logging.getLogger("DEBUG")

locale.setlocale(locale.LC_ALL, '')

lokalzeit = strftime('%A_%d_%B_%Y_%H:%M:%S')

class BewerbungPDF(dict):
    
    def __init__(self):
        self.firma = ""
        self.bezeichnung = ""
        self.strasse = ""
        self.plz = ""
        self.ort = ""
        self.anrede = ""
        self.ansprechpartner = ""
        self.quelle = ""
        self.ergebnis = ""
        self.template = ""
        self.zeugnisse = ""
        self.tex = ""
        self.user = ""
        self.password = ""
        self.db = ""


    def mkConnectData(self):
        with open("connect.txt") as datei:
            stripper = lambda a: a.strip()
            credentials = list(map(stripper, datei.readlines()))

            self.user     = credentials[0]
            self.password = credentials[1]
            self.db       = credentials[2]
            
        
    def mkDict(self):
        con = MySQLdb.connect(host     = 'localhost',
                              user     = self.user,
                              password = self.password,
                              db       = self.db)

        cur = con.cursor()
        
        select = "SELECT bezeichnung, firma, anrede, ansprechpartner, strasse, plz, ort, quelle FROM bewerbungen ORDER BY id DESC LIMIT 1"
        
        cur.execute(select)
    
        row = list(cur.fetchone())

        self.bezeichnung     = row[0]
        self.firma           = row[1]
        self.anrede          = row[2]
        self.ansprechpartner = row[3]
        self.strasse         = row[4]
        self.ort             = row[5] + " " + row[6]
        self.quelle          = row[7]


        self.dictionary = {
            'bezeichnung':    self.bezeichnung,
            'firma':          self.firma,
            'anrede':         self.anrede,
            'ansprechpartner':self.ansprechpartner,
            'strasse':        self.strasse,
            'ort':            self.ort,
            'quelle':         self.quelle,
        }

        pprint(self.dictionary)


    def fillInTemplate(self):
        template = self.firma.split()[0]
        log.debug(template)
        template += ".tex"
        
        with open(template) as text:
            templatestring = text.read()
            template       = Template(templatestring)

        templatetext = template.render(self.dictionary)

        templatetext = re.sub(" & Co.", " \& Co.", templatetext)

        self.firma   = re.sub("&", "\\&", self.firma)
        self.vorgang = self.firma.split()[0] + "_" + lokalzeit
        self.vorgang = re.sub(" ", "_", self.vorgang)
        self.tex     = self.vorgang + ".tex"
        self.pdf     = self.vorgang + ".pdf"

        with open(self.tex, "w") as ausgabe:
            ausgabe.write(templatetext)


    def mkPDF(self):
        cmd = "/usr/bin/pdflatex "
        cmd += self.tex
        os.system(cmd)
        sleep(1)
        try:
            cmd = "/usr/bin/pdftk.pdftk-java " + self.pdf\
            + " " + sys.argv[1]+ " " + sys.argv[2] + " "\
            + " cat output " +  self.pdf.split('_')[0].upper() + ".PDF"
            os.system(cmd)
        except(IndexError):
            print("Bitte eine Lebenslaufdatei sowie eine Zeugnissuite auswählen!")

            
log.debug("BEGINN")


if __name__ == "__main__":

    bewerbung = BewerbungPDF()
    bewerbung.mkConnectData()
    bewerbung.mkDict()
    bewerbung.fillInTemplate()
    bewerbung.mkPDF()
    
        
log.debug("ENDE")
