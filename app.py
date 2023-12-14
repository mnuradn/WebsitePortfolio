from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# --- PATH SETTINGS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "MuhammadNurAdnan_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
python_logo = current_dir / "assets" / "python.png"
msword_logo = current_dir / "assets" / "msword.png"
msexcel_logo = current_dir / "assets" / "msexcel.png"
msppt_logo = current_dir / "assets" / "msppt.png"
adae_logo = current_dir / "assets" / "adae.png"
adpr_logo = current_dir / "assets" / "adpr.png"
canva_logo = current_dir / "assets" / "canva.png"
postgre_logo = current_dir / "assets" / "postgre.png"
project1 = current_dir / "assets" / "Project1.png"
project2 = current_dir / "assets" / "Project2.png"
project3 = current_dir / "assets" / "Project3.png"
project4 = current_dir / "assets" / "Project4.png"
project5 = current_dir / "assets" / "Project5.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Muhammad Nur Adnan"
NAME = "MUHAMMAD NUR ADNAN"
DESCRIPTION = """
Bachelor's of Communication | Ex-Journalist at Gentra Priangan | Data Enthusiast
"""
EMAIL = "nuradnan70@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/muhammad-nur-adnan/",
    "Instagram":"https://www.instagram.com/mnuradn/",
    "GitHub":"https://github.com/mnuradn",

}

st.set_page_config(page_title=PAGE_TITLE)


# --- LOAD CSS, PDF, & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html= True)
with open(resume_file,'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
python_logo = Image.open(python_logo)
msword_logo = Image.open(msword_logo)
msexcel_logo = Image.open(msexcel_logo)
msppt_logo = Image.open(msppt_logo)
adae_logo = Image.open(adae_logo)
adpr_logo = Image.open(adpr_logo)
canva_logo = Image.open(canva_logo)
postgre_logo = Image.open(postgre_logo)
project1 = Image.open(project1)
project2 = Image.open(project2)
project3 = Image.open(project3)
project4 = Image.open(project4)
project5 = Image.open(project5)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= "📄 Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📫",EMAIL)


    
# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- CONTAINER ---
with st.container():
    selected = option_menu(
        menu_title= None,
        options= ['Tentang Saya','My Projects'],
        icons= ['person','code-slash'],
        orientation= 'horizontal'
    )

