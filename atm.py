#MENU UTAMA
import getpass
class Atm:
 def pilih_menu():
  saldo = 100000
  print("="*45)
  print("\t\tATM BERSAMA\t\t")
  print("\tJl. S. Parman No.14 Balikpapan Tengah")
  print("\t\tTelp.0542-48215")
  print("================ MENU PILIHAN ===============")
  print("[1] Informasi Saldo")
  print("[2] Bayar")
  print("[3] Transfer")
  print("[4] Ambil Uang")
  print("[5] Keluar")
  print("="*45)
  
  pilih = int(input("Masukkan Menu Pilihan [1/2/3/4/5]: "))
  if(pilih == 1):
   n = 1
   while(n == 1):
    print("Menu: Informasi Saldo")
    print("Menu: Informasi Rekening Tabungan")
    print("Menu: Informasi Giro")
    kembali = input("Masukkan Transaksi Lagi? [y/t]: ")
    if((kembali == "y") or (kembali == "Y")):
     Atm.pilih_menu()
     continue
  elif (pilih == 2):
   n = 1
   while(n == 1):
    print("Menu: Bayar")
    print("[1] BPJS\t[3] PDAM")
    print("[2] PLN\t\t[4] PULSA PASCABAYAR")
    kembali = input("Masukkan Transaksi Lagi? [y/t]: ")
    if((kembali == "y") or (kembali == "Y")):
     Atm.pilih_menu()
  elif (pilih == 3):
   n = 1
   while(n == 1):
    print("Menu: Transfer")
    print("[1] Transfer Antar Bank")
    print("[2] Transfer Sesama Bank")
    kembali = input("Masukkan Transaksi Lagi? [y/t]: ")
    if((kembali == "y") or (kembali == "Y")):
     Atm.pilih_menu() 
     continue
  elif (pilih == 4):
   n = 1
   while(n == 1):
    print("Menu: Ambil Uang")
    print("[1] Rp. 1.000.000,-")
    print("[2] Rp. 500.000,-")
    print("[3] Rp. 300.000,-")
    print("[4] Nominal Lain")
    print("="*45)
    ambil = int(input("Masukkan Nominal Yang Akan Diambil [1/2/3/4]: "))
    uang1 = 1000000
    uang2 = 500000
    uang3 = 300000
    if(ambil == 1):
     saldo > uang1
     saldo = saldo - uang1
     print('Status   : Penarikan Berhasil')
     print('Saldo Anda Saat Ini Adalah Rp. ',saldo)
     kembali = input("Masukkan Transaksi Lagi? [y/t]: ")
     if((kembali == "y") or (kembali == "Y")):
        Atm.pilih_menu()
        continue
    elif(ambil == 2):
     saldo > uang2
     saldo = saldo - uang2
     print('Status   : Penarikan Berhasil')
     print('Saldo Anda Saat Ini Adalah Rp. ',saldo)
     kembali = input("Masukkan Transaksi Lagi? [y/t]: ")
     if((kembali == "y") or (kembali == "Y")):
        Atm.pilih_menu()
        continue
    elif(ambil == 3):
     saldo > uang3
     saldo = saldo - uang3
     print('Status   : Penarikan Berhasil')
     print('Saldo Anda Saat Ini Adalah Rp. ',saldo)
     kembali = input("Masukkan Transaksi Lagi? [y/t]: ")
     if((kembali == "y") or (kembali == "Y")):
        Atm.pilih_menu()
        continue
    elif(ambil == 4):
     uang4 = int(input("Masukkan Nominal Uang Yang Akan Diambil: Rp."))
     saldo > uang4
     saldo = saldo - uang4
     print('Status   : Penarikan Berhasil')
     print('Saldo Anda Saat Ini Adalah Rp. ',saldo)
     kembali = input("Masukkan Transaksi Lagi? [y/t]: ")
     if((kembali == "y") or (kembali == "Y")):
        Atm.pilih_menu()
        continue
    else :
     print("Maaf Saldo Anda Tidak Mencukupi")
     print('Saldo Anda Saat Ini Adalah Rp. ',saldo)
     kembali = input("Masukkan Transaksi Lagi [y/t]: ")
     if((kembali == "y") or (kembali == "Y")):
      Atm.pilih_menu() 
      continue
  elif(pilih == 5):
   print("Terima Kasih, Silahkan Ambil Kartu Anda!")
   exit()
 def menu_utama():
  pin = "12345"
  print("="*45)
  print("\t\tATM BERSAMA")
  print("\tJl. S. Parman No.14 Balikpapan Tengah")
  print("\t\tTelp.0542-48215")
  print("================ MENU UTAMA ================")
  for i in range(3) :
   sandi = getpass.getpass("Masukkan PIN Anda\t: ")
   if(sandi == pin):
    Atm.pilih_menu()
   else :
    print("PIN Anda Salah!")
    if i == 2 :
     print("Anda Telah Melakukan 3x Percobaan")
     print("Kartu Anda Terblokir")
     exit() 
Atm.menu_utama()
   