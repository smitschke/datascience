#Exercise 1

#Write a program to guess a number in between0 and 100! Hence the computer invents the number and the user = you tries to guess it!

guess_number <- function() {
  rnum <- floor(runif(1, min=0, max=101))
  uinput <- readline(prompt="Bitte gib eine Zahl zwischen 0 und 100 ein: ")
  uinput <- as.integer(uinput)
  
  if (rnum == uinput) {
    print("Richtig geraten!")
  } else {
    output = paste("Leider falsch geraten. Die richtige Zahl wäre die", rnum, "gewesen", sep=" ")
    print(output)
  }
}

guess_number()

#Exercise 2

#Analyse the esoph dataset. Can you derive some useful statements from it? Use data() to see all available datasets. 

#data()
data(esoph)

#Ausgabe der ersten 10 Zeilen
head(esoph, 10)

#Anzahl der Zeilen
nrow(esoph)

#Anzahl der Spalten
ncol(esoph)

#Anzahl Zeilen und Spalten
dim(esoph)

#Zusammenfassung wieviele Einträge unter Alter, Alkohol- und Tabakkonsum, sowie staistische Infos (wie Mittelwert und Median) bei den Fall- und Teilnehmerzahlen
summary(esoph)

#Startet den Viewer (in RStudio)
View(esoph)
aggregate(esoph$ncases, by=list(esoph$agegp), FUN = max)
aggregate(esoph$ncases, by=list(esoph$alcgp), FUN = max)
aggregate(esoph$ncases, by=list(esoph$tobgp), FUN = max)
#Es ist ersichtlich, dass Speiseröhrenkrebs vor allem im gehobenen Alter auftritt (die meisten Fälle zwischen 65-74) und sich Alkoholkonsum wohl mehr auswikrt als Tabakkonsum (bei dem Datensatz mit den meisten Fällen lag der Tabakkonsum gerade mal zwischen 0-9g pro Tag)

aggregate(esoph$ncases, by=list(esoph$agegp), FUN = sum)
aggregate(esoph$ncontrols, by=list(esoph$agegp), FUN = sum)
#Unabhängig vom Tabak- und Alkoholkonsum treten in der Altersgruppe zwischen 55-64 die meisten Fälle auf, jedoch liegen hier auch die meisten Testdaten dafür vor
