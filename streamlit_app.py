import streamlit as st
import random
import pandas as pd

# ===================== DATA UJI SENYAWA =====================
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
    "Alkohol Sekunder": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Keruh sedang (~5 menit)", "Keterangan": "Reaksi sedang"},
        {"Nama Uji": "Uji Kromik", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi → keton"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"}
    ],
    "Alkohol Tersier": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Cepat keruh", "Keterangan": "Cepat bereaksi"},
        {"Nama Uji": "Uji Kromik", "Hasil Positif": "Negatif", "Keterangan": "Tidak teroksidasi"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"}
    ],
    "Fenol": [
        {"Nama Uji": "Uji Ferri Klorida", "Hasil Positif": "Warna ungu/biru", "Keterangan": "Kompleks fenolat"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Endapan putih tribromofenol", "Keterangan": "Substitusi elektrofilik"}
    ],
    "Aldehida": [
        {"Nama Uji": "Uji Tollens", "Hasil Positif": "Cermin perak", "Keterangan": "Aldehida teroksidasi"},
        {"Nama Uji": "Uji Fehling", "Hasil Positif": "Endapan merah bata", "Keterangan": "Aldehida positif"},
        {"Nama Uji": "Uji DNP", "Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Adisi nukleofilik"}
    ],
    "Keton": [
        {"Nama Uji": "Uji Tollens", "Hasil Positif": "Negatif", "Keterangan": "Tidak teroksidasi"},
        {"Nama Uji": "Uji Fehling", "Hasil Positif": "Negatif", "Keterangan": "Tidak bereaksi"},
        {"Nama Uji": "Uji DNP", "Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"}
    ],
    "Asam Karboksilat": [
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus merah", "Keterangan": "Bersifat asam"},
        {"Nama Uji": "Uji NaHCO₃", "Hasil Positif": "Gelembung CO₂", "Keterangan": "Reaksi dengan basa lemah"}
    ],
    "Amina Primer": [
        {"Nama Uji": "Uji Hinsberg", "Hasil Positif": "Larut setelah basa", "Keterangan": "Gugus -NH₂"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus biru", "Keterangan": "Bersifat basa"}
    ],
    "Amina Sekunder": [
        {"Nama Uji": "Uji Hinsberg", "Hasil Positif": "Tidak larut setelah basa", "Keterangan": "Tidak membentuk garam"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus biru", "Keterangan": "Bersifat basa"}
    ],
    "Amina Tersier": [
        {"Nama Uji": "Uji Hinsberg", "Hasil Positif": "Tidak bereaksi", "Keterangan": "Tidak membentuk derivat"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus biru", "Keterangan": "Bersifat basa"}
    ],
    "Ester": [
        {"Nama Uji": "Uji Hidrolisis", "Hasil Positif": "Bau khas dan asam", "Keterangan": "Hidrolisis → alkohol + asam"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus tetap", "Keterangan": "Netral"}
    ],
    "Amida": [
        {"Nama Uji": "Uji NaOH Panas", "Hasil Positif": "Amonia tercium", "Keterangan": "Hidrolisis amida"},
        {"Nama Uji": "Uji Lakmus", "Hasil Positif": "Lakmus biru", "Keterangan": "Basa lemah"}
    ],
    "Karbohidrat": [
        {"Nama Uji": "Uji Molisch", "Hasil Positif": "Cincin ungu", "Keterangan": "Dehidrasi → furfural"},
        {"Nama Uji": "Uji Benedict", "Hasil Positif": "Endapan merah bata", "Keterangan": "Gula pereduksi"}
    ],
    "Protein": [
        {"Nama Uji": "Uji Biuret", "Hasil Positif": "Warna ungu", "Keterangan": "Ikatan peptida"},
        {"Nama Uji": "Uji Xantoproteat", "Hasil Positif": "Warna kuning", "Keterangan": "Gugus aromatik"}
    ],
    "Lemak & Minyak": [
        {"Nama Uji": "Uji Kertas", "Hasil Positif": "Noda transparan", "Keterangan": "Ciri khas lipid"},
        {"Nama Uji": "Uji Baeyer", "Hasil Positif": "Warna ungu hilang", "Keterangan": "Ikatan tak jenuh"}
    ]
}

# ===================== FAKTA MENARIK =====================
fakta_menarik = [
    "🧴 Lemak jenuh tidak bereaksi dengan larutan Baeyer, tapi lemak tak jenuh bisa.",
    "🧪 Fenol memberikan warna ungu dengan FeCl₃, berbeda dari alkohol biasa.",
    "⚗ Uji Lucas membedakan alkohol primer, sekunder, dan tersier secara visual.",
    "💨 NaHCO₃ hanya bereaksi dengan asam kuat seperti asam karboksilat.",
    "🔬 Biuret test hanya positif jika terdapat dua atau lebih ikatan peptida.",
]

# ===================== DATA TABEL PERIODIK =====================
periodic_data = [
    {"Unsur": "H", "Nama": "Hidrogen", "No Atom": 1, "Simbol": "H", "Golongan": "Non-logam", "Massa Atom": 1.008, "Keterangan": "Gas tidak berwarna dan sangat ringan."},
    {"Unsur": "He", "Nama": "Helium", "No Atom": 2, "Simbol": "He", "Golongan": "Gas mulia", "Massa Atom": 4.0026, "Keterangan": "Gas inert, digunakan dalam balon udara."},
    {"Unsur": "Li", "Nama": "Litium", "No Atom": 3, "Simbol": "Li", "Golongan": "Logam alkali", "Massa Atom": 6.94, "Keterangan": "Logam lunak dan reaktif."},
    {"Unsur": "Be", "Nama": "Berilium", "No Atom": 4, "Simbol": "Be", "Golongan": "Logam alkali tanah", "Massa Atom": 9.0122, "Keterangan": "Logam keras dengan titik leleh tinggi."},
    {"Unsur": "B", "Nama": "Boron", "No Atom": 5, "Simbol": "B", "Golongan": "Semilogam", "Massa Atom": 10.81, "Keterangan": "Semilogam dengan sifat unik."},
    {"Unsur": "C", "Nama": "Karbon", "No Atom": 6, "Simbol": "C", "Golongan": "Non-logam", "Massa Atom": 12.011, "Keterangan": "Elemen dasar kehidupan."},
    {"Unsur": "N", "Nama": "Nitrogen", "No Atom": 7, "Simbol": "N", "Golongan": "Non-logam", "Massa Atom": 14.007, "Keterangan": "Gas utama di atmosfer bumi."},
    {"Unsur": "O", "Nama": "Oksigen", "No Atom": 8, "Simbol": "O", "Golongan": "Non-logam", "Massa Atom": 15.999, "Keterangan": "Diperlukan untuk respirasi."},
    {"Unsur": "F", "Nama": "Fluorin", "No Atom": 9, "Simbol": "F", "Golongan": "Halogen", "Massa Atom": 18.998, "Keterangan": "Gas sangat reaktif."},
    {"Unsur": "Ne", "Nama": "Neon", "No Atom": 10, "Simbol": "Ne", "Golongan": "Gas mulia", "Massa Atom": 20.180, "Keterangan": "Gas inert untuk lampu neon."}
    # Tambah data unsur lain sesuai kebutuhan
]
df_periodic = pd.DataFrame(periodic_data)

# ===================== CONFIG STREAMLIT =====================
st.set_page_config(page_title="Uji Senyawa Kimia", layout="wide")
tab1, tab2, tab3 = st.tabs(["🔍 Uji Senyawa", "🧠 Kuis Kimia", "🧪 Tabel Periodik"])

# ===================== TAB 1: UJI SENYAWA =====================
with tab1:
    st.title("🔬 Uji Golongan Senyawa Kimia")
    st.markdown("Pilih golongan senyawa untuk melihat jenis uji, hasil positif, dan keterangannya.")

    selected = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()))
    st.subheader(f"📋 Hasil Uji untuk: {selected}")
    for uji in senyawa_data[selected]:
        with st.expander(uji["Nama Uji"]):
            st.markdown(f"*Hasil Positif:* {uji['Hasil Positif']}")
            st.markdown(f"*Keterangan:* {uji['Keterangan']}")

# ===================== TAB 2: KUIS KIMIA =====================
with tab2:
    st.title("🧠 Kuis Golongan Senyawa")

    semua_uji = []
    for gol, daftar_uji in senyawa_data.items():
        for uji in daftar_uji:
            semua_uji.append({**uji, "Golongan": gol})

    jumlah_soal = min(15, len(semua_uji))

    if "soal_kuis" not in st.session_state:
        st.session_state["soal_kuis"] = random.sample(semua_uji, k=jumlah_soal)
        st.session_state["opsi_kuis"] = []
        for soal in st.session_state["soal_kuis"]:
            opsi = random.sample(list(senyawa_data.keys()), 4)
            if soal["Golongan"] not in opsi:
                opsi[random.randint(0, 3)] = soal["Golongan"]
            random.shuffle(opsi)
            st.session_state["opsi_kuis"].append(opsi)

    soal_kuis = st.session_state["soal_kuis"]
    opsi_kuis = st.session_state["opsi_kuis"]

    st.markdown("Jawab semua soal terlebih dahulu, lalu klik *Submit Jawaban Semua*.")

    jawaban_pengguna = {}
    for i, soal in enumerate(soal_kuis, 1):
        st.markdown(f"*Soal {i}:* {soal['Nama Uji']} → Hasil: {soal['Hasil Positif']}")
        opsi = opsi_kuis[i - 1]
        jawaban = st.radio("Pilih Golongan:", opsi, key=f"kuis_{i}")
        jawaban_pengguna[f"soal_{i}"] = {"jawaban": jawaban, "benar": soal["Golongan"]}

    if st.button("📤 Submit Jawaban Semua"):
        benar = sum(1 for k in jawaban_pengguna if jawaban_pengguna[k]["jawaban"] == jawaban_pengguna[k]["benar"])
        skor = (benar / jumlah_soal) * 100

        st.success(f"✅ Kamu menjawab {benar} dari {jumlah_soal} soal dengan benar.")
        st.info(f"🎯 Skor akhir: *{skor:.2f}%*")

        salah = [(k, v["jawaban"], v["benar"]) for k, v in jawaban_pengguna.items() if v["jawaban"] != v["benar"]]
        if salah:
            st.warning("❌ Jawaban yang salah:")
            for s in salah:
                st.markdown(f"- *{s[0]}: Jawabanmu **{s[1]}, seharusnya **{s[2]}*")

        st.markdown("---")
        st.subheader("💡 Fakta Menarik Kimia")
        st.info(random.choice(fakta_menarik))

# ===================== TAB 3: TABEL PERIODIK =====================
with tab3:
    st.title("🧪 Tabel Periodik Unsur")
    st.markdown("Pilih satu unsur untuk melihat informasi lengkapnya.")

    pilihan_unsur = st.selectbox("Pilih Unsur:", df_periodic["Unsur"] + " - " + df_periodic["Nama"])
    simbol = pilihan_unsur.split(" - ")[0]
    data_unsur = df_periodic[df_periodic["Unsur"] == simbol].iloc[0]

    st.write(f"**Nama:** {data_unsur['Nama']}")
    st.write(f"**Simbol:** {data_unsur['Simbol']}")
    st.write(f"**Nomor Atom:** {data_unsur['No Atom']}")
    st.write(f"**Golongan:** {data_unsur['Golongan']}")
    st.write(f"**Massa Atom:** {data_unsur['Massa Atom']}")
    st.write(f"**Keterangan:** {data_unsur['Keterangan']}")

# Contoh data struktur dan reaksi
struktur_dan_reaksi = {
    "Alkohol Primer": {
        "struktur": "struktur/alkohol_primer.png",  # letakkan gambar ini di folder struktur/
        "reaksi": "Alkohol primer dapat mengalami oksidasi menjadi aldehida, kemudian asam karboksilat.\nReaksi umum:\nR-CH2OH → R-CHO → R-COOH",
        "deskripsi": "Alkohol primer memiliki gugus -OH yang melekat pada karbon primer."
    },
    "Fenol": {
        "struktur": "struktur/fenol.png",
        "reaksi": "Fenol bereaksi dengan FeCl3 membentuk kompleks berwarna ungu.\nReaksi substitusi juga terjadi dengan brom pada cincin aromatik.",
        "deskripsi": "Fenol adalah senyawa dengan gugus -OH yang berikatan langsung ke cincin aromatik."
    },
    "Aldehida": {
        "struktur": "struktur/aldehida.png",
        "reaksi": "Aldehida dapat teroksidasi menjadi asam karboksilat dan memberikan cermin perak dengan reagen Tollens.",
        "deskripsi": "Aldehida memiliki gugus karbonil (C=O) di ujung rantai karbon."
    },
    # Tambahkan sesuai kebutuhan
}


# ===================== FOOTER =====================
st.markdown("---")
st.caption("© 2025 | Uji Senyawa Kimia Interaktif by Streamlit 🎓")
