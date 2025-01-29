import time
import datetime
import sys
import shutil
import os

def hapus_layar():
    # penghapus layar
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS dan Linux
        os.system("clear")

def logo():
    # fungsi logo
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
    # fungsi loading
    print(teks)
    for i in range(waktu+1):
        proses = i * 10
        sys.stdout.write("\r >>.Proses: [{}{}] {}%".format("#" * (proses // 10), "-" * (10 - proses // 10), proses))
        sys.stdout.flush()
        time.sleep(1)
    print("\nMulai !")
    
def salam_waktu():
    jam_sekarang = datetime.datetime.now().hour
    if 1 <= jam_sekarang <= 9:
        return "Selamat pagi!"
    elif 10 <= jam_sekarang <= 12:
        return "Selamat siang!"
    elif 13 <= jam_sekarang <= 15:
        return "Selamat siang!"
    elif 16 <= jam_sekarang <= 18:
        return "Selamat sore!"
    else:
        return "Selamat malam!"

def buat_data_file():
    # Membuat file jika belum ada
    file_name = "data.txt"
    try:
        with open(file_name, "x") as file:
            pass
        print(f"File {file_name} berhasil dibuat.")
    except FileExistsError:
        print(f"File {file_name} sudah ada.")
        
def edit_data_file(pertanyaan,jawaban):
    # fungsi Menambah isi file
    file_name = "data.txt"
    with open(file_name, "a") as file:
        file.write(f"{pertanyaan}:{jawaban}\n")
        print(f"Data berhasil ditambahkan ke file {file_name}.")

def cari_jawaban(pertanyaan):
    #mendapatkan jawaban
    try:
        with open("data.txt", "r") as file:
            for line in file:
                p, j = line.strip().split(":")
                if p.lower() == pertanyaan.lower():
                    return j
    except FileNotFoundError:
        print("File data.txt tidak ditemukan.")
        return None
        
def main ():
	loading_proses(" >>.memuat data: ",)
	time.sleep(2)
	hapus_layar()
	logo()
	print(salam_waktu())
	print("ada yang bisa saya bantu ?")
	#while True:
		
		
	
	
	
if __name__ == "__main__":
		main()
		

