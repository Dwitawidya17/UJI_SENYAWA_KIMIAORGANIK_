import streamlit as st
import random
import pandas as pd
from PIL import Image
import os

# ===================== DATA UJI SENYAWA =====================
senyawa_data = {
    "Hidrokarbon": {
        "Uji Reaksi": [
            {"Nama Uji": "Uji Pembakaran", "Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
            {"Nama Uji": "Uji Bromin", "Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
            {"Nama Uji": "Uji Baeyer", "Hasil Positif": "Warna ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"}
        ],
        "Sifat Fisik & Kimia": [
            {"Nama Sifat": "Kelarutan", "Detail": "Tidak larut dalam air, larut dalam pelarut nonpolar", "Keterangan": "Hidrokarbon cenderung nonpolar"},
            {"Nama Sifat": "Titik Didih", "Detail": "Bervariasi, biasanya rendah untuk senyawa ringan", "Keterangan": "Ikatan antar molekul lemah"},
            {"Nama Sifat": "Kebasaan", "Detail": "Tidak bersifat basa", "Keterangan": "Tidak memiliki pasangan elektron bebas"}
        ]
    },
    "Alkohol Primer": {
        "Uji Reaksi": [
            {"Nama Uji": "Uji Lucas", "Hasil Positif": "Tidak keruh / lambat", "Keterangan": "Reaksi lambat dengan ZnCl₂/HCl"},
            {"Nama Uji": "Uji Kromik (Jones)", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi menjadi asam karboksilat"},
            {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"}
        ],
        "Sifat Fisik & Kimia": [
            {"Nama Sifat": "Kelarutan", "Detail": "Larut dalam air dan pelarut polar", "Keterangan": "Gugus –OH membuat molekul polar"},
            {"Nama Sifat": "Titik Didih", "Detail": "Tinggi dibanding hidrokarbon setara", "Keterangan": "Adanya ikatan hidrogen antar molekul"},
            {"Nama Sifat": "Kebasaan", "Detail": "Bersifat sangat lemah basa", "Keterangan": "Alkohol bukan basa kuat"}
        ]
    },
    "Fenol": {
        "Uji Reaksi": [
            {"Nama Uji": "Uji Ferri Klorida", "Hasil Positif": "Warna ungu/biru", "Keterangan": "Kompleks fenolat"},
            {"Nama Uji": "Uji Bromin", "Hasil Positif": "Endapan putih tribromofenol", "Keterangan": "Substitusi elektrofilik"}
        ],
        "Sifat Fisik & Kimia": [
            {"Nama Sifat": "Kelarutan", "Detail": "Agak larut dalam air", "Keterangan": "Interaksi gugus –OH dan cincin aromatik"},
            {"Nama Sifat": "Titik Didih", "Detail": "Lebih tinggi dari alkohol setara", "Keterangan": "Ikatan hidrogen dan struktur aromatik"},
            {"Nama Sifat": "Keasaman", "Detail": "Asam lemah", "Keterangan": "Stabilisasi resonansi anion fenoksida"}
        ]
    }
    # Tambahkan golongan lain sesuai kebutuhan
}

# ===================== FAKTA MENARIK =====================
fakta_menarik = [
    "🧴 Lemak jenuh tidak bereaksi dengan larutan Baeyer, tapi lemak tak jenuh bisa.",
    "🧪 Fenol memberikan warna ungu dengan FeCl₃, berbeda dari alkohol biasa.",
    "⚗ Uji Lucas membedakan alkohol primer, sekunder, dan tersier secara visual.",
    "💨 NaHCO₃ hanya bereaksi dengan asam kuat seperti asam karboksilat.",
    "🔬 Biuret test hanya positif jika terdapat dua atau lebih ikatan peptida.",
]

# ===================== DATA TABEL PERIODIK (30 unsur) =====================
periodic_data = [
    {"Unsur": "H",  "Nama": "Hidrogen",     "No Atom": 1,  "Simbol": "H",  "Golongan": "Non-logam",          "Massa Atom": 1.008,    "Keterangan": "Gas ringan, penyusun utama air."},
    {"Unsur": "He", "Nama": "Helium",       "No Atom": 2,  "Simbol": "He", "Golongan": "Gas mulia",          "Massa Atom": 4.0026,   "Keterangan": "Gas inert, digunakan pada lampu neon."},
    {"Unsur": "Li", "Nama": "Litium",       "No Atom": 3,  "Simbol": "Li", "Golongan": "Logam alkali",       "Massa Atom": 6.94,     "Keterangan": "Logam lunak, reaktif."},
    {"Unsur": "Be", "Nama": "Berilium",     "No Atom": 4,  "Simbol": "Be", "Golongan": "Logam alkali tanah", "Massa Atom": 9.0122,   "Keterangan": "Logam keras, titik leleh tinggi."},
    {"Unsur": "B",  "Nama": "Boron",        "No Atom": 5,  "Simbol": "B",  "Golongan": "Semilogam",           "Massa Atom": 10.81,    "Keterangan": "Semilogam dengan sifat unik."},
    {"Unsur": "C",  "Nama": "Karbon",       "No Atom": 6,  "Simbol": "C",  "Golongan": "Non-logam",           "Massa Atom": 12.011,   "Keterangan": "Dasar kehidupan organik."},
    {"Unsur": "N",  "Nama": "Nitrogen",     "No Atom": 7,  "Simbol": "N",  "Golongan": "Non-logam",           "Massa Atom": 14.007,   "Keterangan": "Komponen utama atmosfer."},
    {"Unsur": "O",  "Nama": "Oksigen",      "No Atom": 8,  "Simbol": "O",  "Golongan": "Non-logam",           "Massa Atom": 15.999,   "Keterangan": "Penting untuk respirasi."},
    {"Unsur": "F",  "Nama": "Fluorin",      "No Atom": 9,  "Simbol": "F",  "Golongan": "Halogen",             "Massa Atom": 18.998,   "Keterangan": "Gas sangat reaktif."},
    {"Unsur": "Ne", "Nama": "Neon",         "No Atom": 10, "Simbol": "Ne", "Golongan": "Gas mulia",          "Massa Atom": 20.180,   "Keterangan": "Gas inert, digunakan dalam lampu neon."},
    {"Unsur": "Na", "Nama": "Natrium",      "No Atom": 11, "Simbol": "Na", "Golongan": "Logam alkali",       "Massa Atom": 22.990,   "Keterangan": "Logam lunak, bereaksi keras dengan air."},
    {"Unsur": "Mg", "Nama": "Magnesium",    "No Atom": 12, "Simbol": "Mg", "Golongan": "Logam alkali tanah", "Massa Atom": 24.305,   "Keterangan": "Berperan dalam klorofil tanaman."},
    {"Unsur": "Al", "Nama": "Aluminium",    "No Atom": 13, "Simbol": "Al", "Golongan": "Logam pasca transisi", "Massa Atom": 26.982, "Keterangan": "Ringan dan anti karat."},
    {"Unsur": "Si", "Nama": "Silikon",      "No Atom": 14, "Simbol": "Si", "Golongan": "Semilogam",           "Massa Atom": 28.085,   "Keterangan": "Penting dalam semikonduktor elektronik."},
    {"Unsur": "P",  "Nama": "Fosfor",       "No Atom": 15, "Simbol": "P",  "Golongan": "Non-logam",           "Massa Atom": 30.974,   "Keterangan": "Digunakan dalam pupuk."},
    {"Unsur": "S",  "Nama": "Belerang",     "No Atom": 16, "Simbol": "S",  "Golongan": "Non-logam",           "Massa Atom": 32.06,    "Keterangan": "Digunakan dalam produksi asam sulfat."},
    {"Unsur": "Cl", "Nama": "Klorin",       "No Atom": 17, "Simbol": "Cl", "Golongan": "Halogen",             "Massa Atom": 35.45,    "Keterangan": "Sterilizer dan pemutih air."},
    {"Unsur": "Ar", "Nama": "Argon",        "No Atom": 18, "Simbol": "Ar", "Golongan": "Gas mulia",          "Massa Atom": 39.948,   "Keterangan": "Gas inert, digunakan dalam pengelasan."},
    {"Unsur": "K",  "Nama": "Kalium",       "No Atom": 19, "Simbol": "K",  "Golongan": "Logam alkali",       "Massa Atom": 39.098,   "Keterangan": "Elemen penting untuk fungsi saraf."},
    {"Unsur": "Ca", "Nama": "Kalsium",      "No Atom": 20, "Simbol": "Ca", "Golongan": "Logam alkali tanah", "Massa Atom": 40.078,   "Keterangan": "Pembentuk tulang dan gigi."},
    {"Unsur": "Sc", "Nama": "Skandium",     "No Atom": 21, "Simbol": "Sc", "Golongan": "Logam transisi",     "Massa Atom": 44.956,   "Keterangan": "Digunakan pada lampu halida logam."},
    {"Unsur": "Ti", "Nama": "Titanium",     "No Atom": 22, "Simbol": "Ti", "Golongan": "Logam transisi",     "Massa Atom": 47.867,   "Keterangan": "Ringan, kuat, anti karat."},
    {"Unsur": "V",  "Nama": "Vanadium",     "No Atom": 23, "Simbol": "V",  "Golongan": "Logam transisi",     "Massa Atom": 50.942,   "Keterangan": "Digunakan dalam paduan logam."},
    {"Unsur": "Cr", "Nama": "Kromium",      "No Atom": 24, "Simbol": "Cr", "Golongan": "Logam transisi",     "Massa Atom": 51.996,   "Keterangan": "Memberikan lapisan anti karat."},
    {"Unsur": "Mn", "Nama": "Mangan",       "No Atom": 25, "Simbol": "Mn", "Golongan": "Logam transisi",     "Massa Atom": 54.938,   "Keterangan": "Digunakan dalam baja tuang."},
    {"Unsur": "Fe", "Nama": "Besi",         "No Atom": 26, "Simbol": "Fe", "Golongan": "Logam transisi",     "Massa Atom": 55.845,   "Keterangan": "Elemen logam yang umum pada baja."},
    {"Unsur": "Co", "Nama": "Kobalt",       "No Atom": 27, "Simbol": "Co", "Golongan": "Logam transisi",     "Massa Atom": 58.933,   "Keterangan": "Digunakan dalam baterai dan magnet."},
    {"Unsur": "Ni", "Nama": "Nikel",        "No Atom": 28, "Simbol": "Ni", "Golongan": "Logam transisi",     "Massa Atom": 58.693,   "Keterangan": "Sering dipakai untuk pelapis anti karat."},
    {"Unsur": "Cu", "Nama": "Tembaga",      "No Atom": 29, "Simbol": "Cu", "Golongan": "Logam transisi",     "Massa Atom": 63.546,   "Keterangan": "Konduktor listrik yang baik."},
    {"Unsur": "Zn", "Nama": "Seng",         "No Atom": 30, "Simbol": "Zn", "Golongan": "Logam transisi",     "Massa Atom": 65.38,    "Keterangan": "Digunakan sebagai pelindung baja dari karat."}
]
df_periodic = pd.DataFrame(periodic_data)

# ========== DATA STRUKTUR & REAKSI KIMIA ORGANIK ==========
struktur_reaksi = {
    "Hidrokarbon": {
        "gambar": "struktur/hidrokarbon.png",
        "reaksi": "Pembakaran menghasilkan CO₂ dan H₂O.\nReaksi adisi pada ikatan rangkap.",
        "deskripsi": "Hidrokarbon adalah senyawa yang hanya tersusun dari atom karbon dan hidrogen."
    },
    "Alkohol Primer": {
        "gambar": "struktur/alkohol_primer.png",
        "reaksi": "Oksidasi alkohol primer menghasilkan aldehida dan asam karboksilat.",
        "deskripsi": "Alkohol primer memiliki gugus –OH pada karbon primer."
    },
    "Fenol": {
        "gambar": "struktur/fenol.png",
        "reaksi": "Reaksi dengan FeCl₃ membentuk warna ungu.\nReaksi substitusi elektrofilik cincin aromatik.",
        "deskripsi": "Fenol memiliki gugus –OH yang langsung terikat pada cincin benzena."
    }
    # Tambahkan jika perlu
}

# ========== SETUP STREAMLIT ==========
st.set_page_config(page_title="Uji Senyawa Kimia", layout="wide")

tab1_uji, tab2_sifat, tab3_kuis, tab4_periodik, tab5_struktur = st.tabs([
    "🔍 Uji Reaksi", 
    "💧 Sifat Fisik & Kimia", 
    "🧠 Kuis Kimia", 
    "🧪 Tabel Periodik", 
    "⚗ Struktur & Reaksi"
])

# Tab 1 - Uji Reaksi
with tab1_uji:
    st.header("Uji Reaksi Senyawa")
    selected = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()), key="uji_reaksi_golongan")
    reaksi_list = senyawa_data[selected].get("Uji Reaksi", [])
    if reaksi_list:
        for uji in reaksi_list:
            with st.expander(uji["Nama Uji"], expanded=False):
                st.write(f"**Hasil Positif**: {uji['Hasil Positif']}")
                st.write(f"**Keterangan**: {uji['Keterangan']}")
    else:
        st.info("Data uji reaksi belum tersedia untuk golongan ini.")

# Tab 2 - Sifat Fisik & Kimia
with tab2_sifat:
    st.header("Sifat Fisik & Kimia Senyawa")
    selected2 = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()), key="sifat_kimia_golongan")
    sifat_list = senyawa_data[selected2].get("Sifat Fisik & Kimia", [])
    if sifat_list:
        for sifat in sifat_list:
            with st.expander(sifat["Nama Sifat"], expanded=False):
                st.write(f"**Detail**: {sifat['Detail']}")
                st.write(f"**Keterangan**: {sifat['Keterangan']}")
    else:
        st.info("Data sifat fisik & kimia belum tersedia untuk golongan ini.")

