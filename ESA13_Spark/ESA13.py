# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:48:28 2020
@author: Susanne Mitschke

____________________________________

Durchführung der Spark-Installation:

1. Spark 2.4.5 (Jun 05 2020) / Package-Type: Pre-built for Apache Hadoop 2.7 heruntergeladen 
   (Nicht die neueste Version genommen habe, da Spark wohl zum Standalone-Betrieb die unter 3. genannte Datei braucht,
    die ich leider nicht in der neuesten Version gefunden habe)
2. File entpackt und in einem separaten Spark-Ordner geschoben
3. Für hadoop winutils Datei heruntergeladen und ebenfalls in einem extra Ordner (hadoop/bin) abgespeichert
4. Für hadoop eine Umgebungsvariable HADOOP_HOME erstellt und den Pfad zu Spark in der PATH-Variable gespeichert

-> Spark lässt sich nun über pyspark in der Console aufrufen

Innerhalb Spyder (Anaconda) wurde Spark jedoch nicht erkannt. 
Hierfür habe ich extra noch einmal Spark 3.0.0 via "conda install -c conda-forge pyspark" installiert
(Wäre von vornherein wohl die einfachere Lösung gewesen, aber ich glaube das war nicht Sinn und Zweck der Übung :D)
"""

import re
from pyspark import SparkConf, SparkContext


if __name__ == "__main__":

    #Führe Spark set-up aus
    conf = SparkConf()
    conf.setAppName("Word count App")
    sc = SparkContext.getOrCreate(conf=conf)
    
    #Lese den Text ein
    text = sc.textFile("C:/spark/shakespeare.txt")
    
    #Entferne alle Satzzeichen und wandle alles in Kleinbuchstaben. Anschließend splitte den Text nach jedem Leerzeichen
    words = text.flatMap(lambda x: re.sub('[?!@#$\'",.;:()]', '', x).lower().split())
    
    #Erstelle für jedes Wort ein Tupel in der Form (Wort, 1), mit 1 als Counter
    words = words.map(lambda x: (x,1))
    
    #Entferne doppelte Einträge und erhöhe den Counter jeweils um 1
    words = words.reduceByKey(lambda x, y: x+y)
    
    #Vertausche die Reihenfolge im Tupel und sortiere nach der größe des Counters
    words = words.map(lambda x: (x[1], x[0])).sortByKey(False).take(24)
    
    print(words)
    #I think i "have" found the word ;) 
    #-> have kommt 5877 x im Text vor und ist damit auf Platz 24