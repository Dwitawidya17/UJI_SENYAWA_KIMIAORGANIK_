import streamlit as st
import random

# Data golongan senyawa dan uji
data = {
    "Hidrokarbon": {
        "Uji Pembakaran": {"Hasil Positif": "Nyala kuning berasap", "Keterangan": "Aromatik"},
        "Uji Bromin": {"Hasil Positif": "Warna hilang", "Keterangan": "Adisi ikatan rangkap"},
        "Uji Baeyer": {"Hasil Positif": "Warna ungu hilang jadi coklat", "Keterangan": "Ikatan rangkap"}
    },
    # (Lengkapi dengan data lain sesuai kebutuhan, data selengkapnya bisa disalin dari balasan sebelumnya)
}

# Fakta menarik (contoh untuk fitur tambahan)
fun_facts = [
    "Uji Tollens dikenal juga sebagai uji cermin perak karena menghasilkan endapan perak mengkilap.",
    "Fenol memberikan warna ungu dengan larutan FeCl3, berbeda dengan alkohol.",
    "Tidak semua alkohol bereaksi dengan uji Lucas dalam waktu yang sama, tergantung strukturnya.",
    "Gula dapat diidentifikasi dengan uji Benedict yang menghasilkan warna merah bata."
]
