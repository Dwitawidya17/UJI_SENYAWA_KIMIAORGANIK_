import streamlit as st
import pandas as pd
import random

# DATA (dari gambar, sudah diketik manual sebelumnya — ringkas)
data = [
    {
        "Golongan": "Hidrokarbon",
        "Nama Uji": "Uji Pembakaran",
        "Hasil Positif": "Nyala kuning berasap",
        "Keterangan": "Aromatik"
    },
    {
        "Golongan": "Hidrokarbon",
        "Nama Uji": "Uji Bromin",
        "Hasil Positif": "Warna hilang",
        "Keterangan": "Adisi ikatan rangkap"
    },
    {
        "Golongan": "Alkohol Primer",
        "Nama Uji": "Uji Lucas",
        "Hasil Positif": "Tidak keruh / keruh lambat (>5 menit)",
        "Keterangan": "Lambat bereaksi dengan ZnCl2/HCl"
    },
    {
        "Golongan": "Fenol",
        "Nama Uji": "Uji Ferri Klorida",
        "Hasil Positif": "Warna ungu/biru",
        "Keterangan": "Fenol positif"
    },
    {
        "Golongan": "Aldehida",
        "Nama Uji": "Uji Tollens",
        "Hasil Positif": "Cermin perak",
        "Keterangan": "Aldehida positif"
    },
    {
        "Golongan": "Keton",
        "Nama Uji": "Uji Tollens",
        "Hasil Positif": "Negatif",
        "Keterangan": "Tidak bereaksi"
    },
    {
        "Golongan": "Protein",
        "Nama Uji": "Uji Biuret",
        "Hasil Positif": "Warna ungu",
        "Keterangan": "Ikatan peptida"
    },
    # Tambahkan data lain sesuai tabel aslinya...
]

df = pd.DataFrame(data)

# --- STREAMLIT APP ---
st.set_page_config(page_title="Uji Golongan Senyawa", layout="centered")

st.title("🧪 Uji Golongan Senyawa Organik")
st.write("Pilih golongan senyawa untuk melihat jenis uji, hasil positif, dan prinsip reaksinya.")

golongan_list = sorted(df['Golongan'].unique())
selected = st.selectbox("Pilih Golongan Senyawa:", golongan_list)

filtered = df[df["Golongan"] == selected]

st.subheader("📋 Hasil Uji:")
st.table(filtered[["Nama Uji", "Hasil Positif", "Keterangan"]])

# --- QUIZ SECTION ---
st.markdown("---")
st.subheader("🧠 Kuis Struktur Kimia")

quiz_data = {
    "struktur1.png": "Benzena",
    "struktur2.png": "Etanol",
    "struktur3.png": "Aseton",
}

img_file = random.choice(list(quiz_data.keys()))
st.image(f"images/{img_file}", caption="Struktur senyawa di atas")

answer = st.text_input("Apa nama senyawa tersebut?")
if answer:
    if answer.strip().lower() == quiz_data[img_file].lower():
        st.success("✅ Benar!")
    else:
        st.error(f"❌ Salah. Jawaban yang benar: {quiz_data[img_file]}")

# Footer
st.markdown("---")
st.markdown("🧬 Dibuat dengan ❤ menggunakan Streamlit")uji_senyawa_app/
│
├── app.py
├── images/
│   ├── struktur1.png
│   ├── struktur2.png
│   └── struktur3.png
└── requirements.txt
