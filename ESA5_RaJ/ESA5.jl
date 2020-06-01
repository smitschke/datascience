#Exercise 3

#Create a 2x4 two dimensional matrix with random floats in it and in the next step determine the biggest element. 
m1=rand(0:0.01:10,(2,4))
println(m1)
println(maximum(m1)) #Wert
println(findmax(m1)) #Wert + Index

#Exercise 4

#1. Create two matrices of the same layout and test if addition and subtraction of the matrix works as expected: C = A + B 
m2 = [1 2 3; 4 5 6; 7 8 9]
m3 = [1 2 3; 3 5 6; 7 8 9]

println(m2 + m3)
println(m2 - m3)
#Addition und Subtraktion funktioniert wie erwartet

#2. Now compare matrix multiplication either this way A * B and this way A .* B. Whats the difference?! 
println(m2 * m3) #Führt Matrixmultiplikation wie erwartet aus. Also Zeile x Spalte
println(m2 .* m3) #Multipliziert die Elemente indexbasiert. Also m1[0] x m2[0] usw.

#3. What about matrix division with "/" or "\"?! 
println(m2 / m3) #Multipliziert m2 mit der Inversen Matrix von m3, also: m2 * inv(m3)
println(m2 \ m3) #Generiert Matrix X: m2*X == m3

#4. Create a 3x3 integer matrix A with useful numbers. Now try A+1, A-1, A*2, A/2. 
#println(m2 + 2) und println(m2 - 2) wirft Fehler "no method matching + bzw. -"
#stattdessen:
println(broadcast(+, m2, 2))
#oder
println(m3 .- 2)
println(m2 * 2) #Multipliziert alle Elemente mit 2
println(m2 / 2) #Teilt alle Elemente durch 2

#5. Now multiply a 3x4 matrix with a suitable (4)vector. 
m4 = [1 2 3 4; 5 6 7 8; 9 10 11 12]
v1 = [1, 2, 3, 4]
println(m4 * v1)