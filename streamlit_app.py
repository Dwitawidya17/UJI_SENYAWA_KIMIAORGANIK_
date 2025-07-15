import streamlit as st
from PIL import Image
import random
import os

# ===================== DATA UJI SENYAWA =====================
senyawa_data = {
    "Hidrokarbon": [
        {"Nama Uji": "Uji Pembakaran", "Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
        {"Nama Uji": "Uji Baeyer", "Hasil Positif": "Warna ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"}
    ],
    "Alkohol Primer": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Tidak keruh / keruh lambat (>5 menit)", "Keterangan": "Lambat bereaksi dengan ZnCl₂/HCl"},
        {"Nama Uji": "Uji Kromik (Jones)", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi menjadi asam karboksilat"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi dengan logam Na"}
    ],
    "Alkohol Sekunder": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Keruh dalam ~5 menit", "Keterangan": "Reaksi sedang"},
        {"Nama Uji": "Uji Kromik", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi menjadi keton"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"}
    ],
    "Fenol": [
        {"Nama Uji": "Uji Ferri Klorida", "Hasil Positif": "Warna ungu/biru", "Keterangan": "Fenol positif"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Endapan putih tribromofenol", "Keterangan": "Substitusi brom"}
    ],
    "Aldehida": [
        {"Nama Uji": "Uji DNP", "Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"},
        {"Nama Uji": "Uji Tollens", "Hasil Positif": "Cermin perak", "Keterangan": "Aldehida positif"},
        {"Nama Uji": "Uji Fehling", "Hasil Positif": "Endapan merah bata", "Keterangan": "Aldehida positif"}
    ],
    "Keton": [
        {"Nama Uji": "Uji DNP", "Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"},
        {"Nama Uji": "Uji Tollens", "Hasil Positif": "Negatif", "Keterangan": "Tidak bereaksi"},
        {"Nama Uji": "Uji Fehling", "Hasil Positif": "Negatif", "Keterangan": "Tidak bereaksi"}
    ],
    "Asam Karboksilat": [
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus merah", "Keterangan": "Asam"},
        {"Nama Uji": "Uji NaHCO₃", "Hasil Positif": "Gelembung CO₂", "Keterangan": "Asam karboksilat"}
    ],
    "Amina Primer": [
        {"Nama Uji": "Uji Hinsberg", "Hasil Positif": "Larut setelah NaOH", "Keterangan": "Amina primer"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus biru", "Keterangan": "Basa"}
    ],
    "Protein": [
        {"Nama Uji": "Uji Biuret", "Hasil Positif": "Warna ungu", "Keterangan": "Ikatan peptida"},
        {"Nama Uji": "Uji Ninhidrin", "Hasil Positif": "Warna ungu/biru", "Keterangan": "Asam amino bebas"},
        {"Nama Uji": "Uji Xantoproteat", "Hasil Positif": "Warna kuning", "Keterangan": "Asam amino aromatik"}
    ],
    "Lemak & Minyak": [
        {"Nama Uji": "Uji Kertas", "Hasil Positif": "Noda transparan", "Keterangan": "Lemak/minyak positif"},
        {"Nama Uji": "Uji Baeyer", "Hasil Positif": "Warna ungu hilang jika tak jenuh", "Keterangan": "Lemak tak jenuh"}
    ]
}

# ===================== DATA KUIS STRUKTUR =====================
kuis_data = [
    {"gambar": "struktur_senyawa/etanol.png", "jawaban": "Etanol"},
    {"gambar": "struktur_senyawa/fenol.png", "jawaban": "Fenol"},
    {"gambar": "struktur_senyawa/asam_format.png", "jawaban": "Asam format"},
    {"gambar": "struktur_senyawa/anilin.png", "jawaban": "Anilin"},
    # Tambahkan file gambar lainnya di folder /struktur_senyawa
]

# ===================== TAMPILAN STREAMLIT =====================
st.set_page_config(page_title="Uji Golongan Senyawa", layout="wide")
st.title("🧪 Uji Golongan Senyawa Kimia")

st.markdown("Pilih golongan senyawa di bawah untuk melihat daftar uji, hasil positif, dan prinsip kerjanya.")

# Dropdown golongan senyawa
golongan = st.selectbox("🔍 Pilih Golongan Senyawa", list(senyawa_data.keys()))

st.subheader(f"Hasil Uji untuk: {golongan}")
for uji in senyawa_data[golongan]:
    with st.expander(uji["Nama Uji"]):
        st.markdown(f"**Hasil Positif:** {uji['Hasil Positif']}")
        st.markdown(f"**Prinsip/Keterangan:** {uji['Keterangan']}")

# ===================== KUIS STRUKTUR =====================
st.markdown("---")
st.subheader("🧬 Kuis Struktur Kimia")

kuis = random.choice(kuis_data)
if os.path.exists(kuis["gambar"]):
    gambar = Image.open(kuis["gambar"])
    st.image(gambar, caption="Tebak Nama Senyawa")
else:
    st.warning("Gambar tidak ditemukan.")

jawaban = st.text_input("Masukkan nama senyawa:")
if jawaban:
    if jawaban.lower().strip() == kuis["jawaban"].lower():
        st.success("✅ Benar!")
    else:
        st.error("❌ Salah. Coba lagi!")

st.markdown("---")
st.caption("© 2025 | Dibuat oleh Mahasiswa Kimia 👩‍🔬 dengan Streamlit")
