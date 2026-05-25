# hp_prices = [['iphone', 15000000], ['samsung', 12000000], ['vivo', 5000000], ['oppo', 7000000], ['xiaomi', 7000000]]

# def display_menu():
#     print("\nMenu:")
#     print("1. Tampilkan semua harga HP")
#     print("2. keluar")

# def lihat_data():
#     print("\nData harga Hp:")

#     # jika data kosong
#     if not hp_prices:
#         print("tidak ada data.")
#         return
    
#     # menampilkan seriap merek dan harga
#     for hp, harga in hp_prices:
#         print(f"-{hp}: Rp{harga:,}")

    
# # def tambah_data():
# #     new_hp = input("masukkan merek hp yang ingin ditambahkan:")

# def main():
#     while True: 
#         display_menu()
#         choice = input("pilih menu (1-2): ")

#         if choice == '1':
#             lihat_data()
#         # elif choice == '2':
#         #     tambah_data()
#         elif choice == '2':
#             print("terimakasih! program selesai.")
#             break
#         else:
#             print("pilihan tidak valid. silahkan pilih lagi")

# #  if_name__ == "_main"
# main()

"""
    APLIKASI TO DO LIST - CLI
Fitur:
    - Tambah tugas
    - Lihat tugas
    - Hapus tugas
    - Tandai tugas selesai
"""

# ── Tipe data: list untuk menyimpan daftar tugas ──
daftar_tugas = []



#  FUNCTION: Tampilkan header
def tampilkan_header():
    print("         TO DO LIST ")

#  FUNCTION: Tampilkan menu utama
def tampilkan_menu():
    tampilkan_header()
    print("  1. Tambah Tugas")
    print("  2. Lihat Tugas")
    print("  3. Tandai Tugas Selesai")
    print("  4. Hapus Tugas")
    print("  5. Keluar")


#  FUNCTION: Tambah tugas baru
def tambah_tugas():
    tampilkan_header()
    print("    TAMBAH TUGAS BARU")

    nama_tugas = input("  Nama tugas : ").strip()

    # Percabangan if-else: validasi input tidak boleh kosong
    if nama_tugas == "":
        print("\n   Nama tugas tidak boleh kosong!")
    else:
        # Tipe data dict untuk menyimpan info tiap tugas
        tugas_baru = {
            "nama"    : nama_tugas,
            "selesai" : False          # tipe data bool
        }
        daftar_tugas.append(tugas_baru)

        # Operator matematika: hitung total tugas
        total = len(daftar_tugas)
        print(f"\n   Tugas '{nama_tugas}' berhasil ditambahkan!")
        print(f"  Total tugas sekarang: {total}")

    input("\n  Tekan Enter untuk kembali...")



#  FUNCTION: Lihat semua tugas
def lihat_tugas():
    tampilkan_header()
    print("  DAFTAR TUGAS")

    # Percabangan if-else: cek apakah list kosong
    if len(daftar_tugas) == 0:
        print("  (Belum ada tugas. Silakan tambah tugas.)")
    else:
        # Operator logika & perulangan for dengan enumerate
        selesai_count = 0
        for nomor, tugas in enumerate(daftar_tugas, start=1):
            if tugas["selesai"]:          # operator logika (bool)
                status = "berhasil diselesaikan"
                selesai_count += 1        # operator matematika
            else:
                status = "gagal diselesaikan"

            print(f"  {nomor}. [{status}] {tugas['nama']}")

        # Operator matematika: hitung persentase selesai
        total        = len(daftar_tugas)
        belum_selesai = total - selesai_count
        persen       = (selesai_count / total) * 100   # pembagian & perkalian

        print("-" * 34)
        print(f"  Total   : {total} tugas")
        print(f"  Selesai : {selesai_count} tugas")
        print(f"  Pending : {belum_selesai} tugas")
        print(f"  Progress: {persen:.1f}%")

    input("\n  Tekan Enter untuk kembali...")



