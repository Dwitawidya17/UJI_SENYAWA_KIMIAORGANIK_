import streamlit as st
import random

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

# ===================== DATA KUIS (pilihan ganda tanpa gambar) =====================
kuis_data = [
    {
        "soal": "Golongan senyawa dengan uji pembakaran menghasilkan nyala kuning berasap adalah?",
        "pilihan": ["Fenol", "Hidrokarbon", "Asam Karboksilat", "Aldehida"],
        "jawaban": "Hidrokarbon"
    },
    {
        "soal": "Uji Lucas bereaksi cepat (<1 menit) menandakan jenis alkohol?",
        "pilihan": ["Alkohol Primer", "Alkohol Sekunder", "Alkohol Tersier", "Bukan alkohol"],
        "jawaban": "Alkohol Tersier"
    },
    {
        "soal": "Uji Tollens menghasilkan cermin perak jika senyawa termasuk golongan?",
        "pilihan": ["Keton", "Aldehida", "Ester", "Fenol"],
        "jawaban": "Aldehida"
    },
    {
        "soal": "Uji FeCl₃ memberi warna ungu/biru yang menunjukkan adanya?",
        "pilihan": ["Fenol", "Alkohol Primer", "Alkaloid", "Asam Karboksilat"],
        "jawaban": "Fenol"
    },
    {
        "soal": "Reaksi dengan NaHCO₃ menghasilkan gelembung CO₂ pada golongan?",
        "pilihan": ["Alkohol", "Asam Karboksilat", "Amina", "Protein"],
        "jawaban": "Asam Karboksilat"
    }
]


# ===================== STREAMLIT UI =====================

st.set_page_config(page_title="Uji Golongan Senyawa", layout="wide")
st.title("🧪 Uji Golongan Senyawa Kimia - Interaktif")

# Sidebar - Pilihan golongan dan kuis pilihan ganda
with st.sidebar:
    st.header("Menu")
    golongan = st.selectbox("🔍 Pilih Golongan Senyawa", [""] + list(senyawa_data.keys()))

    st.markdown("---")
    st.header("🧬 Kuis Pilihan Ganda")
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.quiz_done = False

    if not st.session_state.quiz_done:
        current = kuis_data[st.session_state.quiz_index]
        st.write(f"*Soal {st.session_state.quiz_index + 1}:*")
        st.write(current["soal"])
        jawaban_user = st.radio("Pilih jawaban:", current["pilihan"], key="quiz_radio")

        if st.button("Cek Jawaban"):
            if jawaban_user == current["jawaban"]:
                st.success("✅ Jawaban benar!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Salah. Jawaban yang benar: {current['jawaban']}")
            if st.session_state.quiz_index < len(kuis_data) - 1:
                st.session_state.quiz_index += 1
            else:
                st.session_state.quiz_done = True
    else:
        st.write(f"🎉 Kuis selesai! Skor Anda: {st.session_state.score} dari {len(kuis_data)}")
        if st.button("Ulangi Kuis"):
            st.session_state.quiz_index = 0
            st.session_state.score = 0
            st.session_state.quiz_done = False

# Main page - Tampilkan uji sesuai golongan
st.subheader(f"Hasil Uji untuk Golongan: {golongan if golongan else '-'}")
if golongan:
    for uji in senyawa_data[golongan]:
        with st.expander(uji["Nama Uji"]):
            st.markdown(f"*Hasil Positif:* {uji['Hasil Positif']}")
            st.markdown(f"*Keterangan:* {uji['Keterangan']}")
else:
    st.info("Pilih golongan senyawa dari sidebar untuk lihat detail uji.")

# Styling CSS sederhana agar tombol & layout menarik
st.markdown("""
<style>
    .stButton>button {
        background-color: #007ACC;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #005a99;
        color: white;
    }
    .css-18e3th9 {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)
