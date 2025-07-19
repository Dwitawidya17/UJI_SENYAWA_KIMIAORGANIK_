import streamlit as st

# ========== DATA ==========

# Pengertian golongan senyawa
pengertian = {
    "Hidrokarbon": "Senyawa organik yang terdiri dari unsur karbon dan hidrogen saja.",
    "Alkohol": "Senyawa yang memiliki gugus –OH (hidroksil) yang terikat pada atom karbon.",
    "Fenol": "Senyawa yang memiliki gugus –OH yang terikat langsung pada cincin aromatik.",
    "Eter": "Senyawa yang memiliki gugus –O– di antara dua gugus alkil atau aril.",
    "Aldehid": "Senyawa yang memiliki gugus karbonil (C=O) di ujung rantai karbon.",
    "Keton": "Senyawa yang memiliki gugus karbonil (C=O) di tengah rantai karbon.",
    "Asam Karboksilat": "Senyawa yang memiliki gugus –COOH.",
    "Karbohidrat": "Senyawa yang terdiri dari karbon, hidrogen, dan oksigen, biasanya dengan rumus umum Cn(H2O)n.",
    "Protein": "Biomolekul yang terdiri dari rantai panjang asam amino.",
}

# Uji senyawa
uji_senyawa = {
    "Hidrokarbon": [
        {"Nama Uji": "Uji Pembakaran", "Hasil Positif": "Nyala kuning berasap", "Keterangan": "Menunjukkan senyawa aromatik"},
        {"Nama Uji": "Uji Bromin", "Hasil Positif": "Warna bromin hilang", "Keterangan": "Menunjukkan ikatan rangkap (tak jenuh)"}
    ],
    "Alkohol": [
        {"Nama Uji": "Uji Kertas Kromatofilik", "Hasil Positif": "Timbul bau khas", "Keterangan": "Menunjukkan alkohol rendah"},
        {"Nama Uji": "Uji Lucas", "Hasil Positif": "Larutan keruh", "Keterangan": "Menunjukkan alkohol tersier bereaksi cepat"}
    ],
    "Fenol": [
        {"Nama Uji": "Uji FeCl3", "Hasil Positif": "Warna ungu", "Keterangan": "Menunjukkan adanya gugus fenol"}
    ],
    "Aldehid": [
        {"Nama Uji": "Uji Tollens", "Hasil Positif": "Cermin perak terbentuk", "Keterangan": "Menunjukkan adanya gugus aldehid"},
        {"Nama Uji": "Uji Benedict", "Hasil Positif": "Endapan merah bata", "Keterangan": "Aldehid tereduksi"}
    ],
    "Keton": [
        {"Nama Uji": "Uji 2,4-DNPH", "Hasil Positif": "Endapan kuning jingga", "Keterangan": "Menunjukkan adanya gugus karbonil"}
    ],
    "Karbohidrat": [
        {"Nama Uji": "Uji Molisch", "Hasil Positif": "Cincin ungu di batas larutan", "Keterangan": "Menunjukkan karbohidrat"},
        {"Nama Uji": "Uji Benedict", "Hasil Positif": "Endapan merah bata", "Keterangan": "Menunjukkan gula pereduksi"}
    ],
    "Asam Karboksilat": [
        {"Nama Uji": "Uji NaHCO3", "Hasil Positif": "Terbentuk gelembung CO2", "Keterangan": "Menunjukkan adanya gugus –COOH"}
    ],
    "Protein": [
        {"Nama Uji": "Uji Biuret", "Hasil Positif": "Warna ungu", "Keterangan": "Menunjukkan adanya ikatan peptida"}
    ]
}

# Data fisik
data_fisik = {
    "Alkohol": {"Kelarutan": "Larut dalam air", "pH": "Netral", "Titik Didih": "Tinggi karena ikatan hidrogen"},
    "Fenol": {"Kelarutan": "Sedikit larut", "pH": "Asam lemah", "Titik Didih": "Tinggi"},
    "Eter": {"Kelarutan": "Tidak larut", "pH": "-", "Titik Didih": "Rendah"},
    "Aldehid": {"Kelarutan": "Larut", "pH": "Netral", "Titik Didih": "Sedang"},
    "Keton": {"Kelarutan": "Larut", "pH": "Netral", "Titik Didih": "Sedang"},
    "Asam Karboksilat": {"Kelarutan": "Larut", "pH": "Asam", "Titik Didih": "Tinggi"},
    "Karbohidrat": {"Kelarutan": "Larut", "pH": "Netral", "Titik Didih": "-"},
    "Protein": {"Kelarutan": "Variatif", "pH": "Bervariasi", "Titik Didih": "Tidak tentu"}
}

