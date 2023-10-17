# Nama : Ricky Renaldi 
# Nim : 2309116064
# Kelas : SI B
# Konversi Nilai Mahasiswa



Nama : input("Masukkan nama kalian : ")
Nim  : input("Masukkan NIM : ")
Kelas: input("Masukkan kelas : ")

angka1 = float(input("input Nilai Ujian Anda : "))
if angka1 >= 0 and angka1 <= 75 : 
        print("ANDA TIDAK LULUS UJIAN")
elif angka1 >= float(97.1) and angka1 <= float(100) :
        print("Nilai ", angka1, " = A") 
elif angka1 >= float(94.1) and angka1 <= float(97) :
        print("Nilai ", angka1, " = A-") 
elif angka1 >= float(89.1) and angka1 <= float(94) :
        print("Nilai ", angka1, " = A/B")
elif angka1 >= float(87.1) and angka1 <= float(89) :
        print("Nilai ", angka1, " = B+")
elif angka1 >= float(83.1) and angka1 <= float(87) :
        print("Nilai ", angka1, " = B")
elif angka1 >= float(79.1) and angka1 <= float(83) :
        print("Nilai ", angka1, " = B-")
elif angka1 >= float(75.1) and angka1 <= float(79) :
        print("Nilai ", angka1, " = B/C")
elif angka1 >= float(70.1) and angka1 <= float(75) :
        print("Nilai ", angka1, " = C+")
elif angka1 >= float(67.1) and angka1 <= float(70) :
        print("Nilai ", angka1, " = C")
elif angka1 >= float(64.1) and angka1 <= float(67) :
        print("Nilai ", angka1, " = C-")
elif angka1 >= float(60.1) and angka1 <= float(64) :
        print("Nilai ", angka1, " = C/D")
elif angka1 >= float(57.1) and angka1 <= float(60) :
        print("Nilai ", angka1, " = D+")
elif angka1 >= float(54.1) and angka1 <= float(57) :
        print("Nilai ", angka1, " = D")
elif angka1 >= float(50.1) and angka1 <= float(54) :
        print("Nilai ", angka1, " = D-")
elif angka1 >= float(47.1) and angka1 <= float(50) :
        print("Nilai ", angka1, " = D/E")
elif angka1 >= float(44.1) and angka1 <= float(47) :
        print("Nilai ", angka1, " = E+")
elif angka1 >= float(0) and angka1 <= float(44) :
        print("Nilai ", angka1, " = E")
else :
        print("anda harus menginput angka")