nilai = int(input('Enter any number = '))

#jika nilai 90 ~ 100 maka mendapat nilai A 
#jika nilai 85 ~ 89 maka mendapat nilai B
#jika nilai 70 ~ 79 maka mendapat nilai C 
#jika nilai 60 ~ 69 maka mendapat nilai D 
#jika nilai kurang dari 60 mendapat nilai F

if(nilai >= 90 and nilai <= 100 ):
    print(f'Nilai {nilai} = A')
elif(nilai >= 80 and nilai <= 89):
    print(f'Nilai {nilai} = B')
elif(nilai >= 70 and nilai <= 79):
    print(f'Nilai {nilai} = C')
elif(nilai >= 60 and nilai <= 69):
    print(f'Nilai {nilai} = D')
elif(nilai < 60 ):
    print(f'Nilai {nilai} = F')
else:
    print(f'Nilai {nilai} = Nilai berada diluar jangkauan')