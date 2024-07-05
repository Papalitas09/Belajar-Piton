# array cugs

array = ["Tahu", "Tempe", "Oncom", "Labu"]

print(f" pemanggilan Array biasa di python : {array[0]}")
# dibawah ini print array dengan cara ditambah / kurang
print(f"Pemangilan Array yang di manipulasi : {array[3-1]}")
print(f"Pemangilan Array yang di manipulasi : {array[100 - 100]}")
print(f"Pemangilan Array yang di manipulasi : {array[1 + 1]}")

# dibawah ini menambah data pada suatu array
Nakama = ["Luffy", "Zoro", "Nami", "Sanji", "Chopper", "Robin"]
Nakama.append("Franky")
Nakama.append("Brook")
Nakama.append("Jinbe")
print(Nakama)

# Berikut dibawah ini array yang valuenya diganti
kekuatan_pahlawan = ["Terbang", "Membutakan lawan", "Pukulan dewa"]
print(kekuatan_pahlawan)
change = input("Kamu harus mengganti salah kekuatan Terbang mu..., apakah kamu mau ganti? [Y/N]")

if change == "Y" or change == "y" :
    kekuatan_pahlawan = ["Membutakan lawan", "Pukulan Dewa", "Berlari cepat"]
    print(f"Selamat kekuatan mu telah berganti {kekuatan_pahlawan}")
    
else:
    print("APALAH")
    


oca = "aku"
mantap = [oca] * 4
print(mantap)





