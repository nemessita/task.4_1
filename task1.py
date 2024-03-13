# İstifadəçidən alınan məlumatlara uyğun olaraq bədən kütlə indeksini hesablayın.
#  Bədən Kütle İndeksi: Kütlə / (Boy(m) / 100) ustu 2
#  BKİ 18.5'un altındadırsa -------> Zəif
#  BKİ 18.5 ile 25 arasındadırsa ------> Normal
#  BKİ 25 ile 30 arasındadırsa --------> Kilolu
#  BKİ 30'un üstündədirsə -------------> Obez

# Boyunuzu Daxil edin:174
# Kütlənizi Daxil edin:76
# Normal


boy = int(input("Boyunuzu Daxil edin: "))
kutle = int(input("Kütlənizi Daxil edin: "))

index = kutle / (boy / 100) ** 2

if index <= 18.5:                     
    print("Zəif")
elif 18.5 < index <= 24.9:             
    print("Normal")
elif 25 <= index <= 29.9:               
    print("Kilolu")
elif index >= 30:                       
    print("Obez")







