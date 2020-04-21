# wxChomeur
Firmendaten für Bewerbung in MySQL-Datenbank speichern und PDF-Bewerbungsunterlagen (Anschreiben, Lebenslauf, Zeugnisse) zusammenstellen.

Verwendung: ./wxChomeur.py

1.      Den Angebotstext in die Zwischenablage kopieren!
2.      In der nun erscheinenden Oberfläche die entsprechenden Daten eintragen.
3.      Daten mit Druck auf Speicher-Knopf speichern.
4.      Der Anweisung des nun erscheinenden Dialogs folgen.
5.      Programm beenden.
6.      Template-Datei in das gewünschte Verzeichnis kopieren (abhängig vom 'Aufenthaltsort' von erstellePDF.py).
7.      ./erstellePDF.py lebenslauf.pdf zeugnisse.pdf

Das Programm bedient sich standardmäßig der SQLite3-Datenbank, die in den meisten Python3-Distributionen mitgeliefert wird.
Natürlich können hier Anpassungen vorgenommen werden -- etwa für den Fall, dass MySQL als Datenbank verwendet werden soll.

Abhängigkeiten je nach Software-Konstellation:

MariaDB, MySQL (ggf. Konfiguration ändern!) oder SQLite3, jinja2, texlive, etc. sowie die richtigen Daten in connect.txt eintragen!

Mindestkonfigurationsanforderung für die Datenbank liegt in Form von connect.txt bei!

Der Einfachheit halber lege ich noch eine Musterdatenbank (SQLite3) bei.

Dokumentation wird noch vervollständigt. Also Geduld!

NOCH AUSSTEHEND: Integration der Funktionalität von erstellePDF.py ins Hauptprogramm, computerlinguistische Analyse des Angebotstextes
im Hinblick auf das Anschreiben mit Hilfe von nltk (Natural Language Toolkit), pandas und Redis.