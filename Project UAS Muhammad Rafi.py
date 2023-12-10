from datetime import datetime

def jalankan_quiz(quiz_number, pertanyaan):
    print(f"**Quiz {quiz_number}**")
    nilai = 0

    for i, (pertanyaan_text, opsi, jawaban_benar) in enumerate(pertanyaan, start=1):
        print(f"\n**Pertanyaan {i}**\n\n{pertanyaan_text}")
        for option in opsi:
            print(f"{option[0]}. {option[1]}")

        while True:
            jawaban = input("\nMasukkan jawaban Anda: ")
            if jawaban.lower() in [str(option[0].lower()) for option in opsi]:
                break
            else:
                print("Isi jawaban sesuai dengan pilihan!")

        if jawaban.lower() == jawaban_benar.lower():
            nilai += 25

    return nilai

def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r") as f:
            for line in f:
                data.append(tuple(line.strip().split("|")))
    except FileNotFoundError:
        pass
    return data

def tulis_data(nama_file, data):
    with open(nama_file, "w") as f:
        for entry in data:
            if len(entry) == 3:
                f.write(f"{entry[0]}|{entry[1]}|{entry[2]}\n")

def is_valid_name(name): 
     return all(character.isalpha() or character.isspace() for character in name)

file_quiz1 = "quiz1.txt"
file_quiz2 = "quiz2.txt"
file_quiz3 = "quiz3.txt"

pertanyaan_quiz1 = [
    ("Apa itu PEP 8 dalam konteks Python?", [("a", "Versi Python terbaru"), ("b", "Panduan gaya penulisan kode Python"), ("c", "Fungsi built-in dalam Python"), ("d", "Modul standar Python")], "b"),
    ("Apa fungsi dari method append() pada list Python?", [("a", "Menambahkan elemen ke dalam list"), ("b", "Mengurangi panjang list"), ("c", "Menghapus elemen list"), ("d", "Mengurutkan list")], "a"),
    ("Apa output dari print(2 ** 3)?", [("a", "6"), ("b", "9"), ("c", "8"), ("d", "16")], "c"),
    ("Apakah Python case-sensitive?", [("a", "Ya"), ("b", "Tidak"), ("c", "Kadang-kadang"), ("d", "Bergantung pada versi Python")], "a"),
]

pertanyaan_quiz2 = [
    ("Apa singkatan dari HTML?", [("a", "Hyper Transfer Markup Language"), ("b", "Hyper Text Markup Language"), ("c", "High Transfer Markup Language"), ("d", "Hyperlink Text Markup Language")], "b"),
    ("Mana dari pernyataan berikut yang benar tentang tag HTML <br>?", [("a", "Ini adalah tag untuk membuat gambar"), ("b", "Ini adalah tag untuk membuat hyperlink"), ("c", "Ini adalah tag untuk membuat baris baru"), ("d", "Ini adalah tag untuk membuat teks tebal")], "c"),
    ("Apa fungsi dari elemen <img> dalam HTML?", [("a", "Untuk menampilkan gambar di halaman web"), ("b", "Untuk membuat tabel di halaman web"), ("c", "Untuk menampilkan teks tebal di halaman web"), ("d", "Untuk membuat hyperlink di halaman web")], "a"),
    ("Apa yang dilakukan oleh tag <a> dalam HTML?", [("a", "Membuat daftar terurut (ordered list)"), ("b", "Membuat hyperlink ke halaman web lain atau ke bagian yang sama dari halaman"), ("c", "Membuat teks menjadi tebal"), ("d", "Membuat gambar menjadi lebih besar")], "b"),
]

pertanyaan_quiz3 = [
    ("Apa output dari pernyataan 'console.log(typeof 42)'?", [("a", "Number"), ("b", "String"), ("c", "Boolean"), ("d", "Object")], "a"),
    ("Bagaimana cara mendapatkan panjang (jumlah elemen) dari 'array myArray' di JavaScript?", [("a", "myArray.length()"), ("b", "myArray.size()"), ("c", "myArray.count()"), ("d", "myArray.length")], "d"),
    ("Apa yang akan menjadi hasil dari operasi 2 + '2' dalam JavaScript?", [("a", "22"), ("b", "4"), ("c", "'22'"), ("d", "Error")], "c"),
    ("Bagaimana cara mendeklarasikan variabel yang tidak dapat diubah nilainya (konstan) di JavaScript?", [("a", "const myVar;"), ("b", "let myVar;"), ("c", "constant myVar;"), ("d", "const myVar = 10;")], "d"),
]
while True:
    print("Quiz Pemrograman")
    nama = input("Masukkan nama Anda: ")

    if not is_valid_name(nama):
        print("Nama hanya boleh berisi huruf, Harap masukkan kembali.")
        continue

    waktu_mulai = datetime.now()

    print("\nPilih tipe quiz:")
    print("1. Quiz Python")
    print("2. Quiz html")
    print("3. Quiz JavaScript")

    while True:
        pilihan_quiz = input("Masukkan pilihan Anda (1/2/3): ")
        if pilihan_quiz == "" or pilihan_quiz not in ["1", "2", "3"]:
            print("Pilihan tidak valid. Harap masukkan angka 1, 2, atau 3.")
        else:
            break

    if pilihan_quiz == "1":
        nilai = jalankan_quiz(1, pertanyaan_quiz1)
        nama_file = file_quiz1
    elif pilihan_quiz == "2":
        nilai = jalankan_quiz(2, pertanyaan_quiz2)
        nama_file = file_quiz2
    elif pilihan_quiz == "3":
        nilai = jalankan_quiz(3, pertanyaan_quiz3)
        nama_file = file_quiz3

    waktu_selesai = datetime.now()
    
    data_pemain = baca_data(nama_file)
    data_pemain.append((nama, nilai, waktu_mulai.strftime("%H:%M")))
    tulis_data(nama_file, data_pemain)

    print("\n**Hasil Quiz**")
    for i, entry in enumerate(data_pemain, start=1):
        if len(entry) == 3:
            print(f"{i}. {entry[0]} (nilai: {entry[1]}) - {entry[2]}")

    while True:
        tanya = input("Apakah ingin bermain lagi (Y/N): ")
        if tanya == "":
            print("Isi sesuai opsi")
        elif tanya.lower() not in ["y", "n"]:
            print("Isi jawaban sesuai dengan pilihan!")
        else:
            break

    if tanya.lower() == "n":
        print("Terima kasih telah bermain!")
        break
