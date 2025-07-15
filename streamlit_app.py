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

# ===================== CONFIG STREAMLIT =====================
st.set_page_config(page_title="Uji Senyawa Kimia", layout="wide")
tab1, tab2 = st.tabs(["🔍 Uji Senyawa", "🧠 Kuis Kimia"])

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

   
# ===================== FOOTER =====================
st.markdown("---")
st.caption("© 2025 | Uji Senyawa Kimia Interaktif by Streamlit 🎓")

<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Tabel Periodik Interaktif</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background: #f4f4f4;
    margin: 0;
    padding: 20px;
    display: flex;
    justify-content: center;
  }
  .container {
    background: white;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
    width: 900px;
    max-width: 95vw;
    padding: 30px;
  }
  h1 {
    text-align: center;
    color: #0056b3;
    margin-bottom: 24px;
  }
  .periodic-table {
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    gap: 10px;
    justify-items: center;
    margin-bottom: 40px;
  }
  .element-tile {
    background-color: #e0e0e0;
    border-radius: 8px;
    box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
    width: 75px;
    height: 90px;
    cursor: pointer;
    padding: 8px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    user-select: none;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    position: relative;
  }
  .element-tile:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 12px rgba(0,0,0,0.2);
  }
  .atomic-number {
    font-size: 14px;
    text-align: left;
    font-weight: bold;
    color: #333;
  }
  .symbol {
    font-size: 26px;
    font-weight: 800;
    text-align: center;
    color: #222;
  }
  .name {
    font-size: 11px;
    text-align: center;
    color: #555;
    user-select: text;
  }
  /* Warna kategori unsur */
  .nonmetal { background-color: #ffcccc; }
  .noble-gas { background-color: #cceeff; }
  .alkali-metal { background-color: #ffeecc; }
  .alkaline-earth-metal { background-color: #ddffdd; }
  .metalloid { background-color: #ffedb3; }
  .halogen { background-color: #e0ccff; }
  .element-info {
    padding: 20px;
    border-radius: 10px;
    background: #e6f2ff;
    border: 1px solid #b3d9ff;
    min-height: 130px;
  }
  .element-info h2 {
    margin-top: 0;
    color: #0056b3;
    text-align: center;
  }
  .element-info p {
    margin: 6px 0;
    font-size: 15px;
    color: #333;
  }
</style>
</head>
<body>
<div class="container">
  <h1>Tabel Periodik Unsur</h1>
  <div class="periodic-table" id="periodic-table"></div>
  
  <div class="element-info">
    <h2>Informasi Unsur</h2>
    <p id="info-text">Klik salah satu unsur di tabel untuk melihat detailnya.</p>
  </div>
</div>

<script>
  // Data unsur periodik sebagai objek JavaScript
  const elements = {
    "H": {name: "Hydrogen", atomic_number: 1, atomic_mass: 1.008, category: "nonmetal", description: "Unsur teringan, paling melimpah di alam semesta."},
    "He": {name: "Helium", atomic_number: 2, atomic_mass: 4.0026, category: "noble-gas", description: "Gas mulia tak berwarna, tak berbau, dan tak berasa. Paling tidak reaktif."},
    "Li": {name: "Lithium", atomic_number: 3, atomic_mass: 6.94, category: "alkali-metal", description: "Logam paling ringan, digunakan dalam baterai."},
    "Be": {name: "Beryllium", atomic_number: 4, atomic_mass: 9.0122, category: "alkaline-earth-metal", description: "Logam ringan, digunakan dalam paduan dan cermin."},
    "B": {name: "Boron", atomic_number: 5, atomic_mass: 10.81, category: "metalloid", description: "Metalloid yang digunakan dalam kaca, keramik, dan deterjen."},
    "C": {name: "Carbon", atomic_number: 6, atomic_mass: 12.011, category: "nonmetal", description: "Dasar kehidupan di Bumi, membentuk berlian dan grafit."},
    "N": {name: "Nitrogen", atomic_number: 7, atomic_mass: 14.007, category: "nonmetal", description: "Gas paling melimpah di atmosfer Bumi."},
    "O": {name: "Oxygen", atomic_number: 8, atomic_mass: 15.999, category: "nonmetal", description: "Penting untuk pernapasan dan pembakaran."},
    "F": {name: "Fluorine", atomic_number: 9, atomic_mass: 18.998, category: "halogen", description: "Unsur paling reaktif, digunakan dalam pasta gigi."},
    "Ne": {name: "Neon", atomic_number: 10, atomic_mass: 20.180, category: "noble-gas", description: "Gas mulia yang digunakan dalam lampu neon."}
  };

  // Render tabel periodik di div #periodic-table
  const container = document.getElementById("periodic-table");
  
  for (const [symbol, element] of Object.entries(elements)) {
    const elDiv = document.createElement("div");
    elDiv.className = element-tile ${element.category};
    elDiv.title = element.name;
    elDiv.innerHTML = `
      <div class="atomic-number">${element.atomic_number}</div>
      <div class="symbol">${symbol}</div>
      <div class="name">${element.name}</div>
    `;
    elDiv.onclick = () => {
      const infoText = `
        <h3>${element.name} (${symbol})</h3>
        <p><strong>Nomor Atom:</strong> ${element.atomic_number}</p>
        <p><strong>Massa Atom:</strong> ${element.atomic_mass}</p>
        <p><strong>Kategori:</strong> ${element.category.replace(/-/g," ")}</p>
        <p><strong>Deskripsi:</strong> ${element.description}</p>
      `;
      document.getElementById("info-text").innerHTML = infoText;
    };
    container.appendChild(elDiv);
  }
</script>
</body>
</html>
