import random
random = random.randint(1, 4)


posisi_alien = random 
print(posisi_alien)
# kosong
lobang = "|_|"
tempat = [lobang] * 4 #lobang ori yang ada 4 lobang no alien



# yang ada alien
tempat_alien = tempat.copy()
tempat_alien[posisi_alien - 1] = ("|x_x|")\


# Dibawah ini buat hilangin kutip, segala macem yang array. Dandiubah menjadi string
tempat = ' '.join(tempat)    
tempat_alien = ' '.join(tempat_alien)




def menerima() :
     yakin1 = input("Oke tapi lo yakin bisa menangin nya? [Y/N]")
     if yakin1 == 'Y' or yakin1 == 'y':
            print("Baiklah yok, kita main!!!")
            print(f'''
                Tebaklah dimanakah alien di lobang yang di bawah ini!!!
                     
                        {tempat}
                         
                         
                         ''')
            tebakan = int(input("[1/2/3/4]"))
            
                    
                 
            if tebakan == random :
                yakingak = input(f"Apakah lo udh yakin tebakan lo adalah {tebakan}? [Y/N]")
                if yakingak == "Y" or yakingak == "y" :
                    print(f"SELAMAT {nama_user} lo menang!!!!")
                    print(f"Posisi Alien berada di  lobang nomer {tebakan}!!! \n {tempat_alien} ")
                    
                elif yakingak == "N" or yakingak == "n" :
                    print("Yah peak, seharusnya lo udh yakin")
                    yakingak2 = input("Gue tanya lagi, Apakah lo udh yakin dengan pilihan lo? [Y/N]")
                    
                    if yakingak2 == "Y" or yakingak2 == "y" :
                        print(f"SELAMAT {nama_user} lo menang!!!!")
                        print(f"Posisi Alien berada di  lobang nomer {tebakan}!!! \n {tempat_alien} ")
                        print("Bagus akhirnya lo yakin, lain kali harus yakin sama pilihan lo yang tempuh tod")
                        
                    elif yakingak2 == "N" or yakingak2 == "n" :
                        print(f"SELAMAT {nama_user} lo menang!!!!")
                        print(f"Posisi Alien berada di  lobang nomer {tebakan}!!! \n {tempat_alien} ")
                        print("Lain kali harus yakin sama pilihan yang lo tempuh tod")
                        
                else :
                    print("apalah.Tapi")
                    print(f"SELAMAT {nama_user} lo menang!!!!")
                    print(f"Posisi Alien berada di  lobang nomer {tebakan}!!! \n {tempat_alien} ")
                    
                
            elif tebakan != random:
                  yakingak1 = input(f"Apakah lo udh yakin tebakan lo adalah {tebakan}? [Y/N]")
                  if yakingak1 == "Y" or yakingak1 == "y" :
                     print("Mampus lo salah awokwokaokwo")
                  elif yakingak1 == "N" or "n" :
                     print("awkwodk mampus kalah wadowjdaw")
            
            else :
                 print("apalah")
                 
     elif yakin1 == 'N' or yakin1 == 'n':
        print(f"Yaudah sih {nama_user}.Gue ga butuh orang lemah kek lo!! ")
    



print('''
 ^^ SELAMAT DATANG PARA MANUSIA 👽👽 ^^ 
''')

nama_user = input("Sebelumnya, Nama lo siapa manusia?")

while nama_user == "":
    nama_user = input("Kasih tau dulu nama lo manusia!!! :")

print(f'''
    OH nama lo {nama_user}.Btw mau main Game ga ama gue??''')

ajakanp = input("[Y/N]")

if ajakanp == 'Y' or ajakanp == 'y':
    menerima()
   
    
    
elif ajakanp == 'N' or ajakanp == 'n':
    mauga = input("kenapa cuk? gue tanya lagi, mau main sama gue ga? serulohh  [Y/N]?")
    if mauga == "Y" or mauga == "y" :
        menerima()
    elif mauga == "n" or mauga == "N" :
        print("YWDH SIH, ADA KATA-KATA TERAKHIR? BYEE")
        exit()
    else :
        print("Apalah..")
        exit()
      
   
    
else :
    print("Yang bener dong jawabnya peak.Udahan ah bye👽👽👽")
    

