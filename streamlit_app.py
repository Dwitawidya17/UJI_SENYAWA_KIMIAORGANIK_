import streamlit as st
import random

# Data golongan senyawa dan uji
data = {
    "Hidrokarbon": {
        "Uji Pembakaran": {"Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
        "Uji Bromin": {"Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
        "Uji Baeyer": {"Hasil Positif": "Warna ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"}
    },
    # (Lengkapi dengan data lain sesuai kebutuhan, data selengkapnya bisa disalin dari balasan sebelumnya)
}

# Fakta menarik (contoh untuk fitur tambahan)
fun_facts = [
    "Uji Tollens dikenal juga sebagai uji cermin perak karena menghasilkan endapan perak mengkilap.",
    "Fenol memberikan warna ungu dengan larutan FeCl3, berbeda dengan alkohol.",
    "Tidak semua alkohol bereaksi dengan uji Lucas dalam waktu yang sama, tergantung strukturnya.",
    "Gula dapat diidentifikasi dengan uji Benedict yang menghasilkan warna merah bata."
]

# Interface utama
st.set_page_config(page_title="Uji Kimia Interaktif", layout="centered")
st.title("🔬 Uji Kimia Golongan Senyawa Organik")
st.caption("Eksplorasi interaktif uji-uji golongan senyawa, dilengkapi fakta menarik dan quiz singkat!")

# Fitur pencarian cepat
search = st.text_input("🔎 Cari Golongan atau Uji...", "")

# Tampilkan fakta menarik di bagian atas untuk menarik perhatian
if st.checkbox("Tampilkan Fakta Menarik?"):
    st.info(random.choice(fun_facts))

# Daftar golongan bisa difilter via input pencarian
filtered_golongan = [k for k in data.keys() if search.lower() in k.lower() or any(search.lower() in u.lower() for u in data[k].keys())] if search else list(data.keys())
golongan = st.selectbox("Pilih Golongan Senyawa:", filtered_golongan)

if golongan:
    # Pilihan Nama Uji juga bisa difilter
    filtered_uji = [u for u in data[golongan] if search.lower() in u.lower()] if search else list(data[golongan].keys())
    nama_uji = st.selectbox("Pilih Nama Uji:", filtered_uji)
    
    if nama_uji:
        hasil = data[golongan][nama_uji]
        st.success(f"*Hasil Positif:* {hasil['Hasil Positif']}")
        st.write(f"*Keterangan / Prinsip:* {hasil['Keterangan']}")
        
        # Tooltip istilah teknis
        with st.expander("Penjelasan Istilah Teknis"):
            if "cermin perak" in hasil["Hasil Positif"].lower():
                st.write("- *Cermin perak:* Endapan perak pada dinding tabung reaksi hasil reduksi ion Ag⁺.")
            if "endapan merah bata" in hasil["Hasil Positif"].lower():
                st.write("- *Endapan merah bata:* Endapan Cu2O pada uji gula reduksi.")

        # Fitur komentar sederhana menggunakan st.text_area
        st.subheader("💬 Kirim Komentar atau Saran")
        feedback = st.text_area("Tulis komentar...")
        if st.button("Kirim"):
            st.write("Terima kasih atas masukan Anda!")

# Mini Quiz Singkat (opsional)
if st.checkbox("Quiz: Uji Senyawa?"):
    quiz = [
        {"tanya": "Uji mana yang menghasilkan 'cermin perak'?", "jawaban": "Uji Tollens", "opsi": ["Uji Fehling", "Uji Tollens", "Uji Lucas"]},
        {"tanya": "Golongan mana yang memberikan warna ungu pada uji Biuret?", "jawaban": "Protein", "opsi": ["Karbohidrat", "Protein", "Amina"]},
    ]
    soal = random.choice(quiz)
    st.write(soal["tanya"])
    ans = st.radio("Pilih jawaban:", soal["opsi"])
    if st.button("Cek Jawaban!"):
        if ans == soal["jawaban"]:
            st.success("Benar! 🎉")
        else:
            st.error("Jawaban Salah.")
