# [No 2] Grade Mahasiswa
# Penentuan Deskripsi Nilai Mahasiswa

nama = "Pingky"
nilai = 96

if 0 <= nilai < 35:
    print("Grade Nilai", nama, "adalah E")
elif 35 <= nilai < 50:
    print("Grade Nilai", nama, "adalah D")
elif 50 <= nilai < 65:
    print("Grade Nilai", nama, "adalah C")
elif 65 <= nilai < 80:
    print("Grade Nilai", nama, "adalah B")
elif 80 <= nilai <= 100:
    print("Grade Nilai", nama, "adalah A")
else:
    print("Nilai Invalid")

