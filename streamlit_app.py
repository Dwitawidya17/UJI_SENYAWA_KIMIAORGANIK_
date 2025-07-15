import streamlit as st

# Data uji golongan senyawa (ringkasan dari sumber ilmiah uji fitokimia dan kualitatif)
uji_data = {
    "Hidrokarbon": [
        {"Nama Uji": "Uji Pembakaran",
         "Hasil Positif": "Nyala kuning berasap",
         "Keterangan": "Menunjukkan adanya karbon tak jenuh dan aromatic."},
        {"Nama Uji": "Uji Bromin",
         "Hasil Positif": "Larutan berubah warna hilang",
         "Keterangan": "Menandakan adanya ikatan rangkap C=C yang bereaksi dengan bromin."},
        {"Nama Uji": "Uji Baeyer (Kalium Permanganat)",
         "Hasil Positif": "Warna ungu KMnO4 memudar menjadi coklat",
         "Keterangan": "Menunjukkan adanya ikatan rangkap tak jenuh pada molekul."}
    ],
    "Alkohol Primer": [
        {"Nama Uji": "Uji Lucas",
         "Hasil Positif": "Tidak keruh atau keruh lambat (>5 menit)",
         "Keterangan": "Alkohol primer bereaksi lambat dengan ZnCl2/HCl membentuk klorida alkil."},
        {"Nama Uji": "Uji Kromik (Jones)",
         "Hasil Positif": "Warna oranye berubah menjadi hijau",
         "Keterangan": "Alkohol primer teroksidasi menjadi asam karboksilat."}
    ],
    "Alkohol Sekunder": [
        {"Nama Uji": "Uji Lucas",
         "Hasil Positif": "Keruh dalam 5 menit",
         "Keterangan": "Alkohol sekunder bereaksi sedang dengan ZnCl2/HCl membentuk klorida alkil."},
        {"Nama Uji": "Uji Kromik (Jones)",
         "Hasil Positif": "Warna oranye menjadi hijau",
         "Keterangan": "Alkohol sekunder teroksidasi menjadi keton."}
    ],
    "Alkohol Tersier": [
        {"Nama Uji": "Uji Lucas",
         "Hasil Positif": "Keruh cepat (<1 menit)",
         "Keterangan": "Alkohol tersier bereaksi cepat dengan ZnCl2/HCl membentuk klorida alkil."},
        {"Nama Uji": "Uji Kromik (Jones)",
         "Hasil Positif": "Tidak ada perubahan warna",
         "Keterangan": "Alkohol tersier tidak mudah teroksidasi."}
    ],
    "Aldehid": [
        {"Nama Uji": "Uji Tollens",
         "Hasil Positif": "Cermin perak terbentuk",
         "Keterangan": "Aldehid teroksidasi membentuk asam karboksilat."},
        {"Nama Uji": "Uji Fehling",
         "Hasil Positif": "Endapan merah bata terbentuk",
         "Keterangan": "Aldehid mereduksi ion Cu(II) menjadi Cu(I) oksida."}
    ],
    "Keton": [
        {"Nama Uji": "Uji Tollens",
         "Hasil Positif": "Tidak ada perubahan",
         "Keterangan": "Keton tidak teroksidasi dengan reagen Tollens."},
        {"Nama Uji": "Uji Fehling",
         "Hasil Positif": "Tidak ada endapan",
         "Keterangan": "Keton tidak bereaksi dengan reagen Fehling."}
    ],
    "Fenol": [
        {"Nama Uji": "Uji FeCl3",
         "Hasil Positif": "Warna hijau, biru, atau ungu terbentuk",
         "Keterangan": "Menandakan adanya gugus hidroksil fenolik."},
        {"Nama Uji": "Uji Bromin",
         "Hasil Positif": "Endapan putih terbentuk",
         "Keterangan": "Fenol bereaksi dengan bromin membentuk senyawa tribromofenol."}
    ],
    "Asam Karboksilat": [
        {"Nama Uji": "Uji Natrium Bikarbonat",
         "Hasil Positif": "Terbentuk gas CO2 yg berbuih",
         "Keterangan": "Asam karboksilat bereaksi dengan bikarbonat menghasilkan karbon dioksida."},
        {"Nama Uji": "Uji Esterifikasi",
         "Hasil Positif": "Terbentuk ester dengan bau harum",
         "Keterangan": "Reaksi asam karboksilat dengan alkohol membentuk ester."}
    ],
    "Ester": [
        {"Nama Uji": "Uji Bau",
         "Hasil Positif": "Tercium bau harum khas ester",
         "Keterangan": "Ester memiliki bau aroma buah/kembang yang khas."},
        {"Nama Uji": "Uji Hidrolisis Asam",
         "Hasil Positif": "Terbentuk asam karboksilat dan alkohol",
         "Keterangan": "Ester terhidrolisis oleh asam menjadi alkohol dan asam."}
    ],
    "Alkaloid (fitokimia)": [
        {"Nama Uji": "Uji Mayer",
         "Hasil Positif": "Terbentuk endapan putih",
         "Keterangan": "Alkaloid membentuk kompleks dengan pereaksi Mayer."},
        {"Nama Uji": "Uji Dragendorff",
         "Hasil Positif": "Terbentuk endapan oranye",
         "Keterangan": "Alkaloid bereaksi dengan pereaksi Dragendorff."}
    ],
    "Flavonoid": [
        {"Nama Uji": "Uji Mg dan HCl",
         "Hasil Positif": "Lahirnya warna merah/jingga pada lapisan atas",
         "Keterangan": "Reaksi reduksi flavonoid menghasilkan warna khas."},
        {"Nama Uji": "Uji AlCl3",
         "Hasil Positif": "Warna kuning intensif",
         "Keterangan": "Pembentukan kompleks dengan aluminium klorida."}
    ],
    "Saponin": [
        {"Nama Uji": "Uji Buah Busapun",
         "Hasil Positif": "Terbentuk buih stabil lebih dari 10 menit",
         "Keterangan": "Saponin menimbulkan busa khas di air."},
        {"Nama Uji": "Uji Hemolisis",
         "Hasil Positif": "Merusak membran eritrosit",
         "Keterangan": "Saponin dapat merusak membran sel darah merah."}
    ]
}


