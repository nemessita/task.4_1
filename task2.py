# İstifadəçidən alınan şifrənin keçərliliyini kontrol edən proqram yazın.
# n giriniz...'))

# Doğrulama:

# [az] arasında en az 1 harf ve [AZ] arasında en az 1 harf.
# [0-9] arasında en az 1 sayı.
# [$#@]'dan en az 1 karakter.
# Minimum uzunluk 6 karakter.
# Maksimum uzunluk 16 karakter.

import re
password = input("Sifrenizi daxil edin:")

if 6 <= len(password) <= 16:
    print("Sifre 6-16 arasi")
elif re.search("[a-z]", password):
    print("Sifre min kicik herifle")
elif re.search("[A-Z]", password):
    print("Sifre max boyuk herifle")
elif re.search("[0-9]", password):
    print("Sifre reqem olmali")
elif re.search("[$#@]", password):
    print("Sifre zehmet olmasa [$#@] simvol birini daxil edin")
else:
    print("Sifre uygun deyil")
