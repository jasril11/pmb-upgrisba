# =========================================================
# PMB SAINS DATA UPGRISBA
# WEBSITE PENDAFTARAN MAHASISWA BARU
# =========================================================

import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import base64
import requests

# =========================================================
# CONFIG PAGE
# =========================================================

st.set_page_config(
    page_title="PMB UPGRISBA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# FUNCTION BASE64 BACKGROUND
# =========================================================


def get_base64(file_path):

    with open(file_path, "rb") as file:
        data = file.read()

    return base64.b64encode(data).decode()


# =========================================================
# LOAD BACKGROUND IMAGE
# =========================================================

bg_image = get_base64("kampus.jpg")

# =========================================================
# WHATSAPP API
# =========================================================

TOKEN = "E4VpspWTWeN9F4NsoW1K"

def kirim_wa(pesan):

    url = "https://api.fonnte.com/send"

    headers = {
        "Authorization": TOKEN
    }

    data = {
        "target": "085762228563",
        "message": pesan
    }

    requests.post(
        url,
        data=data,
        headers=headers
    )

# =========================================================
# DATABASE SQLITE
# =========================================================

conn = sqlite3.connect(
    "pmb.db",
    check_same_thread=False
)

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS mahasiswa (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nama TEXT,

    nik TEXT,

    email TEXT,

    hp TEXT,

    sekolah TEXT,

    alamat TEXT,

    jalur TEXT,

    tanggal TEXT
)
""")

conn.commit()

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(f"""
<style>

.stApp {{

    background-image:

    linear-gradient(
        rgba(255,255,255,0.25),
        rgba(255,255,255,0.25)
    ),

    url("data:image/jpg;base64,{bg_image}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

section[data-testid="stSidebar"] {{

    background: linear-gradient(
        to bottom,
        #08143c,
        #0d1b4c
    );
}}

section[data-testid="stSidebar"] * {{
    color: white;
}}

.hero {{

    background: linear-gradient(
        to right,
        #005bea,
        #00c6fb
    );

    padding: 20px 15px;

    border-radius: 30px;

    text-align: center;

    color: white;

    margin-top: -50px;
    margin-bottom: 10px;

    box-shadow: 0px 10px 25px rgba(0,0,0,0.18);

    width: 94%;
    max-width: 1350px;

    margin-left: auto;
    margin-right: auto;

    box-sizing: border-box;
}}

.hero h1 {{

    font-size: clamp(28px, 3.5vw, 52px);

    font-weight: 700;

    line-height: 1.35;

    margin-bottom: 18px;
}}

.hero h2 {{

    font-size: clamp(20px, 2vw, 32px);

    margin-bottom: 5px;
}}

.hero h3 {{

    font-size: clamp(18px, 1.8vw, 24px);

    margin-bottom: 5px;
}}

.hero p {{

    font-size: clamp(14px, 1.3vw, 20px);
}}

.card {{

    background: rgba(255,255,255,0.94);

    padding: 25px;

    border-radius: 20px;

    box-shadow: 0px 5px 15px rgba(0,0,0,0.08);

    transition: 0.3s;
}}

.card:hover {{
    transform: translateY(-5px);
}}

.card h3 {{
    font-size: 24px;
    margin-bottom: 15px;
    color: #0d1b4c;
}}

.card p {{
    font-size: 18px;
    line-height: 1.8;
    color: #333;
}}

.stButton > button {{

    width: 100%;
    height: 50px;

    border-radius: 12px;
    border: none;

    background: linear-gradient(
        to right,
        #005bea,
        #00c6fb
    );

      color: white;

    font-size: 18px;
    font-weight: bold;

    transition: 0.3s;
}}

.stButton > button:hover {{
    transform: scale(1.02);
}}

.stTextInput input,
.stTextArea textarea,
.stSelectbox div {{

    border-radius: 10px !important;
}}

[data-testid="stDataFrame"] {{

    background: rgba(255,255,255,0.94);

    border-radius: 18px;

    padding: 12px;

    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}}

.footer {{

    width: 92%;

    margin: auto;

    margin-top: 70px;

    background: rgba(255,255,255,0.94);

    padding: 50px;

    border-radius: 25px;
}}

.footer-container {{

    display: grid;

    grid-template-columns: repeat(2, 1fr);

    gap: 40px;
}}

.footer-column {{

    background: rgba(255,255,255,0.35);

    padding: 20px;

    border-radius: 18px;

    backdrop-filter: blur(6px);
}}

.footer-subtitle {{

    font-size: 24px;

    font-weight: bold;

    color: #0d1b4c;

    margin-bottom: 15px;
}}

.footer-text {{

    color: #555;

    line-height: 1.8;

    font-size: 17px;
}}

.footer-link {{

    display: block;

    margin-bottom: 10px;

    color: #555;

    text-decoration: none;

    font-size: 17px;
}}

.footer-link:hover {{

    color: #005bea;
}}

.social-icons {{

    display: flex;

    gap: 20px;

    margin-top: 15px;

    flex-wrap: wrap;
}}

.social-icons a {{

    display: flex;

    align-items: center;

    gap: 8px;

    text-decoration: none;

    font-size: 18px;

    color: #0d1b4c;

    font-weight: 500;
}}

.social-icons img {{

    width: 24px;

    height: 24px;
}}

.copyright {{

    text-align: center;

    margin-top: 40px;

    padding-top: 20px;

    border-top: 1px solid #ddd;

    color: #555;

    font-size: 16px;
}}

.whatsapp {{

    position: fixed;

    bottom: 20px;

    right: 20px;

    background: #25D366;

    color: white !important;

    padding: 12px 18px;

    border-radius: 14px;

    text-decoration: none;

    font-weight: bold;

    box-shadow: 0px 5px 15px rgba(0,0,0,0.2);

    z-index: 999;

    display: flex;

    align-items: center;

    gap: 10px;

    font-size: 15px;

    transition: 0.3s;
}}

.whatsapp:hover {{

    background: #1ebc59;

    transform: scale(1.03);
}}

.whatsapp img {{

    width: 28px;

    height: 28px;
}}

@media (max-width: 768px) {{

    .hero {{

    width: 94%;

    padding: 30px 18px;

    margin-top: 10px;

    border-radius: 22px;
   }}

    .hero h1 {{

        font-size: 28px;
    }}

    .hero h2 {{

        font-size: 22px;
    }}

    .hero h3 {{

        font-size: 18px;
    }}

    .hero p {{

        font-size: 14px;
    }}

    .card {{

        margin-bottom: 20px;
    }}

    .footer {{

        width: 95%;

        padding: 25px;
    }}

    .footer-container {{

        display: flex;

        flex-direction: column;

        gap: 25px;
    }}

    .footer-column {{

        width: 100%;

        min-width: 100%;

        padding: 18px;
    }}

    .footer-subtitle {{

        font-size: 32px;

        text-align: left;
    }}

    .footer-text {{

        font-size: 18px;

        line-height: 1.8;
    }}

    .social-icons {{

        flex-direction: column;

        gap: 18px;
    }}

    .social-icons a {{

        font-size: 18px;
    }}

    .social-icons img {{

        width: 30px;

        height: 30px;
    }}

    .footer-link {{

        font-size: 18px;

        margin-bottom: 14px;
    }}

    .copyright {{

        font-size: 15px;

        line-height: 1.8;
    }}

    .whatsapp {{

        right: 12px;

        bottom: 12px;

        padding: 10px 14px;

        font-size: 14px;
    }}

    .whatsapp img {{

        width: 24px;

        height: 24px;
    }}
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.image(
    "logo.png",
    width=200
)

st.sidebar.title(
    "PMB UPGRISBA"
)

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Beranda",
        "Profil Prodi",
        "Biaya Kuliah",
        "Pendaftaran",
        "Data Pendaftar",
        "Kontak"
    ]
)

# =========================================================
# HEADER
# =========================================================

st.markdown("""

<div class="hero">
<center><h2>
WEBSITE PENERIMAAN MAHASISWA BARU PROGRAM STUDI SAINS DATA
</h2>
<h2>
UNIVERSITAS PGRI SUMATERA BARAT
</h2>
<p>
<h2>Tahun Akademik 2026/2027</h2>
</p>
</center>
</div>

""", unsafe_allow_html=True)

# =========================================================
# BERANDA
# =========================================================

if menu == "Beranda":

    st.markdown("""
    <div class="card" style="
    padding:22px 30px;
    margin:20px auto 30px auto;
    text-align:center;
    max-width:1100px;
    margin-left:auto;
    margin-right:auto;
    ">

    <center><h3 style="
    color:#0d1b4c;
    margin-bottom:20px;
    font-size:30px;
    ">
    Selamat Datang di PMB Sains Data
    </h3>

    <p style="
    font-size:22px;
    line-height:1.9;
    color:#444;
    ">

    Program Studi Sains Data Universitas PGRI Sumatera Barat
    mempersiapkan mahasiswa menjadi talenta digital
    yang unggul di bidang Artificial Intelligence,
    Machine Learning, Big Data, dan Data Analytics.

    </p>
    </center>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# PROFIL
# =========================================================

elif menu == "Profil Prodi":

    st.markdown("""
    <div class="card" style="
    padding:20px;
    margin:20px auto 30px auto;
    max-width:1100px;
    ">
    
    <div style="
    text-align:center;
    color:#0d1b4c;
    margin-bottom:5px;
    font-size:30px;
    "><center>
    <b>Profil Program Studi</b>
    </div>
    
    <p style="
    font-size:20px;
    line-height:1.7;
    text-align:center;
    color:#444;
    margin-top:0px;
    margin-bottom:0px;
    ">
    Program Studi Sains Data
    berfokus pada pengolahan data,
    Artificial Intelligence,
    Machine Learning,
    Big Data,
    dan pemrograman modern.
    </p>
    </center>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 style="
    text-align:center;
    color:#0d1b4c;
    margin-top:10px;
    margin-bottom:25px;
    font-size:30px;
    ">
    Profesi Lulusan
    </h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
        <h3>AI / Machine Learning Engineer</h3>
        <p>Membangun sistem kecerdasan buatan modern.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>Business Intelligence Analyst</h3>
        <p>Menganalisis data bisnis dan perusahaan.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>Data Consultant</h3>
        <p>Memberikan solusi berbasis data dan teknologi.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:

        st.markdown("""
        <div class="card">
        <h3>Data Scientist</h3>
        <p>Mengolah data menggunakan teknologi modern.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>Data Engineer</h3>
        <p>Membangun sistem dan pipeline data.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>Big Data Engineer</h3>
        <p>Mengelola sistem Big Data dan Cloud.</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# BIAYA
# =========================================================

elif menu == "Biaya Kuliah":

    st.markdown("""
    <h2 style="
    text-align:left;
    color:#0d1b4c;
    ">
    Biaya Kuliah
    </h2>
    """, unsafe_allow_html=True)

    data = {

    "Pembayaran": [
        "Pengembangan",
        "Orientasi & Jaket",
        "SPP",
        "Kemahasiswaan",
        "TOTAL"
    ],

    "Semester 1": [
        "Rp 1.950.000",
        "Rp 500.000",
        "Rp 2.850.000",
        "Rp 100.000",
        "Rp 5.300.000"
    ]
}

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        width="stretch"
    )

# =========================================================
# PENDAFTARAN
# =========================================================

elif menu == "Pendaftaran":

    st.markdown("## Form Pendaftaran")

    with st.form("form"):

        nama = st.text_input("Nama Lengkap")

        nik = st.text_input("NIK")

        email = st.text_input("Email")

        hp = st.text_input("Nomor HP")

        sekolah = st.text_input("Asal Sekolah")

        alamat = st.text_area("Alamat")

        jalur = st.selectbox(
            "Jalur Pendaftaran",
            [
                "Reguler",
                "KIP-K",
                "Roadshow",
                "Mahasiswa Undangan",
                "Rekomendasi Wali Nagari"
            ]
        )

        upload = st.file_uploader(
            "Upload Berkas",
            type=["pdf", "jpg", "png"]
        )

        submit = st.form_submit_button(
            "DAFTAR SEKARANG"
        )

        if submit:

            if nama == "" or email == "" or hp == "":

                st.error(
                    "Harap lengkapi data terlebih dahulu!"
                )

            else:

                tanggal = datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

                c.execute("""
                INSERT INTO mahasiswa (

                    nama,
                    nik,
                    email,
                    hp,
                    sekolah,
                    alamat,
                    jalur,
                    tanggal
                    
                  )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?)

                """, (

                    nama,
                    nik,
                    email,
                    hp,
                    sekolah,
                    alamat,
                    jalur,
                    tanggal
                ))

                conn.commit()

                pesan = f"""
                PENDAFTAR BARU PMB

                Nama: {nama}
                Email: {email}
                HP: {hp}
                Sekolah: {sekolah}
                Jalur: {jalur}
                """

                kirim_wa(pesan)

                st.markdown("""
                <div style="
                background: rgba(13, 27, 76, 0.92);
                color: white;
                padding: 18px;
                border-radius: 14px;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                margin-top: 15px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
                ">

                Pendaftaran Berhasil!

                </div>

                """, unsafe_allow_html=True)

                st.balloons()

# =========================================================
# DATA PENDAFTAR
# =========================================================

elif menu == "Data Pendaftar":

    st.markdown("## Data Pendaftar")

    data = pd.read_sql_query(
        "SELECT * FROM mahasiswa",
        conn
    )

    st.dataframe(
        data,
        width="stretch"
    )

# =========================================================
# KONTAK
# =========================================================

elif menu == "Kontak":

    st.markdown("""

    <div class="footer">

    <div class="footer-container">

    <div class="footer-column">

    <h3 class="footer-subtitle">
    Kontak Dosen
    </h3>

    <p class="footer-text">

    📞 Zulfaneti<br> 081363387278
    <br><br>
    📞 Satrio Junaidi<br> 082389238003
    </p>

    </div>

    <div class="footer-column">

    <h3 class="footer-subtitle">
    Informasi Kampus           
    </h3>     
                    
    <p class="footer-text">
                
    📍 Jl. Gunung Pangilun Padang
    <br><br>
    ☎ 07517053731
    <br><br>
    ✉ info@upgrisba.ac.id
    </p>

    </div>

    <div class="footer-column">

    <h3 class="footer-subtitle">
    Media Sosial
    </h3>

    <div class="social-icons">

    <a href="https://facebook.com" target="_blank">

    <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png">

    <span>Facebook</span>

    </a>

    <a href="https://instagram.com" target="_blank">

    <img src="https://cdn-icons-png.flaticon.com/512/733/733558.png">

    <span>Instagram</span>

    </a>

    </div>

    </div>

    <div class="footer-column">

    <h3 class="footer-subtitle">        
    Tautan </h3>
    <a class="footer-link"
    href="https://upgrisba.ac.id">
    Website Universitas
    </a>
    <a class="footer-link"
    href="https://spmb.upgrisba.ac.id">
    Portal PMB
    </a>
    </div>
    </div>

    <div class="copyright">
    © 2026 Universitas PGRI Sumatera Barat
    </div>

    </div>

    <a class="whatsapp"
    href="https://wa.me/6285762228563?text=Halo%20Admin%20PMB%20Sains%20Data%20UPGRISBA"
    target="_blank">

    <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png">

    <span>
    Hubungi Kami
    </span>

    </a>

    """, unsafe_allow_html=True)