# Uji lanjutan
uji_lanjutan_data = {
    "Aldehid": [
        {"Nama Uji": "Uji Schiff", "Hasil Positif": "Warna merah magenta", "Keterangan": "Menunjukkan aldehid alifatik"},
    ],
    "Protein": [
        {"Nama Uji": "Uji Xanthoproteat", "Hasil Positif": "Larutan kuning oranye", "Keterangan": "Adanya cincin aromatik"},
    ]
}

# ========== APLIKASI STREAMLIT ==========

st.set_page_config(page_title="Uji Senyawa Organik", layout="centered")
st.title("Aplikasi Edukasi: Uji Senyawa Organik")

menu = ["Beranda", "Uji Senyawa Organik", "Data Fisik Senyawa", "Kuis", "Uji Lanjutan"]
selected = st.sidebar.selectbox("Menu", menu)

if selected == "Beranda":
    st.header("Selamat Datang!")
    st.write("""
        Aplikasi ini dirancang untuk membantu mempelajari **uji kualitatif senyawa organik**.
        Gunakan menu di samping untuk mengeksplorasi berbagai fitur seperti:
        - Pengertian golongan senyawa
        - Jenis uji senyawa
        - Data fisik senyawa
        - Kuis interaktif
    """)

elif selected == "Uji Senyawa Organik":
    st.header("Uji Senyawa Organik")

    jenis = st.selectbox("Pilih Golongan Senyawa:", list(uji_senyawa.keys()))
    st.subheader(f"Pengertian {jenis}")
    st.write(pengertian.get(jenis, "-"))

    st.subheader("Data Uji:")
    data = uji_senyawa.get(jenis, [])
    for item in data:
        with st.expander(item["Nama Uji"]):
            st.write(f"**Hasil Positif**: {item['Hasil Positif']}")
            st.write(f"**Keterangan**: {item['Keterangan']}")

elif selected == "Data Fisik Senyawa":
    st.header("Data Fisik Senyawa")
    pilihan = st.selectbox("Pilih Golongan Senyawa:", list(data_fisik.keys()))
    data = data_fisik.get(pilihan, {})
    st.subheader(f"Karakteristik Fisik {pilihan}")
    st.write(f"- Kelarutan: {data.get('Kelarutan', '-')}")
    st.write(f"- pH: {data.get('pH', '-')}")
    st.write(f"- Titik Didih: {data.get('Titik Didih', '-')}")

elif selected == "Uji Lanjutan":
    st.header("Uji Lanjutan Senyawa Organik")
    jenis_terpilih = st.selectbox("Pilih Golongan Senyawa:", list(uji_lanjutan_data.keys()))
    uji_lanjutan = uji_lanjutan_data.get(jenis_terpilih, [])

    if uji_lanjutan:
        st.write(f"Berikut adalah uji lanjutan untuk **{jenis_terpilih}**:")
        for uji in uji_lanjutan:
            with st.expander(uji["Nama Uji"]):
                st.write(f"**Hasil Positif**: {uji['Hasil Positif']}")
                st.write(f"**Keterangan**: {uji['Keterangan']}")
    else:
        st.warning("Belum ada data uji lanjutan untuk golongan ini.")

elif selected == "Kuis":
    st.header("Kuis Interaktif")

    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'qn' not in st.session_state:
        st.session_state.qn = 0

    questions = [
        {
            "soal": "Apa hasil positif dari uji Tollens untuk aldehid?",
            "pilihan": ["Endapan merah", "Cermin perak", "Warna ungu", "Tidak bereaksi"],
            "jawaban": "Cermin perak"
        },
        {
            "soal": "Uji Biuret digunakan untuk mendeteksi apa?",
            "pilihan": ["Aldehid", "Protein", "Fenol", "Asam"],
            "jawaban": "Protein"
        },
        {
            "soal": "Hasil positif uji bromin pada hidrokarbon tak jenuh adalah...",
            "pilihan": ["Cermin perak", "Warna bromin hilang", "Ungu", "Endapan merah"],
            "jawaban": "Warna bromin hilang"
        }
    ]

    if st.session_state.qn < len(questions):
        q = questions[st.session_state.qn]
        st.write(f"**Pertanyaan {st.session_state.qn+1}:** {q['soal']}")
        pilihan = st.radio("Pilih jawaban:", q["pilihan"], key="jawaban_kuis")

        if st.button("Jawab"):
            if pilihan == q["jawaban"]:
                st.session_state.score += 1
                st.success("Jawaban benar!")
            else:
                st.error(f"Jawaban salah! Jawaban benar: {q['jawaban']}")
            st.session_state.qn += 1
    else:
        st.subheader(f"Kuis selesai! Skor Anda: {st.session_state.score} / {len(questions)}")
        if st.button("Ulang Kuis"):
            st.session_state.qn = 0
            st.session_state.score = 0
