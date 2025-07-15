import streamlit as st

# --- DATA SOAL KUIS (CONTOH SEDERHANA) ---
quiz_data = [
    {
        "image_url": "https://www.chemblink.com/structure/1/100-51-6.gif",  # Benzyl alcohol, contoh saja
        "answer": "Benzyl alcohol"
    },
    {
        "image_url": "https://www.chemsynthesis.com/base/structure_diagrams/635.gif",
        "answer": "Benzaldehyde"
    },
    # Tambahkan lebih banyak soal (struktur kimia & nama)
]

# --- DATA UJI SENYAWA (dari tabel gambar, ringkas, edit sesuai kebutuhan) ---
uji_data = {
    "Hidrokarbon": [
        {
            "Nama Uji": "Uji Pembakaran",
            "Hasil Positif": "Nyala kuning berasap",
            "Keterangan": "Aromatik"
        },
        {
            "Nama Uji": "Uji Bromin",
            "Hasil Positif": "Warna hilang",
            "Keterangan": "Adisi ikatan rangkap"
        },
        {
            "Nama Uji": "Uji Baeyer",
            "Hasil Positif": "Warna ungu hilang jadi coklat",
            "Keterangan": "Ikatan rangkap"
        },
    ],
    "Alkohol Primer": [
        {
            "Nama Uji": "Uji Lucas",
            "Hasil Positif": "Tidak keruh/keruh lambat (>5 menit)",
            "Keterangan": "Lambat bereaksi dengan ZnCl2/HCl"
        },
        {
            "Nama Uji": "Uji Kromik (Jones)",
            "Hasil Positif": "Oranye → hijau",
            "Keterangan": "Oksidasi menjadi asam karboksilat"
        },
    ],
    # ... Tambahkan semua golongan sesuai tabel ...
}

# --- STREAMLIT UI ---
st.set_page_config(page_title="Uji Golongan Senyawa", page_icon="⚗", layout="wide")
st.title("Uji Golongan Senyawa Kimia")

st.markdown("""
Web interaktif untuk mencari informasi uji-uji kimia pada berbagai golongan senyawa organik, beserta deskripsi hasil positif dan penjelasannya.
""")

# Pilihan golongan senyawa
golongan = st.selectbox("Pilih Golongan Senyawa:", list(uji_data.keys()))

# Tampilkan semua uji untuk golongan tersebut
if golongan:
    st.subheader(f"Daftar Uji untuk {golongan}")
    for uji in uji_data[golongan]:
        with st.expander(uji["Nama Uji"]):
            st.markdown(f"*Hasil Positif:* {uji['Hasil Positif']}")
            st.markdown(f"*Keterangan/Prinsip:* {uji['Keterangan']}")

st.markdown("---")

# --- QUIZ KIMIA ---
st.header("Quiz: Tebak Nama Senyawa dari Strukturnya")
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
    st.session_state.score = 0

question = quiz_data[st.session_state.quiz_index]
st.image(question["image_url"], width=200, caption="Struktur kimia, tebak namanya!")

user_answer = st.text_input("Jawaban Anda (nama senyawa):", key="answer_key")
if st.button("Cek Jawaban"):
    if user_answer.strip().lower() == question["answer"].lower():
        st.success("Benar!")
        st.session_state.score += 1
    else:
        st.error(f"Salah, nama yang benar: {question['answer']}")

    if st.session_state.quiz_index < len(quiz_data) - 1:
        st.session_state.quiz_index += 1
    else:
        st.write(f"Quiz selesai! Skor Anda: {st.session_state.score}/{len(quiz_data)}")
        st.session_state.quiz_index = 0
        st.session_state.score = 0

# --- Styling tambahan ---
st.markdown("""
<style>
    .stApp {
        background-color: #f7f7ff;
        font-family: 'Roboto', sans-serif;
    }
</style>
""", unsafe_allow_html=True)
