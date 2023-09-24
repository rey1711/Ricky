Registrasi = input("Selamat Datang Mahasiswa Sistem Informasi")
Nama = input("Masukkan Nama : ")
Nim = input("Masukkan Nim : ")
Password = input("Masukkan Password : ")

if Password == "121212": 
    print("Anda  berhasil  login")
else : 
    print("Password yang anda masukan salah")

Angka= float(input("Angka dalam Kilogram : "))
operasi = input("gram, pon, ons : ")

if operasi == "gram":
    hasil = Angka * 1000 
    print (hasil)
elif operasi == "pon":
    hasil = Angka * 2.20462
    print (hasil)
elif operasi == "ons":
    hasil = Angka * 35.271
    print (hasil)
else :
    print ("hasil tidak diketahui")
    






