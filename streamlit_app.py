import streamlit as st

# Data dari tabel gambar disusun dalam dictionary
data = {
    "Hidrokarbon": {
        "Uji Pembakaran": {"Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
        "Uji Bromin": {"Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
        "Uji Baeyer": {"Hasil Positif": "Warna ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"}
    },
    "Alkohol Primer": {
        "Uji Lucas": {"Hasil Positif": "Tidak keruh / keruh lambat (>5 menit)", "Keterangan": "Lambat bereaksi dengan ZnCl2/HCl"},
        "Uji Kromik (Jones)": {"Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi menjadi asam karboksilat"},
        "Uji Natrium": {"Hasil Positif": "Gas H2", "Keterangan": "Reaksi dengan logam Na"}
    },
    "Alkohol Sekunder": {
        "Uji Lucas": {"Hasil Positif": "Keruh dalam ~5 menit", "Keterangan": "Reaksi sedang"},
        "Uji Kromik": {"Hasil Positif": "Oranye → hijau", "Keterangan": "Oksidasi menjadi keton"},
        "Uji Natrium": {"Hasil Positif": "Gas H2", "Keterangan": "Reaksi umum alkohol"}
    },
    "Alkohol Tersier": {
        "Uji Lucas": {"Hasil Positif": "Keruh cepat (<1 menit)", "Keterangan": "Reaksi cepat"},
        "Uji Kromik": {"Hasil Positif": "Negatif", "Keterangan": "Tidak teroksidasi"},
        "Uji Natrium": {"Hasil Positif": "Gas H2", "Keterangan": "Reaksi alkohol"}
    },
    "Fenol": {
        "Uji Ferri Klorida": {"Hasil Positif": "Warna ungu/biru", "Keterangan": "Fenol positif"},
        "Uji Bromin": {"Hasil Positif": "Endapan putih tribromofenol", "Keterangan": "Substitusi brom"}
    },
    "Eter": {
        "Bau": {"Hasil Positif": "Bau khas eter", "Keterangan": "Volatil"},
        "Uji Pembakaran": {"Hasil Positif": "Nyala bersih, asap sedikit", "Keterangan": "Identifikasi eter"}
    },
    "Aldehida": {
        "Uji DNPH": {"Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"},
        "Uji Tollens": {"Hasil Positif": "Cermin perak", "Keterangan": "Aldehida positif"},
        "Uji Fehling": {"Hasil Positif": "Endapan merah bata", "Keterangan": "Aldehida positif"}
    },
    "Keton": {
        "Uji DNPH": {"Hasil Positif": "Endapan kuning/jingga", "Keterangan": "Gugus karbonil"},
        "Uji Tollens": {"Hasil Positif": "Negatif", "Keterangan": "Tidak bereaksi"},
        "Uji Fehling": {"Hasil Positif": "Negatif", "Keterangan": "Tidak bereaksi"}
    },
    "Karbohidrat": {
        "Uji Molisch": {"Hasil Positif": "Cincin ungu", "Keterangan": "Semua karbohidrat positif"},
        "Uji Benedict": {"Hasil Positif": "Endapan merah bata", "Keterangan": "Gula reduksi"},
        "Uji Barfoed": {"Hasil Positif": "Endapan merah bata cepat", "Keterangan": "Monosakarida positif"},
        "Uji Selivanoff": {"Hasil Positif": "Warna merah cepat", "Keterangan": "Ketosa positif"}
    },
    "Asam Karboksilat": {
        "Uji Lakmus": {"Hasil Positif": "Lakmus merah", "Keterangan": "Asam"},
        "Uji NaHCO3": {"Hasil Positif": "Gelembung CO2", "Keterangan": "Asam karboksilat"}
    },
    "Amina Primer": {
        "Uji Hinsberg": {"Hasil Positif": "Larut setelah NaOH", "Keterangan": "Amina primer"}
    },
    "Amina Sekunder": {
        "Uji Hinsberg": {"Hasil Positif": "Tidak larut", "Keterangan": "Amina sekunder"}
    },
    "Amina Tersier": {
        "Uji Hinsberg": {"Hasil Positif": "Tidak bereaksi", "Keterangan": "Amina tersier"}
    },
    "Amina": {
        "Uji Lakmus": {"Hasil Positif": "Lakmus biru", "Keterangan": "Basa"}
    },
    "Protein": {
        "Uji Biuret": {"Hasil Positif": "Warna ungu", "Keterangan": "Ikatan peptida"},
        "Uji Ninhidrin": {"Hasil Positif": "Warna ungu/biru", "Keterangan": "Asam amino bebas"},
        "Uji Xantoproteat": {"Hasil Positif": "Warna kuning", "Keterangan": "Asam amino aromatik"}
    },
    "Lemak & Minyak": {
        "Uji Saponifikasi": {"Hasil Positif": "Sabun terbentuk", "Keterangan": "Hidrolisis trigliserida"},
        "Uji Kertas": {"Hasil Positif": "Noda transparan", "Keterangan": "Lemak/minyak positif"},
        "Uji Baeyer": {"Hasil Positif": "Warna ungu hilang jika tak jenuh", "Keterangan": "Lemak tak jenuh"}
    }
}

st.title("Uji Kimia Golongan Senyawa")

# Pilih Golongan Senyawa
golongan = st.selectbox("Pilih Golongan Senyawa", list(data.keys()))

if golongan:
    # Pilih Nama Uji
    nama_uji = st.selectbox("Pilih Nama Uji", list(data[golongan].keys()))
    if nama_uji:
        hasil = data[golongan][nama_uji]
        st.write("**Hasil Positif:**", hasil["Hasil Positif"])
        st.write("**Keterangan / Prinsip:**", hasil["Keterangan"])
