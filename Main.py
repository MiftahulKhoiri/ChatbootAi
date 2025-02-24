import time
import datetime
from babel.dates import format_date
import sys
import shutil
import os
import random
import subprocess

# Daftar modul yang dibutuhkan
modul_yang_dibutuhkan = ["babel"]
data_nama = ""

def hapus_layar():
    # Penghapus layar
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS dan Linux
        os.system("clear")

def cek_install_modul():
    # Memeriksa dan menginstal modul yang dibutuhkan
    for modul in modul_yang_dibutuhkan:
        try:
            __import__(modul)
            print(f" >>.Modul {modul} sudah terinstal.")
            time.sleep(1)
        except ImportError:
            print(f" >>.Modul {modul} belum terinstal. Menginstal...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", modul])
            print(f" >>.Modul {modul} berhasil diinstal.")
    print(" >>.Semua modul telah diinstal.")

def logo():
    # Fungsi logo
    lebar_terminal = shutil.get_terminal_size().columns
    spasi = " " * ((lebar_terminal - 30) // 2)
    print("\n" + spasi + """
       =========================
      |				|
      |		BOOT AI		|
      |				|
       ==========================
   
""")
    print(spasi + " Selamat datang di Chatbot AI ")
    print(spasi + "-------------------------------")

def loading_proses(teks, waktu=10):
    # Fungsi loading
    print(teks)
    for i in range(waktu + 1):
        proses = i * 10
        sys.stdout.write("\r >>.Proses: [{}{}] {}%".format("#" * (proses // 10), "-" * (10 - proses // 10), proses))
        sys.stdout.flush()
        time.sleep(0.10)
    print("\n")

def salam_waktu():
    # memberi salam sesuai waktu nya
    jam_sekarang = datetime.datetime.now().hour
    if 1 <= jam_sekarang <= 9:
        return cari_jawaban("pagi")
    elif 10 <= jam_sekarang <= 12:
        return cari_jawaban("siang")
    elif 13 <= jam_sekarang <= 15:
        return cari_jawaban("siang")
    elif 16 <= jam_sekarang <= 18:
        return cari_jawaban("sore")
    else:
        return cari_jawaban("malam")

def tanggal_hariini():
    # Menampilkan tanggal sekarang
    hari_ini = datetime.datetime.now()
    return format_date(hari_ini, format='full', locale='id_ID')

def tampilkan_waktu_sekarang():
    """
    Mengembalikan waktu sekarang dalam format: jam:menit:detik
    """
    waktu_sekarang = datetime.datetime.now().time()
    return f"Waktu saat ini: {waktu_sekarang.strftime('%H:%M:%S')}"

def buat_data_file():
    # Membuat file utama jika belum ada
    file_name = "data.txt"
    try:
        with open(file_name, "x") as file:
            pass
        print(f"File {file_name} berhasil dibuat.")
    except FileExistsError:
        print(" >>.Data file sudah siap")
        hitung_data()

def hitung_data():
    file_name = "data.txt"
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            data = file.readlines()
            # Menghitung hanya baris yang tidak kosong
            jumlah_data = sum(1 for line in data if line.strip())
            print(f" >> Jumlah data yang disimpan di database: {jumlah_data}")
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Kesalahan: {e}")

def read_and_clean_file(file_name):
    """
    Membaca file dan membersihkan data yang ada.
    Mengembalikan set pertanyaan yang sudah ada dan daftar baris yang sudah dibersihkan.
    """
    pertanyaan_set = set()
    cleaned_lines = []

    try:
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    try:
                        q, _ = stripped_line.split(" : ", 1)
                        if q not in pertanyaan_set:
                            pertanyaan_set.add(q)
                            cleaned_lines.append(stripped_line)
                    except ValueError:
                        print(f"Baris tidak valid: {stripped_line}")
                        continue
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan. File baru akan dibuat.")
    except Exception as e:
        print(f"Kesalahan saat membaca file: {e}")

    return pertanyaan_set, cleaned_lines

def write_sorted_data(file_name, lines):
    """
    Menulis data yang sudah diurutkan ke file.
    """
    try:
        with open(file_name, "w", encoding='utf-8') as file:
            for line in sorted(lines):
                file.write(line + "\n")
        print("Data disimpan dan file telah dirapikan serta diurutkan berdasarkan abjad.")
    except PermissionError:
        print(f"Anda tidak memiliki izin untuk menulis file {file_name}.")
    except Exception as e:
        print(f"Kesalahan saat menulis file: {e}")

def validate_input(pertanyaan, jawaban):
    """
    Memvalidasi input pertanyaan dan jawaban.
    Mengembalikan True jika valid, False jika tidak.
    """
    if not pertanyaan or not jawaban:
        print("Pertanyaan dan jawaban tidak boleh kosong.")
        return False
    if ":" in pertanyaan or "\n" in pertanyaan or ":" in jawaban or "\n" in jawaban:
        print("Pertanyaan dan jawaban tidak boleh mengandung karakter ':' atau newline.")
        return False
    return True

def edit_data_file(pertanyaan, jawaban):
    """
    Menambahkan pertanyaan dan jawaban baru ke file data.txt.
    Membersihkan dan mengurutkan file berdasarkan abjad.
    """
    file_name = "data.txt"

    # Validasi input
    if not validate_input(pertanyaan, jawaban):
        return

    # Membaca dan membersihkan file
    pertanyaan_set, cleaned_lines = read_and_clean_file(file_name)

    # Menambahkan data baru jika belum ada
    if pertanyaan not in pertanyaan_set:
        cleaned_lines.append(f"{pertanyaan} : {jawaban}")

    # Menulis data yang sudah diurutkan ke file
    write_sorted_data(file_name, cleaned_lines)

konteks = {}  # Variabel global untuk menyimpan konteks

def cari_jawaban(pertanyaan):
    global konteks
    try:
        with open("data.txt", "r") as file:
            jawaban_list = []
            for line in file.readlines():
                line = line.strip().lower()
                if " : " in line:
                    p, j = line.split(" : ")
                    if p in pertanyaan.lower():
                        jawaban_list = [x.strip() for x in j.split(" | ")]
            if jawaban_list:
                return random.choice(jawaban_list)
            else:
                # Cek apakah ada konteks sebelumnya
                if "terakhir" in pertanyaan.lower() and "terakhir" in konteks:
                    return konteks["terakhir"]
                print(f"chatboot: Wah, {data_nama}, sepertinya saya belum tahu jawabannya. Bisa kamu bantu saya dengan memberi tahu jawabannya?")
                
                while True:
                    jawaban_baru = input("jawaban: ")
                    if jawaban_baru.strip() != "":
                        edit_data_file(pertanyaan, jawaban_baru)
                        konteks["terakhir"] = jawaban_baru  # Simpan jawaban terakhir ke konteks
                        return jawaban_baru
                    else:
                        print("Jawaban tidak boleh kosong. Silakan coba lagi.")
    except FileNotFoundError:
        print("File data.txt tidak ditemukan.")
        return None
    except Exception as e:
        print(f"Kesalahan: {e}")
        return None
        
def main():
    # Program utama
    try:
        loading_proses(" >>.Menyalakan program!")
        print(" >>.Memuat modul yang dibutuhkan")
        cek_install_modul()
        buat_data_file()
        nama = input(" >>.Masukkan nama Anda: ")
        global data_nama
        data_nama = nama
        loading_proses(" >>.Memuat data: ")
        print(" >>.Semua data sudah siap:")
        time.sleep(2)
        hapus_layar()
        logo()
        print(salam_waktu(), data_nama)
        print("Ada yang bisa saya bantu?")
        while True:
            pertanyaan = input(nama + ': ').lower()
            if pertanyaan == "hari apa ini":
                print(tanggal_hariini())
            elif pertanyaan == "jam berapa sekarang":
                print(tampilkan_waktu_sekarang())
            elif pertanyaan == "hapus":
                hapus_layar()
            elif pertanyaan == "exit":
                print(f"chatboot: Terima kasih {data_nama}", cari_jawaban("exit"))
                exit()
            else:
                jawaban = cari_jawaban(pertanyaan)
                if jawaban:
                    print('chatboot:', jawaban)

    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
    except Exception as e:
        print(f"Kesalahan: {e}")

if __name__ == "__main__":
    main()
    