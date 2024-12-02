# Check Plagiarism Script

Script ini digunakan untuk mengecek plagiarisme menggunakan API Dolos.

## Fitur
- Membuat file ZIP dari file teks yang ditentukan.
- Mengirim file ZIP ke API Dolos.
- Mendapatkan URL laporan plagiarisme dalam bentuk HTML.

## Prasyarat
Pastikan bahwa Anda memiliki library berikut terinstal:
- `requests`
- `zipfile` (bagian dari Python standard library)
- `os` (bagian dari Python standard library)

Untuk menginstal `requests`, gunakan perintah berikut:

```bash
pip install requests
```
## Cara penggunaan
- Masukkan teks yang ingin di scan ke dalam file text.txt
- Kemudian, jalankan program menggunakan perintah berikut:
```bash
python plag.py
```

## Catatan
- API Dolos membutuhkan file ZIP untuk proses pengiriman.
- Pastikan file teks yang ingin diperiksa sudah ada dan path-nya benar.
- URL laporan akan dikembalikan jika proses berhasil.
