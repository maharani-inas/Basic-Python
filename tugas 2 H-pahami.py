def tambah(kontak): 
    temp = [] 
    for i in range(len(kontak[0])): 
        if i == 0: 
            temp.append(str(input("Enter name: "))) 
        if i == 1: 
            temp.append(int(input("Enter number: "))) 
    kontak.append(temp) 
    return kontak 
def display_all(kontak): 
    print('\nDaftar Kontak :')
    for i in range(len(kontak)):
            print("\nNama : ",kontak[i][0])
            print("Telepon : ",kontak[i][1])
            
def thanks(): 
    print("\nProgram selesai, sampai jumpa!")
    
def menu(): 
    print("\n--- Menu ---") 
    print("1. Daftar Kontak") 
    print("2. Tambah Kontak") 
    print("3. Keluar") 
    pilihan = int(input("Pilih menu : ")) 
    return pilihan

loop = True
print("Selamat datang!")   
kontak = [["Budiono","0812345678"],["Candra","089987654"]]
while loop:
    pilih = menu()
    if pilih == 1: 
        display_all(kontak)
        loop = True
    elif pilih == 2: 
        kontak = tambah(kontak)
        print('\nKontak berhasil ditambahkan')
        loop = True
    elif pilih == 3: 
        thanks()
        loop = False
    else: 
        print("\nMenu tidak tersedia")
        loop = True