#  FUNCTION: Tandai tugas selesai
def tandai_selesai():
    tampilkan_header()
    print("   TANDAI TUGAS SELESAI")

    if len(daftar_tugas) == 0:
        print("  (Belum ada tugas dalam daftar.)")
        input("\n  Tekan Enter untuk kembali...")
        return

    # Tampilkan daftar tugas yang belum selesai
    ada_pending = False
    for nomor, tugas in enumerate(daftar_tugas, start=1):
        if not tugas["selesai"]:           # operator logika: negasi bool
            print(f"  {nomor}. {tugas['nama']}")
            ada_pending = True

    # Percabangan if-else
    if not ada_pending:
        print(" Semua tugas sudah selesai!")
        input("\n  Tekan Enter untuk kembali...")
        return
    try:
        pilihan = int(input("  Pilih nomor tugas: "))

        # Operator logika: validasi rentang nomor (and)
        if pilihan >= 1 and pilihan <= len(daftar_tugas):
            tugas = daftar_tugas[pilihan - 1]   # operator matematika: indeks

            if tugas["selesai"]:
                print(f"\n  Tugas '{tugas['nama']}' sudah ditandai selesai.")
            else:
                tugas["selesai"] = True
                print(f"\n   Tugas '{tugas['nama']}' berhasil diselesaikan!")
        else:
            print("\n  Nomor tidak valid!")

    except ValueError:
        print("\n  Masukkan angka yang valid!")

    input("\n  Tekan Enter untuk kembali...")


#  FUNCTION: Hapus tugas
def hapus_tugas():
    tampilkan_header()
    print("   HAPUS TUGAS")

    if len(daftar_tugas) == 0:
        print("  (Belum ada tugas dalam daftar.)")
        input("\n  Tekan Enter untuk kembali...")
        return

    # Perulangan for: tampilkan semua tugas
    for nomor, tugas in enumerate(daftar_tugas, start=1):
        status = "tugas" if tugas["selesai"] else "tugas belum selesai"
        print(f"  {nomor}. [{status}] {tugas['nama']}")

    try:
        pilihan = int(input("  Pilih nomor tugas yang dihapus: "))

        # Operator logika: validasi rentang (and)
        if pilihan >= 1 and pilihan <= len(daftar_tugas):
            tugas_dihapus = daftar_tugas[pilihan - 1]
            konfirmasi    = input(
                f"\n  Hapus '{tugas_dihapus['nama']}'? (y/n): "
            ).lower()

            if konfirmasi == "y":
                daftar_tugas.pop(pilihan - 1)    # operator matematika: indeks
                print(f"\n  Tugas berhasil dihapus!")
                print(f" Sisa tugas: {len(daftar_tugas)}")
            else:
                print("\n  Penghapusan dibatalkan.")
        else:
            print("\n  Nomor tidak valid!")

    except ValueError:
        print("\n   Masukkan angka yang valid!")

    input("\n  Tekan Enter untuk kembali...")


#  FUNCTION: Program utama (main loop)
def main():
    print("\n  Selamat datang di Aplikasi To Do List!")

    # Perulangan while: jalankan program terus sampai user keluar
    while True:
        tampilkan_menu()
        pilihan = input("  Pilih menu (1-5): ").strip()

        # Percabangan if-elif-else untuk navigasi menu
        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            tandai_selesai()
        elif pilihan == "4":
            hapus_tugas()
        elif pilihan == "5":
            # Perulangan for: tampilkan animasi keluar
            print("\n  Sampai jumpa!")
            for i in range(3, 0, -1):          # perulangan mundur
                print(f"  Menutup program dalam {i}...", end="\r")
                import time
                time.sleep(1)
            print("\n")
            break                              # keluar dari while loop
        else:
            print("\nPilihan tidak valid! Masukkan angka 1-5.")
            input("  Tekan Enter untuk kembali...")


# ── Entry point ──
if __name__ == "__main__":
    main()