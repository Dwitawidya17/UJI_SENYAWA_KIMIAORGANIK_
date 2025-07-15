import streamlit as st
import pandas as pd
import random
from PIL import Image

# Load data tabel uji
data = pd.read_csv("data.csv")

# Load soal kuis
import json
with open("kuis_data.json") as f:
    kuis_data = json.load(f)

st.set_page_config(
    page_title="Uji Golongan Senyawa",
    page_icon="🧪",
    layout="wide",
)

st.title("🧪 Uji Golongan Senyawa Organik")
st.markdown("""
Pilih golongan senyawa untuk melihat detail uji, hasil positif, dan prinsipnya.
""")

# Pilihan dropdown
golongan_list = data["Golongan Senyawa"].unique()
golongan_pilihan = st.selectbox("Pilih Golongan Senyawa", golongan_list)

# Filter data
filtered = data[data["Golongan Senyawa"] == golongan_pilihan]

# Tampilkan tabel
st.subheader(f"Detail Uji untuk: {golongan_pilihan}")
st.table(filtered[["Nama Uji", "Hasil Positif", "Keterangan / Prinsip"]])

# Gambar struktur kimia opsional
st.subheader("Struktur Kimia Contoh")
struktur_path = f"images/{golongan_pilihan.lower().replace(' ', '_')}.png"
try:
    image = Image.open(struktur_path)
    st.image(image, caption=f"Struktur Kimia {golongan_pilihan}")
except FileNotFoundError:
    st.warning("Belum ada gambar struktur.")

# Kuis
st.subheader("📝 Kuis Interaktif")

soal = random.choice(kuis_data)
st.write(f"**{soal['pertanyaan']}**")

jawaban = st.radio("Pilih jawaban:", soal["opsi"])

if st.button("Cek Jawaban"):
    if jawaban == soal["jawaban_benar"]:
        st.success("✅ Jawaban Benar!")
    else:
        st.error(f"❌ Jawaban Salah. Jawaban yang benar: {soal['jawaban_benar']}")

# Footer
st.markdown("---")
st.caption("Aplikasi edukasi kimia - Streamlit + Python")