# Data quiz (nama senyawa saja, tanpa gambar)
quiz_data = [
    {"soal": "Nama senyawa yang merupakan alkohol primer yang mudah teroksidasi menjadi asam karboksilat?",
     "jawaban": "Etanol"},
    {"soal": "Golongan senyawa yang menunjukkan cermin perak pada uji Tollens?",
     "jawaban": "Aldehid"},
    {"soal": "Uji yang menghasilkan endapan oranye menandakan adanya golongan alkaloid?",
     "jawaban": "Dragendorff"},
    {"soal": "Golongan senyawa yang memiliki bau harum khas ester?",
     "jawaban": "Ester"},
    {"soal": "Uji yang menunjukkan warna kuning intens dan pembentukan kompleks dengan aluminium klorida?",
     "jawaban": "Flavonoid"}
]


# Streamlit UI
st.set_page_config(page_title="Uji Golongan Senyawa Kimia", page_icon="⚗", layout="centered")
st.title("Uji Golongan Senyawa Kimia - Lengkap tanpa Gambar")

st.markdown("""
Pilih golongan senyawa dari daftar berikut untuk melihat *nama uji, hasil positif, dan keterangan prinsip uji* secara lengkap.
""")

golongan = st.selectbox("Pilih Golongan Senyawa:", options=[""] + list(uji_data.keys()))

if golongan:
    st.subheader(f"Daftar Uji untuk Golongan {golongan}")
    for item in uji_data[golongan]:
        st.markdown(f"{item['Nama Uji']}")
        st.markdown(f"- Hasil Positif : {item['Hasil Positif']}")
        st.markdown(f"- Keterangan    : {item['Keterangan']}")
        st.markdown("---")

st.markdown("## Kuis Singkat: Tebak Jawaban yang Tepat")
st.markdown("Jawab kuis berikut untuk mengasah pemahaman tentang senyawa dan uji kimia.")

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
    st.session_state.skor = 0
    st.session_state.kuis_selesai = False

if not st.session_state.kuis_selesai:
    soal = quiz_data[st.session_state.quiz_index]
    jawaban = soal["jawaban"].lower()
    st.write(f"*Soal {st.session_state.quiz_index + 1}:* {soal['soal']}")
    user_jwb = st.text_input("Masukkan jawaban Anda:", key="user_jwb")

    if st.button("Periksa Jawaban", key="cek_jwb"):
        if user_jwb.strip().lower() == jawaban:
            st.success("Jawaban benar!")
            st.session_state.skor += 1
        else:
            st.error(f"Jawaban salah. Jawaban yang benar: {soal['jawaban']}")

        if st.session_state.quiz_index < len(quiz_data) - 1:
            st.session_state.quiz_index += 1
        else:
            st.session_state.kuis_selesai = True
else:
    st.write(f"*Kuis selesai! Skor Anda: {st.session_state.skor} / {len(quiz_data)}*")
    if st.button("Mulai ulang kuis"):
        st.session_state.quiz_index = 0
        st.session_state.skor = 0
        st.session_state.kuis_selesai = False


# Styling sederhana supaya menarik di mobile
st.markdown("""
<style>
    body {
        background-color: #f0faff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #007ACC;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #005f99;
    }
</style>
""", unsafe_allow_html=True)