# Tab 3 - Kuis Kimia
with tab3_kuis:
    st.header("Kuis Golongan Senyawa")
    semua_uji = []
    for golongan, data in senyawa_data.items():
        for item in data.get("Uji Reaksi", []):
            soal = item.copy()
            soal["Golongan"] = golongan
            semua_uji.append(soal)
    jumlah_soal = min(10, len(semua_uji))
    if "soal_kuis" not in st.session_state:
        st.session_state["soal_kuis"] = random.sample(semua_uji, k=jumlah_soal)
        st.session_state["opsi_kuis"] = []
        for soal in st.session_state["soal_kuis"]:
            opsi = set([soal["Golongan"]])
            while len(opsi) < 4:
                opsi.add(random.choice(list(senyawa_data.keys())))
            opsi = list(opsi)
            random.shuffle(opsi)
            st.session_state["opsi_kuis"].append(opsi)
    jawaban_pengguna = {}
    for i, soal in enumerate(st.session_state["soal_kuis"], 1):
        st.markdown(f"**Soal {i}:** Uji **{soal['Nama Uji']}** menghasilkan **{soal['Hasil Positif']}**. Golongan senyawa apa ini?")
        opsi = st.session_state["opsi_kuis"][i - 1]
        jawaban = st.radio("Pilih Golongan:", opsi, key=f"kuis_{i}")
        jawaban_pengguna[f"soal_{i}"] = {"jawaban": jawaban, "benar": soal["Golongan"]}
    if st.button("Submit Jawaban"):
        benar = sum(jawaban_pengguna[k]["jawaban"] == jawaban_pengguna[k]["benar"] for k in jawaban_pengguna)
        skor = (benar / jumlah_soal) * 100
        st.success(f"Kamu benar {benar} dari {jumlah_soal} soal.")
        st.info(f"Skor kamu: {skor:.2f}%")
        salah = [(k, v["jawaban"], v["benar"]) for k, v in jawaban_pengguna.items() if v["jawaban"] != v["benar"]]
        if salah:
            st.warning("Jawaban salah:")
            for s in salah:
                st.write(f"- {s[0]}: Jawabanmu **{s[1]}**, seharusnya **{s[2]}**")
        st.markdown("---")
        st.subheader("💡 Fakta Menarik Kimia")
        st.info(random.choice(fakta_menarik))

