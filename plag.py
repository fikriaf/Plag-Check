import requests
import zipfile
import os

def create_zip_file(txtfile_path, zipfile_path):
    print(zipfile_path)
    with zipfile.ZipFile(zipfile_path, 'w') as zipf:
        zipf.write(txtfile_path, os.path.basename(txtfile_path))

def submit_to_dolos(name, zipfile_path):
    print(zipfile_path)
    with open(zipfile_path, 'rb') as file:
        response = requests.post(
            'https://dolos.ugent.be/api/reports',
            files={'dataset[zipfile]': file},
            data={'dataset[name]': name}
        )
    response.raise_for_status()  # Ensure the request was successful
    json = response.json()
    return json["html_url"]

# Contoh penggunaan:
# Buat file ZIP dari file teks
create_zip_file('teks.txt', 'teks.zip')

# Kirim file ZIP ke API Dolos
url = submit_to_dolos("Dokumen Saya", 'teks.zip')
print("Report URL:", url)
