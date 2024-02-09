# Berner_Inkunabeln
Dieses Repositiory wird die Materialien (Code und Daten) für die Erstellung des Berner Inkunabelkatalogs ([Die Inkunabeln in der Universität Bern](https://doi.org/10.36950/kat-ink-2023) enthalten.

## 01_Code_Download_Metadaten_Inkunabeln
Enthält den Code für den automatisierten Download der Inkunabel-Metadaten sowie ein Excel-File, in welches die für den Download erforderlichen Network IDs der Inkunabel-Metadaten abgelegt sind (Spalte A, 1 MMS-ID pro Zeile/Zelle). Der Dateiname der Excel-Datei kann in Zeile 32 konfiguriert werden. Die einzelnen Datensätze werden jeweils in einzelnen Files abgelegt. 

## 02_Code_Erstellung_Rohdatensätze
Enthält den Code für die automatisierte Zusammenführung der heruntergeladenen Inkunabel-Metadaten zum rohen Inkunabel-Datensatz. Nach einer händischen Bearbeitung stellt der mit diesem Code generierte Datensatz die Datengrundlage des Inkunabelkatalogs dar (siehe Ordner *10_Daten_Grundlage*). 

## 03_Code_Nachbearbeitung_Datensätze_Inkunabeln
Enthält den Code für die automatisierte Nachbearbeitung der händisch prozessierten Inkunabel-Datensätze (siehe Ordner *10_Daten_Grundlage*) sowie ein Excel-File
mit für die Legenden- und Bildeinbindung erforderlichen Informationen. 
Folgende Nachbearbeitungsschritte werden durchgeführt:  
- Ersetzen von Stoppzeichen durch Guillemets
- Einfügen fehlender L5-Tags
- Einfügen der jeweiligen Inkunabelnummer
- Einfügen der Legenden- und Bildinformationen

## 04_Code_Überführung_Daten_in_Ausgabeformate
Enthält Scripte für die Konvertierung der nachbearbeiteten Inkunabel-Datensätze in die Ausgabeformate HTML und XML.  
- *convert_to_XML_single*: überführt die nachbearbeiteten Inkunabel-Datensätze in das XML-Format. Pro Inkunabel-Datensatz wird ein XML-File erstellt.  
- *convert_to_HTML_single*: überführt die nachbearbeiteten Inkunabel-Datensätze in das HTML-Format. Pro Inkunabel-Datensatz wird ein HTML-File erstellt.  
- *concat_single_xmls*: konkateniert die einzelnen XML-Files zu einem einzigen XML-File. Dieses File wird u. a. zur Erstellung des Inkunabelkatalogs im PDF-Format benötigt.  

## 05_Code_Erstellung_Register
Enthält den Code für die Erstellung der 4 Register des Inkunabelkatalogs (Autorinnenn und Autoren (Register 1), Drucker nach Orten (Register 2), Buchbinder (Register 3) und Vorbesitzer (Register 4)). Die Register werden aus den nachbearbeiteten Inkunabel-Datensätzen generiert und in die Formate HTML und XML ausgegeben.

## 06_Code_Datenformat_Upload_BOP
Enthält den Code für die Codierung der HTML-Inkunabel-Datensätze in ein base64-Format und für den Einbau der base64-codierten Datensätze in ein XML-Template-File. Das mit diesem Code generierte XML-Template-File erlaubt den automatiserten Upload der Inkunabel-Datensätze in BOP.  

## 10_Daten_Grundlage
Enthält die manuell bearbeiteten Daten nach dem automatisierten Download der Inkunabel-Metadaten (Code im Ordner *01_Code_Download_Metadaten_Inkunabeln*) und der automatisierten Erstellung der Inkunabel-Rohdatensätze (Code im Ordner *02_Code_Erstellung_Rohdatensätze*). Die hier vorhandenen Textfiles stellen die Datengrundlage des Inkunabelkatalogs dar.

## 11_Daten_Legenden
Enthält die Legendeninformationen der in den Inkunabeldatensätzen eingebundenen Bildern.

## Tool_Webseite
Enthält den Code für eine Webseitenversion des Katalogs, an die sich das Endprodukt (der Berner Inkunabelkatalog als BOP-Publikation) orientiert.
Die Webseite kann unter folgendem Link konsultiert werden:  
https://michaelh00.github.io/Berner_Inkunabeln/Tool_Webseite/

## Arbeitsweise/Aufruf der Skripte
Alle Skripte werden im jeweiligen Ordner ohne zusätzliche Parameter aufgerufen. Alle Konfigurationen werden durch Variablen in den Skripten vorgenommen (z.B. `data_path`, `output_path`, etc.)

Wenn der Katalog neu erstellt werden sollte, sind folgende Schritte notwendig.
1. Zusammenstellung der relevanten MMS-IDs in einem Excel-File; Download der Files per Skript im Ordner 01_Code_Download_Metadaten_Inkunabeln
2. Anwendung des Skripts in 2_Code_Erstellung_Rohdatensätze auf die heruntergeladenen Roh-Datensätze
3. Manuelle Bearbeitung der Datensätze im Zwischenformat
4. Konvertierung der bearbeiteten Datensätze in die Endformate durch die Skripte in den Ordnern 03_Code_Nachbearbeitung_Datensätze_Inkunabeln, 04_Code_Überführung_Daten_in_Ausgabeformate, 05_Code_Erstellung_Register, 06_Code_Datenformat_Upload_BOP

**ACHTUNG**: Da in Schritt 3 eine manuelle Bearbeitung der Datensätze erfolgt (bzw. hinsichtlich der bestehenden Datensätze bereits erfolgt ist), sollte nicht erneut alle Datensätze heruntergeladen und ins Zwischenformat konvertiert werden, sondern nur die neu hinzuzufügenden Datensätze heruntergeladen werden. Der genaue Prozess kann durch die in den Skripten definierten Pfadangaben gesteuert werden.



---
Dieses Repository befindet sich im Aufbau !