# Tab 4 - Tabel Periodik
with tab4_periodik:
    st.header("Informasi Tabel Periodik")
    pilihan = st.selectbox("Pilih Unsur:", df_periodic["Unsur"] + " - " + df_periodic["Nama"])
    simbol = pilihan.split(" - ")[0]
    data_unsur = df_periodic[df_periodic["Unsur"] == simbol].iloc[0]
    st.write(f"**Nama:** {data_unsur['Nama']}")
    st.write(f"**Simbol:** {data_unsur['Simbol']}")
    st.write(f"**Nomor Atom:** {data_unsur['No Atom']}")
    st.write(f"**Golongan:** {data_unsur['Golongan']}")
    st.write(f"**Massa Atom:** {data_unsur['Massa Atom']}")
    st.write(f"**Keterangan:** {data_unsur['Keterangan']}")

# Tab 5 - Struktur dan Reaksi Kimia Organik
with tab5_struktur:
    st.header("Struktur dan Reaksi Kimia Organik")
    pilihan_struktur = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()))
    if pilihan_struktur in struktur_reaksi:
        data = struktur_reaksi[pilihan_struktur]
        st.subheader(f"Struktur Kimia: {pilihan_struktur}")
        img_path = data['gambar']
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, width=300)
        else:
            st.warning(f"Gambar '{img_path}' belum tersedia, mohon tambahkan pada folder 'struktur/'.")
        st.markdown("**Deskripsi:**")
        st.write(data["deskripsi"])
        st.markdown("**Reaksi:**")
        st.code(data["reaksi"])
    else:
        st.info("Data struktur dan reaksi belum tersedia untuk golongan ini.")

# Footer
st.markdown("---")
st.caption("© 2025 | Uji Senyawa Kimia Interaktif by Streamlit 🎓")
