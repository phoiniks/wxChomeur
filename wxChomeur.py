#!/usr/bin/python3
import wx
from sqlalchemy import *
from sqlalchemy.sql import func
from pprint import pprint
from collections import namedtuple


connect = ""
with open("connect.txt") as datei:
    connect = datei.readline()
    
metadata = MetaData(connect)


bewerbungen = Table(
    'bewerbungen', metadata,
    Column('id', Integer, primary_key=True),
    Column('bezeichnung', Unicode(255), unique=False, nullable=False),
    Column('firma', Unicode(128), unique=False, nullable=False),
    Column('ansprechpartner', Unicode(64), unique=True, nullable=True),
    Column('anrede', Unicode(4), unique=False, nullable=True),
    Column('strasse', Unicode(128), unique=False, nullable=False),
    Column('plz', Unicode(5), unique=False, nullable=False),
    Column('ort', Unicode(128), unique=False, nullable=False),
    Column('telefon', Unicode(32), unique=True, nullable=True),
    Column('mobil', Unicode(32), unique=True, nullable=True),
    Column('email', Unicode(128), unique=True, nullable=True),
    Column('website', Unicode(128), unique=True, nullable=True),
    Column('quelle', Unicode(128), unique=False, nullable=False),
    Column('ergebnis', Unicode(1024), unique=False, nullable=True),
    Column('zeit', Unicode(30), unique=True, nullable=False))


stmt = bewerbungen.select().order_by(bewerbungen.c.id.desc()).limit(1)

liste = []
for e in stmt.execute():
    liste = [str(el) for el in e]

namedtuple

print(" | ".join(liste))


