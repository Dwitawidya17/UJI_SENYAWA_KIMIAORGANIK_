import streamlit as st
import random

# ===================== DATA UJI SENYAWA =====================
senyawa_data = {
    "Hidrokarbon": [
        {"Nama Uji": "Uji Pembakaran", "Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
        {"Nama Uji": "Uji Baeyer", "Hasil Positif": "Warna ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"},
        # Tambahan:
        {"Nama Uji": "Uji Kelarutan", "Hasil Positif": "Tidak larut dalam air, larut dalam pelarut nonpolar", "Keterangan": "Hidrokarbon cenderung nonpolar"},
        {"Nama Uji": "Titik Didih", "Hasil Positif": "Bervariasi, biasanya rendah untuk senyawa ringan", "Keterangan": "Ikatan antar molekul lemah"},
        {"Nama Uji": "Uji Kebasaan", "Hasil Positif": "Tidak bersifat basa", "Keterangan": "Tidak memiliki pasangan elektron bebas"}
    ],
    "Alkohol Primer": [
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Tidak keruh / lambat", "Keterangan": "Reaksi lambat dengan ZnCl₂/HCl"},
        {"Nama Uji": "Uji Kromik (Jones)", "Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi → asam karboksilat"},
        {"Nama Uji": "Uji Natrium", "Hasil Positif": "Gas H₂", "Keterangan": "Reaksi alkohol"},
        # Tambahan:
        {"Nama Uji": "Uji Kelarutan", "Hasil Positif": "Larut dalam air dan pelarut polar", "Keterangan": "Gugus –OH membuat molekul polar"},
        {"Nama Uji": "Titik Didih", "Hasil Positif": "Relatif tinggi dibanding hidrokarbon setara", "Keterangan": "Ikatan hidrogen antar molekul"},
        {"Nama Uji": "Uji Kebasaan", "Hasil Positif": "Sangat lemah basa", "Keterangan": "Alkohol bukan basa kuat"}
    ],
    # Golongan lain tetap sama ...
}

# ===================== FAKTA MENARIK =====================
fakta_menarik = [
    "🧴 Lemak jenuh tidak bereaksi dengan larutan Baeyer, tapi lemak tak jenuh bisa.",
    "🧪 Fenol memberikan warna ungu dengan FeCl₃, berbeda dari alkohol biasa.",
    "⚗ Uji Lucas membedakan alkohol primer, sekunder, dan tersier secara visual.",
    "💨 NaHCO₃ hanya bereaksi dengan asam kuat seperti asam karboksilat.",
    "🔬 Biuret test hanya positif jika terdapat dua atau lebih ikatan peptida.",
]

# ===================== CONFIG STREAMLIT =====================
st.set_page_config(page_title="Uji Senyawa Kimia", layout="wide")
tab1, tab2, tab3 = st.tabs(["🔍 Uji Senyawa", "⚗ Sifat Kelarutan & Titik Didih", "🧠 Kuis Kimia"])

# ===================== TAB 1: UJI SENYAWA =====================
with tab1:
    st.title("🔬 Uji Golongan Senyawa Kimia")
    st.markdown("Pilih golongan senyawa untuk melihat jenis uji, hasil positif, dan keterangannya.")
    selected = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()))
    st.subheader(f"📋 Hasil Uji untuk: {selected}")
    for uji in senyawa_data[selected]:
        if uji["Nama Uji"] not in ["Uji Kelarutan", "Titik Didih", "Uji Kebasaan"]:  # Tampilkan uji utama saja di tab 1
            with st.expander(uji["Nama Uji"]):
                st.markdown(f"Hasil Positif: {uji['Hasil Positif']}")
                st.markdown(f"Keterangan: {uji['Keterangan']}")

# ===================== TAB 2: SIFAT KELARUTAN & TITIK DIDIH =====================
with tab2:
    st.title("⚗ Uji Kelarutan, Titik Didih, dan Kebasaan")
    selected2 = st.selectbox("Pilih Golongan Senyawa", list(senyawa_data.keys()), key="kelarutan_tdk")
    st.subheader(f"Sifat Fisik dan Kimia untuk: {selected2}")

    # Filter dan tampilkan khusus sifat kelarutan, titik didih, kebasaan
    untuk_tampil = [uji for uji in senyawa_data[selected2] if uji["Nama Uji"] in ["Uji Kelarutan", "Titik Didih", "Uji Kebasaan"]]
    if untuk_tampil:
        for uji in untuk_tampil:
            with st.expander(uji["Nama Uji"]):
                st.markdown(f"Hasil Positif: {uji['Hasil Positif']}")
                st.markdown(f"Keterangan: {uji['Keterangan']}")
    else:
        st.info("Data tentang uji kelarutan, titik didih, atau kebasaan belum tersedia untuk golongan ini.")

# ===================== TAB 3: KUIS KIMIA =====================
with tab3:
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

    st.markdown("Jawab semua soal terlebih dahulu, lalu klik Submit Jawaban Semua.")

    jawaban_pengguna = {}
    for i, soal in enumerate(soal_kuis, 1):
        st.markdown(f"Soal {i}: {soal['Nama Uji']} → Hasil: {soal['Hasil Positif']}")
        opsi = opsi_kuis[i - 1]
        jawaban = st.radio("Pilih Golongan:", opsi, key=f"kuis_{i}")
        jawaban_pengguna[f"soal_{i}"] = {"jawaban": jawaban, "benar": soal["Golongan"]}

    if st.button("📤 Submit Jawaban Semua"):
        benar = sum(1 for k in jawaban_pengguna if jawaban_pengguna[k]["jawaban"] == jawaban_pengguna[k]["benar"])
        skor = (benar / jumlah_soal) * 100

        st.success(f"✅ Kamu menjawab {benar} dari {jumlah_soal} soal dengan benar.")
        st.info(f"🎯 Skor akhir: {skor:.2f}%")

        salah = [(k, v["jawaban"], v["benar"]) for k, v in jawaban_pengguna.items() if v["jawaban"] != v["benar"]]
        if salah:
            st.warning("❌ Jawaban yang salah:")
            for s in salah:
                st.markdown(f"- {s[0]}: Jawabanmu **{s[1]}, seharusnya **{s[2]}")

        st.markdown("---")
        st.subheader("💡 Fakta Menarik Kimia")
        st.info(random.choice(fakta_menarik))

# ===================== FOOTER =====================
st.markdown("---")
st.caption("© 2025 | Uji Senyawa Kimia Interaktif by Streamlit 🎓")
