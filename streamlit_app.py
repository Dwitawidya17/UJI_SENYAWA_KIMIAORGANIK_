import streamlit as st

# ========== DATA ==========
# Pengertian Ester Moon
pengertian = {
    "Ester Moon adalah aplikasi web yang bergerak dalam menyediakan bahan ajar berupa kumpulan 
    materi praktikum analisis titrimetri dan kimia organik. Materi praktikum yang tersedia merupakan 
    materi dasar yang dapat mengasah skill analis dalam bidang analitik. Selain materi praktikum, a
    plikasi web ini menyediakan fitur berupa kalkulator perhitungan konsentrasi dan normalitas larutan
    untuk standardisasi. Dengan adanya aplikasi web ini analis akan lebih mudah dalam mengakses bahan 
    ajar praktikum, karena bahan ajar yang tersedia sangat fleksibel dan bisa diakses kapan saja."
    "list nama kelompok 03 Anita Tiara Angel, Dwita Widya Putri, Marsya Madina Munir, Najwa Ananda Effendy, Shella Rivana Auliya"
}

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

st.set_page_config(page_title="Ester Moon", layout="centered")
st.title("🌙 Ester Moon")

menu = ["Home", "Beranda", "Uji Senyawa Organik", "Data Fisik Senyawa", "Kuis", "Uji Lanjutan"]
selected = st.sidebar.selectbox("Menu", menu)

if selected == "Home":
    st.header("Apa Itu Ester Moon?")
    st.write("""
        **Ester Moon** adalah aplikasi web yang bergerak dalam menyediakan bahan ajar berupa kumpulan materi praktikum analisis titrimetri dan kimia organik.  
        
        Materi praktikum yang tersedia merupakan materi dasar yang dapat mengasah skill analis dalam bidang analitik.  
        Selain materi praktikum, aplikasi web ini menyediakan fitur berupa **kalkulator perhitungan konsentrasi dan normalitas larutan** untuk standardisasi.  
        
        Dengan adanya aplikasi web ini, analis akan lebih mudah dalam mengakses bahan ajar praktikum karena bahan ajar yang tersedia sangat fleksibel dan bisa diakses kapan saja.
    """)
    st.subheader("👩‍🔬 Kelompok 03:")
    anggota = [
        "Anita Tiara Angel",
        "Dwita Widya Putri",
        "Marsya Madina Munir",
        "Najwa Ananda Effendy",
        "Shella Rivana Auliya"
    ]
    for nama in anggota:
        st.write(f"- {nama}")

elif selected == "Beranda":
    st.header("Selamat Datang!")
    st.write("""
        Aplikasi ini dirancang untuk membantu mempelajari **uji kualitatif senyawa organik**.
        Gunakan menu di samping untuk mengeksplorasi berbagai fitur seperti:
        - Pengertian golongan senyawa
        - Jenis uji senyawa
        - Data fisik senyawa
        - Kuis interaktif
    """)

# ... (lanjutan: semua tab lain tetap sama — Uji Senyawa, Data Fisik, Kuis, Uji Lanjutan) ...