class Reiter1(wx.Panel):
    def __init__(self, parent):
        super(Reiter1, self).__init__(parent)

        topLbl = wx.StaticText(self, -1, "Firmendaten")
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        
        bezeichnungLbl       = wx.StaticText(self, -1, "Bezeichnung:")
        self.bezeichnung     = wx.TextCtrl(self, -1, "");
        
        firmaLbl             = wx.StaticText(self, -1, "Firma:")
        self.firma           = wx.TextCtrl(self, -1, "")
        
        ansprLbl             = wx.StaticText(self, -1, "Ansprechpartner:")
        self.ansprechpartner = wx.TextCtrl(self, -1, "")

        anredeLbl            = wx.StaticText(self, -1, "Anrede:")
        self.anrede          = wx.TextCtrl(self, -1, "")
        
        adressLbl            = wx.StaticText(self, -1, "Straße, PLZ, Ort:")
        self.strasse         = wx.TextCtrl(self, -1, "", size=(150, -1))
        self.plz             = wx.TextCtrl(self, -1, "", size=(70, -1))
        self.ort             = wx.TextCtrl(self, -1, "", size=(150, -1))
        
        telefLbl             = wx.StaticText(self, -1, "Telefon (Festnetz):")
        self.telefon         = wx.TextCtrl(self, -1, "");
        
        mobilLbl             = wx.StaticText(self, -1, "Mobiltelefon:")
        self.mobil           = wx.TextCtrl(self, -1, "")
        
        emailLbl             = wx.StaticText(self, -1, "E-Mail:")
        self.email           = wx.TextCtrl(self, -1, "")
        
        webLbl               = wx.StaticText(self, -1, "Website:")
        self.website         = wx.TextCtrl(self, -1, "")
        
        quellLbl             = wx.StaticText(self, -1, "Quelle:")
        self.quelle          = wx.TextCtrl(self, -1, "")
        
        ergLbl               = wx.StaticText(self, -1, "Ergebnis:")
        self.ergebnis        = wx.TextCtrl(self, -1, "steht noch aus")
        
        speicherBtn = wx.Button(self, -1, "Speichern")
        self.Bind(wx.EVT_BUTTON, self.speichern, speicherBtn)
        
        beendeBtn = wx.Button(self, -1, "Beenden")
        self.Bind(wx.EVT_BUTTON, self.beenden, beendeBtn)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl, 0, wx.ALL, 9)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 9)
        
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(bezeichnungLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.bezeichnung, 0, wx.EXPAND)
        addrSizer.Add(firmaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.firma, 0, wx.EXPAND)
        addrSizer.Add(ansprLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.ansprechpartner, 0, wx.EXPAND)
        addrSizer.Add(anredeLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)        
        addrSizer.Add(self.anrede, 0, wx.EXPAND)

        addrSizer.Add(adressLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        adrSizer = wx.BoxSizer(wx.HORIZONTAL)
        adrSizer.Add(self.strasse, 1)
        adrSizer.Add(self.plz, 0, wx.LEFT|wx.RIGHT, 5)
        adrSizer.Add(self.ort)

        addrSizer.Add(adrSizer, 0, wx.EXPAND)
        addrSizer.Add(telefLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.telefon, 0, wx.EXPAND)
        addrSizer.Add(mobilLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.mobil, 0, wx.EXPAND)
        addrSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.email, 0, wx.EXPAND)
        addrSizer.Add(webLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.website, 0, wx.EXPAND)
        addrSizer.Add(quellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.quelle, 0, wx.EXPAND)
        addrSizer.Add(ergLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.ergebnis, 0, wx.EXPAND)
        
        mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)
        
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(speicherBtn, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(beendeBtn, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
        btnSizer.Add((20, 20), 1)
        
        mainSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 20)

        self.SetSizer(mainSizer)

        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

        
    def beenden(self, event):
        self.GetTopLevelParent().Close(True)


    def speichern(self, event):
        schluessel = "bezeichnung, firma, ansprechpartner, anrede, strasse, plz, ort, telefon, mobil, email, website, quelle, ergebnis"

        werte = ([self.bezeichnung.GetValue(), self.firma.GetValue(),\
                  self.ansprechpartner.GetValue(), self.anrede.GetValue(),\
                  self.strasse.GetValue(), self.plz.GetValue(),\
                  self.ort.GetValue(), self.telefon.GetValue(),\
                  self.mobil.GetValue(), self.email.GetValue(),\
                  self.website.GetValue(), self.quelle.GetValue(),\
                  self.ergebnis.GetValue()])

        werte = [wert.strip() for wert in werte]

        dictionary = dict(zip(schluessel.split(", "), werte))

        stmt = bewerbungen.insert()
        stmt.execute(dictionary)

        
class Reiter2(wx.Panel):
    def __init__(self, parent):
        super(Reiter2, self).__init__(parent)

        
class Reiter3(wx.Panel):
    def __init__(self, parent):
        super(Reiter3, self).__init__(parent)

        topLbl = wx.StaticText(self, -1, "Konfiguration")
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

        benutzerLbl = wx.StaticText(self, -1, "Benutzer:")
        self.benutzer = wx.TextCtrl(self, -1, "")

        passwortLbl = wx.StaticText(self, -1, "Passwort:")
        self.passwort = wx.TextCtrl(self, -1, "")

        datenbankLbl = wx.StaticText(self, -1, "Datenbank:")
        self.datenbank = wx.TextCtrl(self, -1, "")
        
        speicherBtn = wx.Button(self, -1, "Speichern")
        self.Bind(wx.EVT_BUTTON, self.speichern, speicherBtn)
        
        beendeBtn = wx.Button(self, -1, "Beenden")
        self.Bind(wx.EVT_BUTTON, self.beenden, beendeBtn)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl, 0, wx.ALL, 9)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 9)

        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(benutzerLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.benutzer, 0, wx.EXPAND)
        addrSizer.Add(passwortLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.passwort, 0, wx.EXPAND)
        addrSizer.Add(datenbankLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.datenbank, 0, wx.EXPAND)

        
        mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)
        
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(speicherBtn, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(beendeBtn, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
        btnSizer.Add((20, 20), 1)
        
        mainSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 20)

        self.SetSizer(mainSizer)

        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)


    def beenden(self, event):
        self.GetTopLevelParent().Close(True)


    def speichern(self, event):
        schluessel = "benutzer, passwort, datenbank"

        werte = ([self.benutzer.GetValue(), self.passwort.GetValue(),\
                  self.datenbank.GetValue()])

        werte = [wert.strip() for wert in werte]

        dictionary = dict(zip(schluessel.split(", "), werte))

        # stmt = bewerbungen.insert()
        # stmt.execute(dictionary)

        

class FirmaFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, None, -1, "Bewerbungen", size = (550, 620)) 
        self.InitUI()

        
    def InitUI(self):
        nb = wx.Notebook(self)
        nb.AddPage(Reiter1(nb), "Eingabe")
        nb.AddPage(Reiter2(nb), "Vorlagen")
        nb.AddPage(Reiter3(nb), "Konfiguration")
        
        self.Centre()
        self.Show(True)


if __name__=='__main__':
    app = wx.App()
    FirmaFrame(None, "Bewerbungen")
    app.MainLoop()