if selected == 'Tentang Saya':
    
    ### --- ABOUT ME ---
    st.write("""Lulusan Ilmu Komunikasi konsentrasi Jurnalistik di Universitas Garut yang memiliki minat kuat pada dunia teknologi. 
           Memiliki pengalaman bekerja sebagai jurnalis di salah satu media lokal di Kabupaten Garut. 
           Menguasai tools yang dibutuhkan dalam berkerja di bidang komunikasi dan data seperti Microsoft Office, Python, SQL, dan lain-lain. 
          Mampu bekerja secara kolaboratif dan memiliki keterampilan komunikasi yang baik.
          """)
    
    # --- SKILLS DAN TOOLS
    st.write("#")
    st.subheader("Skills & Tools")
    col1,col2,col3,col4 = st.columns(4, gap="small")
    with col1:
        st.write("""
              - Komunikasi
              - Adaptif
              - Kepemimpinan
             - Manajemen Waktu
              - Pemecahan Masalah
          """
     )
    with col2:
        st.image(msword_logo, width=70)
        st.image(msexcel_logo, width=70)
        st.image(msppt_logo, width=70)
    
    with col3:
        st.image(python_logo, width=65)
        st.image(adpr_logo, width=70)
        st.image(adae_logo, width=70)

    with col4:
        st.image(canva_logo, width=60)
        st.image(postgre_logo, width=60)

    # --- BAHASA
    st.write("#")
    st.subheader("🔠 Bahasa")
    st.write("""
        - 🇮🇩 Indonesia (Tingkat Fasih atau Bahasa Asli)
        - 🇬🇧 Inggris (Proficiency Test of English to Speakers of Other Languages Score: 493)
        """
    )

    # --- PENGALAMAN BEKERJA
    st.write("#")
    st.subheader("👷🏼‍♂️ Pengalaman Bekerja")
    st.write("---")

    # --- PEKERJAAN 1 ---
    st.write("🚧","**Jurnalis - Gentra Priangan**")
    st.write("**11/2021 - 02/2023**")
    st.write("""
            - Aktif mencari, mengumpulkan, dan menyusun berita terkini dengan cepat dan akurat. Memiliki kemampuan untuk merangkum informasi kompleks menjadi narasi yang mudah dimengerti oleh pembaca.

            - Melakukan wawancara dengan beragam narasumber, termasuk tokoh masyarakat, pejabat, dan sumber berita utama. Mampu mengajukan pertanyaan yang tajam dan mendalam telah membantu menghasilkan konten yang informatif dan berbobot.

            - Terlibat dalam pengeditan dan pemilihan gambar yang sesuai dengan konten berita. Keahlian saya dalam memilih elemen visual yang relevan telah meningkatkan daya tarik visual dan pengalaman pembaca dalam mengonsumsi informasi.

            - Mampu mengoptimalkan konten web, baik itu artikel berita, blog, maupun halaman produk, agar sesuai dengan pedoman terbaru dari mesin pencari. Saya juga terampil dalam memanfaatkan struktur HTML, metadata, dan elemen teknis lainnya untuk meningkatkan keterbacaan oleh mesin pencari.
        
            - Berkolaborasi dengan jurnalis lain, editor, dan fotografer untuk menghasilkan konten multimedia yang mendalam dan berdampak.
    """
    )
    # --- PENDIDIKAN ---
    st.write("#")
    st.subheader("👨🏼‍🎓 Pendidikan")
    st.write("---")

    # --- Education 1
    st.write("🎓","**S1, Jurnalistik / Fakultas Komunikasi dan Informasi - Universitas Garut**")
    st.write("**09/2019 - 11/2023**")
    st.write("**IPK 3,55/4,00**")
    st.write("""
    - Berpartisipasi sebagai Panitia dalam penyelenggaraan acara Seminar Pewarta Foto Indonesia (PFI) Bandung Visit To Campus Di Jawa Barat dengan tema "Proses Editorial Fotografi Dalam Media Massa" pada 10 September 2022.

    - Terpilih sebagai anggota Tim Ambassador dalam kegiatan Penerimaan Mahasiswa Baru UNIGA angkatan 2020/2021 dan angkatan 2021/2022.

    - Menjadi Mentor mahasiswa baru pada acara Pengenalan Kehidupan Kampus bagi Mahasiswa Baru (PKKMB) UNIGA angkatan 2021/2022.

    - Mengikuti Pelatihan Dasar Kepemimpinan dan Bela Negara bagi Mahasiswa UNIGA diselenggarakan oleh Yonif Raider 303/13/1 Kostrad pada September 2019 di Cikajang, Garut.

    """
    )

    # --- Education 2
    st.write("🎓","**Matematika dan Ilmu Pengetahuan Alam - SMAN 1 Lembang**")
    st.write("**06/2016 - 05/2019**")
    st.write("**Mean 88/100**")
    st.write("""
            - Juara 3 Lomba Maca Sajak Sunda Tingkat Provinsi dalam event Riksa Budaya Sunda di UPI, Februari 2018
        
            - Juara 2 Lomba Maca Sajak Sunda Kategori Putera Tingkat Provinsi dalam event Apresiasi Bahasa, Sastra, dan Aksara Sunda (ABSS) di Grand Hotel Lembang, September 2018.

            - Penata Artistik Terbaik dalam event Pasanggiri Monolog Basa Sunda (PMBS) di UNPAD, Oktober 2018

            - Juara Umum Monolog dalam event Pasanggiri Monolog Basa Sunda (PMBS) di UNPAD, Oktober 2018.
    """
    )

