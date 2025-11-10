# Program Pemilihan Ketua
print("=== SISTEM VOTING PEMILIHAN KETUA ===")

# Input nama kandidat
kandidat1 = input("Masukkan nama kandidat 1: ")
kandidat2 = input("Masukkan nama kandidat 2: ")
kandidat3 = input("Masukkan nama kandidat 3: ")

# Inisialisasi suara
suara1 = 0
suara2 = 0
suara3 = 0

# Input jumlah pemilih
jumlah_pemilih = int(input("\nMasukkan jumlah pemilih: "))

# Proses pemilihan (simulasi do-while)
i = 1
while True:
    print(f"\nPemilih ke-{i}")
    print(f"1. {kandidat1}")
    print(f"2. {kandidat2}")
    print(f"3. {kandidat3}")

    pilihan = input("Masukkan pilihan Anda (1/2/3): ")

    if pilihan == "1":
        suara1 += 1
    elif pilihan == "2":
        suara2 += 1
    elif pilihan == "3":
        suara3 += 1
    else:
        print("Pilihan tidak valid, suara tidak dihitung!")

    i += 1
    if i > jumlah_pemilih:  # kondisi berhenti seperti do-while
        break

# Hitung total suara menggunakan for loop
total_suara = [suara1, suara2, suara3]
kandidat = [kandidat1, kandidat2, kandidat3]

print("\n=== HASIL PEMILIHAN KETUA ===")
for j in range(3):
    print(f"{kandidat[j]} memperoleh {total_suara[j]} suara.")

# Tentukan pemenang
max_suara = total_suara[0]
pemenang = kandidat[0]

for j in range(1, 3):
    if total_suara[j] > max_suara:
        max_suara = total_suara[j]
        pemenang = kandidat[j]

print(f"\nPemenang pemilihan adalah: {pemenang} dengan {max_suara} suara!")
