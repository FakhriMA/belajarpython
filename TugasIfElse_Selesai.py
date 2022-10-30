#untuk mendapat nilai A nilai rata rata mulai 90 ~ 100
#untuk mendapat nilai B nilai rata rata mulai 80 ~ 89
#untuk mendapat nilai C nilai rata rata mulai 70 ~ 79
#untuk mendapat nilai D nilai rata rata mulai 60 ~ 69
#untuk mendapat nilai E nilai rata rata mulai 50 ~ 59

# matematika 
# english
# b indo
# pkn
# biologi 
# fisika 



math = int(input('Matematika ='))
eng = int(input('English ='))
indo = int(input('Bahasa Indonesia ='))
pkn = int(input('PKN ='))
bio = int(input('Biologi ='))
fisika = int(input('Fisika ='))

rata2 = int((math + eng + indo + pkn + bio +fisika) / 6)

print('Rata - rata =', rata2)

if(rata2 >= 90 and rata2 <= 100): #jika rata-rata 90-100 maka mendapat nilai A
 print(f'Rata-rata {rata2} = A') 
elif(rata2 >= 80 and rata2 <= 89): #jika rata-rata 80-89 maka mendapat nilai B
 print(f'Rata-rata {rata2} = B') 
elif(rata2 >= 70 and rata2 <= 79): #jika rata-rata 70-79 maka mendapat nilai C
 print(f'Rata-rata {rata2} = C') 
elif(rata2 >= 60 and rata2 <= 69): #jika rata-rata 60-69 maka mendapat nilai D
 print(f'Rata-rata {rata2} = D') 
elif(rata2 < 60): #jika rata-rata kurang dari 60 mendapat nilai E
 print(f'Rata-rata {rata2} = E') 
else:
    print("Tidak dalam jangkauan")

