# wxChomeur
Firmendaten für Bewerbung in MySQL-Datenbank speichern und PDF-Bewerbungsunterlagen (Anschreiben, Lebenslauf, Zeugnisse) zusammenstellen.

Verwendung: ./wxChomeur.py

1.      Den Angebotstext in die Zwischenablage kopieren!
2.	    In der nun aufpoppenden Oberfläche die entsprechenden Daten eintragen.
3.	    Daten mit Druck auf Speicher-Knopf speichern.
4.	    Programm beenden.
5.      Template-Datei in das gewünschte Verzeichnis kopieren (abhängig vom 'Aufenthaltsort' von erstellePDF.py).
6.	    ./erstellePDF.py lebenslauf.pdf zeugnisse.pdf

VORAUSSETZUNG: Installation von MariaDB, MySQL (ggf. Konfiguration ändern!) oder SQLite3, jinja2, texlive, etc. sowie die richtigen Daten in connect.txt eintragen!

Mindestkonfigurationsanforderung für die Datenbank liegt in Form von connect.txt bei!
Der Einfachheit halber lege ich noch eine Musterdatenbank (SQLite3) bei.

Dokumentation wird noch vervollständigt. Also Geduld!