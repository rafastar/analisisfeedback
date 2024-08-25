# Analisis Sentimen Feedback Pelayanan Instansi
Proyek ini merupakan aplikasi web untuk analisis sentimen menggunakan Streamlit. Aplikasi ini memungkinkan pengguna untuk memasukkan teks dan mendapatkan analisis sentimen secara real-time.

## Fitur

- **Analisis Sentimen**: Menilai sentimen dari teks yang dimasukkan, apakah positif, negatif, atau netral.
- **Antarmuka Pengguna**: Interface yang sederhana dan intuitif untuk memasukkan teks dan melihat hasil analisis.

## Penggunaan
Pengguna hanya perlu memasukkan feedback pada kolom isian dan menekan tombol prediksi sentimen untuk melihat hasil sentimen analisis feedback tersebut.

## Teknologi

- **Python**: Bahasa pemrograman utama.
- **Streamlit**: Untuk membuat aplikasi web interaktif.
- **NLTK**: Untuk pemrosesan teks dan analisis sentimen.
- **Naive Bayes**: sebagai algoritma yang digunakan untuk pemodelan.

## Proses Implementasi
- Data feedback dilakukan Preprocessing (Pembersihan data, tokenisasi, dan slang transformation)
- Pemberian label sentimen berdasarkan kata-kata positif dan kata-kata negatif
- Klasifikasi menggunakan algoritma naive bayes
- Pengujian Hasil

## Struktur Proyek
- **app.py**: Berkas utama streamlit.
- **requirements.txt**: Daftar dependensi python.
- **best_model.pkl** : Model yang digunakan.
- **best_vectorizer.pkl** : vectorizer yang digunakan.
- **readme.md** : dokumentasi proyek.

## Kontak
- Muhamad Rifqi R
