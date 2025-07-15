import streamlit as st
import random
import pandas as pd
from PIL import Image
import os

# ===== DATA =====
senyawa_data = {
    "Hidrokarbon": [
        {"Nama Uji": "Uji Pembakaran", "Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
        {"Nama Uji": "Uji Baeyer", "Hasil Positif": "Warna ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"}
    ],
    "Alkohol Primer": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Tidak keruh / lambat", "Keterangan": "Reaksi lambat dengan ZnCl₂/HCl"},
        {"Nama Uji": "Uji Kromik (Jones)", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi → asam karboksilat"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"}
    ],
    "Fenol": [
        {"Nama Uji": "Uji Ferri Klorida", "Hasil Positif": "Warna ungu/biru", "Keterangan": "Kompleks fenolat"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Endapan putih tribromofenol", "Keterangan": "Substitusi elektrofilik"}
    ]
    # Bisa ditambah lagi ...
}

fakta_menarik = [
    "🧴 Lemak jenuh tidak bereaksi dengan larutan Baeyer, tapi lemak tak jenuh bisa.",
    "🧪 Fenol memberikan warna ungu dengan FeCl₃, berbeda dari alkohol biasa.",
    "⚗ Uji Lucas membedakan alkohol primer, sekunder, dan tersier secara visual.",
    "💨 NaHCO₃ hanya bereaksi dengan asam kuat seperti asam karboksilat.",
    "🔬 Biuret test hanya positif jika terdapat dua atau lebih ikatan peptida.",
]

periodic_data = [
    {"Unsur": "H", "Nama": "Hidrogen", "No Atom": 1, "Simbol": "H", "Golongan": "Non-logam", "Massa Atom": 1.008, "Keterangan": "Gas tidak berwarna dan sangat ringan."},
    {"Unsur": "He", "Nama": "Helium", "No Atom": 2, "Simbol": "He", "Golongan": "Gas mulia", "Massa Atom": 4.0026, "Keterangan": "Gas inert, digunakan dalam balon udara."},
    {"Unsur": "C", "Nama": "Karbon", "No Atom": 6, "Simbol": "C", "Golongan": "Non-logam", "Massa Atom": 12.011, "Keterangan": "Elemen dasar kehidupan."},
    {"Unsur": "O", "Nama": "Oksigen", "No Atom": 8, "Simbol": "O", "Golongan": "Non-logam", "Massa Atom": 15.999, "Keterangan": "Diperlukan untuk respirasi."}
]
df_periodic = pd.DataFrame(periodic_data)

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
}

# ===== STREAMLIT APP =====
st.set_page_config(page_title="Uji Senyawa Kimia", layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(["🔍 Uji Senyawa", "🧠 Kuis Kimia", "🧪 Tabel Periodik", "⚗ Struktur & Reaksi"])

# -- Tab 1 --
with tab1:
    st.title("🔬 Uji Golongan Senyawa Kimia")
    st.markdown("Pilih golongan senyawa untuk melihat jenis uji, hasil positif, dan keterangannya.")

    selected = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()))
    st.subheader(f"📋 Hasil Uji untuk: {selected}")

    for uji in senyawa_data[selected]:
        with st.expander(uji["Nama Uji"]):
            st.markdown(f"**Hasil Positif:** {uji['Hasil Positif']}")
            st.markdown(f"**Keterangan:** {uji['Keterangan']}")

# -- Tab 2 --
with tab2:
    st.title("🧠 Kuis Golongan Senyawa")

    semua_uji = []
    for gol, daftar_uji in senyawa_data.items():
        for uji in daftar_uji:
            semua_uji.append({**uji, "Golongan": gol})

    jumlah_soal = min(10, len(semua_uji))

    if "soal_kuis" not in st.session_state:
        st.session_state["soal_kuis"] = random.sample(semua_uji, k=jumlah_soal)
        st.session_state["opsi_kuis"] = []
        for soal in st.session_state["soal_kuis"]:
            opsi = random.sample(list(senyawa_data.keys()), 4)
            if soal["Golongan"] not in opsi:
                opsi[random.randint(0, 3)] = soal["Golongan"]
            random.shuffle(opsi)
            st.session_state["opsi_kuis"].append(opsi)

    jawaban_pengguna = {}

    for i, soal in enumerate(st.session_state["soal_kuis"], 1):
        st.markdown(f"**Soal {i}:** {soal['Nama Uji']} → Hasil: {soal['Hasil Positif']}")
        opsi = st.session_state["opsi_kuis"][i - 1]
        jawaban = st.radio("Pilih Golongan:", opsi, key=f"soal_{i}")
        jawaban_pengguna[f"soal_{i}"] = {"jawaban": jawaban, "benar": soal["Golongan"]}

    if st.button("📤 Submit Jawaban"):
        benar = sum(1 for k in jawaban_pengguna if jawaban_pengguna[k]["jawaban"] == jawaban_pengguna[k]["benar"])
        skor = (benar / jumlah_soal) * 100
        st.success(f"Tepat menjawab {benar} dari {jumlah_soal} soal.")
        st.info(f"Skor: {skor:.2f}%")

        salah = [(k, v["jawaban"], v["benar"]) for k, v in jawaban_pengguna.items() if v["jawaban"] != v["benar"]]
        if salah:
            st.warning("Jawaban salah:")
            for s in salah:
                st.write(f"- {s[0]}: Jawabanmu {s[1]}, seharusnya {s[2]}")

        st.markdown("---")
        st.subheader("💡 Fakta Menarik")
        st.info(random.choice(fakta_menarik))

# -- Tab 3 --
with tab3:
    st.title("🧪 Tabel Periodik Unsur")
    st.markdown("Pilih unsur untuk info lengkap.")

    pilihan = st.selectbox("Pilih Unsur:", df_periodic["Unsur"] + " - " + df_periodic["Nama"])
    simbol = pilihan.split(" - ")[0]
    data_unsur = df_periodic[df_periodic["Unsur"] == simbol].iloc[0]

    st.write(f"**Nama:** {data_unsur['Nama']}")
    st.write(f"**Simbol:** {data_unsur['Simbol']}")
    st.write(f"**Nomor Atom:** {data_unsur['No Atom']}")
    st.write(f"**Golongan:** {data_unsur['Golongan']}")
    st.write(f"**Massa Atom:** {data_unsur['Massa Atom']}")
    st.write(f"**Keterangan:** {data_unsur['Keterangan']}")

# -- Tab 4 --
with tab4:
    st.title("⚗ Struktur dan Reaksi Kimia Organik")

    pilihan_struktur = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()))

    if pilihan_struktur in struktur_reaksi:
        data = struktur_reaksi[pilihan_struktur]
        st.subheader(f"Struktur Kimia: {pilihan_struktur}")
        img_path = data['gambar']
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, width=300)
        else:
            st.warning(f"Gambar '{img_path}' belum tersedia. Silakan tambahkan pada folder 'struktur/'.")

        st.markdown("**Deskripsi:**")
        st.write(data["deskripsi"])

        st.markdown("**Reaksi:**")
        st.code(data["reaksi"])
    else:
        st.info("Data struktur dan reaksi belum tersedia untuk golongan ini.")

# -- Footer --
st.markdown("---")
st.caption("© 2025 | Uji Senyawa Kimia Interaktif by Streamlit 🎓")
