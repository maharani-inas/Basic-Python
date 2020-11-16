def home() :
    print("\n --- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilih = int(input("Pilih nomor menu : "))
    return pilih

def daftar(kontak):
    print("\nDaftar Kontak : ")
    for i in range(len(kontak)):
        print("\nNama : ",kontak[i][0])
        print("No Telepon : ",kontak[i][1])

def tambah(kontak):
    c=[]
    for i in range(len(kontak[0])):
        if i==0:
            c.append(str(input("Nama : ")))
        if i==1:
            c.append(str(input("No Telepon : ")))
    kontak.append(c)
    return kontak
    

value=True
kontak = [["Lea","087987342948"],["Michael", "083416793827"]]
while value:
    pilih=home()
    if pilih==1:
        daftar(kontak)
        value = True
    elif pilih==2:
        kontak=tambah(kontak)
        print("Kontak Berhasil ditambahkan")
        value=True
    elif pilih==3:
        print("\nProgram selesai, sampai jumpa!")
        print("Semoga harimu menyenangkan!")
        value=False
    else:
        print("\nMenu tidak tersedia")
        value=True
