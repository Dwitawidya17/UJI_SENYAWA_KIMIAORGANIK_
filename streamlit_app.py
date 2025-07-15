import streamlit as st
import random
import pandas as pd

# ===================== DATA UJI SENYAWA =====================
# (data senyawa_data tetap sama seperti sebelumnya)

# ===================== FAKTA MENARIK =====================
# (fakta_menarik tetap sama seperti sebelumnya)

# ===================== DATA TABEL PERIODIK SEDERHANA =====================
tabel_periodik = [
    {"No": 1, "Simbol": "H", "Nama": "Hidrogen", "Golongan": "Non-logam"},
    {"No": 2, "Simbol": "He", "Nama": "Helium", "Golongan": "Gas mulia"},
    {"No": 6, "Simbol": "C", "Nama": "Karbon", "Golongan": "Non-logam"},
    {"No": 7, "Simbol": "N", "Nama": "Nitrogen", "Golongan": "Non-logam"},
    {"No": 8, "Simbol": "O", "Nama": "Oksigen", "Golongan": "Non-logam"},
    {"No": 11, "Simbol": "Na", "Nama": "Natrium", "Golongan": "Logam alkali"},
    {"No": 12, "Simbol": "Mg", "Nama": "Magnesium", "Golongan": "Logam alkali tanah"},
    {"No": 17, "Simbol": "Cl", "Nama": "Klorin", "Golongan": "Halogen"},
    {"No": 19, "Simbol": "K", "Nama": "Kalium", "Golongan": "Logam alkali"},
    {"No": 26, "Simbol": "Fe", "Nama": "Besi", "Golongan": "Logam transisi"},
    {"No": 29, "Simbol": "Cu", "Nama": "Tembaga", "Golongan": "Logam transisi"},
    {"No": 35, "Simbol": "Br", "Nama": "Bromin", "Golongan": "Halogen"},
    {"No": 53, "Simbol": "I", "Nama": "Iodin", "Golongan": "Halogen"},
    {"No": 80, "Simbol": "Hg", "Nama": "Raksa", "Golongan": "Logam transisi"},
    {"No": 82, "Simbol": "Pb", "Nama": "Timbal", "Golongan": "Logam pasca-transisi"},
]

df_periodik = pd.DataFrame(tabel_periodik)

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

    if st.button("🔄 Ulangi Kuis"):
        st.session_state.pop("soal_kuis", None)
        st.session_state.pop("opsi_kuis", None)
        st.experimental_rerun()

# ===================== TAB 3: TABEL PERIODIK =====================
with tab3:
    st.title("🧪 Tabel Periodik Unsur Kimia")
    st.markdown("Berikut ini adalah tabel unsur-unsur kimia sederhana:")
    st.dataframe(df_periodik, use_container_width=True)
    st.markdown("> Untuk versi lebih lengkap dan interaktif, kamu bisa mengakses situs seperti [ptable.com](https://ptable.com/)")

# ===================== FOOTER =====================
st.markdown("---")
st.caption("© 2025 | Uji Senyawa Kimia Interaktif by Streamlit 🎓")
