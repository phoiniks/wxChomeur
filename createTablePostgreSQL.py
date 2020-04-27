#!/usr/bin/python
from sqlalchemy import Table, Column, Unicode, Integer, MetaData

metadata = MetaData('postgresql://andreas:andreas@localhost:5432/andreas')        

bewerbungen = Table(
    'bewerbungen', metadata,
    Column('id', Integer, primary_key=True),
    Column('bezeichnung', Unicode(255), unique=False, nullable=False),
    Column('firma', Unicode(128), unique=False, nullable=False),
    Column('ansprechpartner', Unicode(64), unique=True, nullable=True),
    Column('anrede', Unicode(4), unique=False, nullable=True),
    Column('ausgabedatei', Unicode(255), unique=True, nullable=True),
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

metadata.create_all()