if selected == "My Projects":
    with st.container():
        st.header("Project 1")
        st.write("##")
        col5,col6 = st.columns((1,2))
        with col5:
            st.image(project1)
        with col6:
            st.subheader("Final Project E-Commerce Dataset Analysis")
            st.write("""
                     Proyek ini adalah tentang menganalisis dataset sebuah e-commerce di Brasil yang melibatkan data penjualan, 
                     inventaris produk, data pelanggan, dan ulasan produk. Tujuannya adalah untuk mendapatkan wawasan mengenai demografi pelanggan, 
                     penjualan produk terbaik dan terburuk, serta penggunaan metode pembayaran yang sering digunakan oleh pelanggan. Saya bertanggung jawab 
                     atas semua aspek proyek ini, mulai dari Data Wrangling, Exploratory Data Analysis, hingga penyusunan presentasi akhir. Saya menggunakan 
                     alat analisis data seperti Python untuk menggali wawasan dari dataset, serta merancang visualisasi yang efektif untuk menjelaskan temuan kepada berbagai audiens. 
                     """)
            st.markdown("[Publication Link](https://drive.google.com/drive/folders/1RJs3zjaepwto0-VZrJisF_x1Zl4YmG4N?usp=sharing)")
    
    with st.container():
        st.header("Project 2")
        st.write("##")
        col5,col6 = st.columns((1,2))
        with col5:
            st.image(project2)
        with col6:
            st.subheader("Forecasting COVID-19 Jakarta dengan Supervised Learning")
            st.write("""
                     Proyek ini fokus pada perkiraan COVID-19 di Jakarta menggunakan pendekatan Supervised Learning. Proyek ini merupakan tugas persyaratan 
                     untuk mengikuti kegiatan COMFEST UI 2023. Tujuan dari proyek ini untuk mengembangkan model ML yang efektif untuk meramalkan kasus COVID-19 di Jakarta. 
                     Saya berkontribusi dalam tahap Data Wrangling dan Presentation pada proyek ini. Saya bertanggung jawab untuk mengumpulkan data, membersihkannya, dan memastikan 
                     bahwa dataset yang digunakan dalam analisis sudah siap untuk diolah lebih lanjut. Selain itu, Saya juga berperan dalam membuat presentasi hasil dari proyek ini.  
                     """)
            st.markdown("[Publication Link](https://drive.google.com/drive/folders/1wnxQ_tOPDhL3WJoYcEjbf9xFhCjdb7O6?usp=sharing)")

    with st.container():
        st.header("Project 3")
        st.write("##")
        col5,col6 = st.columns((1,2))
        with col5:
            st.image(project3)
        with col6:
            st.subheader("Dicoding Collection (DiCo) Dataset Analysis")
            st.write("""
                     Proyek ini berkaitan dengan analisis data dari Dicoding, yang merupakan salah satu platform yang memberikan pelatihan mengenai ilmu komputer. 
                     Proyek ini mencakup penerapan teknik analisis data menggunakan bahasa pemrograman Python untuk menggali wawasan dari dataset tersebut. 
                     Tujuan dari proyek ini adalah untuk mempraktikkan metode analisis data, seperti pembersihan data, eksplorasi, dan visualisasi, serta untuk memahami 
                     bagaimana berbagai aspek dari dataset berhubungan satu sama lain. ini adalah proyek yang sangat berharga karena memungkinkan Saya untuk mengasah keterampilan 
                     analisis data menggunakan Python dalam lingkungan yang terstruktur seperti Dicoding.  
                     """)
            st.markdown("[Publication Link](https://github.com/mnuradn/DiCo-analysis)")

    with st.container():
        st.header("Project 4")
        st.write("##")
        col5,col6 = st.columns((1,2))
        with col5:
            st.image(project4)
        with col6:
            st.subheader("Journalist at Gentra Priangan")
            st.write("""
                    Saya menganggap pengalaman bekerja sebagai jurnalis di Gentra Priangan bukan sebagai proyek dalam konteks yang sama seperti proyek analisis data atau pengembangan aplikasi. 
                    Namun, pengalaman ini tetap sangat berharga bagi Saya karena merupakan bagian dari perjalanan profesional Saya yang membentuk keterampilan komunikasi, penelitian, dan wawasan 
                    dalam dunia berita. Ini adalah pengalaman penting yang telah memperkaya wawasan Saya tentang dunia media. Pengalaman ini berhubungan dengan pekerjaan saya sebagai jurnalis di 
                    media online local yang ada di Kabupaten Garut bernama Gentra Priangan. Saya terlibat dalam mencari, mengumpulkan, dan menyusun berita berbagai topik, mulai dari berita lokal hingga nasional. 
                    Proyek ini memungkinkan saya untuk mempraktikkan prinsip-prinsip jurnalisme, seperti menyusun laporan berita yang akurat, serta mengasah kemampuan menulis berita dengan bahasa yang efektif. 
                    Sebagai Jurnalis di Gentra Priangan, kontribusi Saya adalah mencari dan mengumpulkan informasi, melakukan wawancara, dan menyusun berita berdasarkan fakta yang Saya temukan. Saya juga bertanggung jawab 
                    untuk memastikan berita yang Saya susun sesuai dengan standar etika jurnalisme dan memiliki nilai informatif bagi pembaca. Selain itu, Saya terlibat dalam menghadiri acara dan konferensi pers, 
                    serta berkolaborasi dengan rekan-rekan jurnalis dan editor.
                    """)
            st.markdown("[Publication Link](https://drive.google.com/drive/folders/1eG5pK3cqfxKoOVAwopwyOByzu-zJm-xM?usp=sharing)")

    with st.container():
        st.header("Project 5")
        st.write("##")
        col5,col6 = st.columns((1,2))
        with col5:
            st.image(project5)
        with col6:
            st.subheader("Berita Wisata CNN Media")
            st.write("""
                    Proyek ini berkaitan dengan tugas kelompok pembuatan video berita wisata tentang Candi Cangkuang. Candi Cangkuang adalah satu-satunya Candi yang ditemukan di daerah Jawa Barat 
                    dan juga tempat wisata yang memiliki nilai historis dan budaya yang kaya. Video ini bertujuan untuk memperkenalkan keindahan dan sejarah candi kepada audiens, mengajak mereka 
                    untuk menjelajahi tempat tersebut dan merasakan pengalaman wisata sejarah dan religi. Sebagai editor video, Saya merangkai klip-klip video yang telah diambil oleh tim kami, 
                    menambahkan efek visual, dan menciptakan alur visual yang menarik. Sebagai penulis naskah, Saya menyusun teks berita yang informatif untuk mendukung video, menjelaskan sejarah 
                    dan pesona Candi Cangkuang, serta membangun koneksi emosional dengan audiens.
                    """)
            st.markdown("[Publication Link](https://drive.google.com/drive/folders/1wO4KoDtj_kQDJaau69hLCxK0xUBv7-DD?usp=sharing)")












