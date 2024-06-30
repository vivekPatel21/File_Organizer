from pathlib import Path

excel = ['XLSM', 'XLSX', 'XLS', 'CSV', 'XLAM', 'XLA']
photos = ['JPG', 'JPEG', 'PNG', 'GIF', 'SVG', 'BMP']
music = ['MP3', 'WAV', 'FLAC']
video = ['MP4', 'AVI', 'MOV']
python = ['PY', 'PYTHON', 'IPYNB']
pdf = ['PDF']
zip_files = ['ZIP', 'RAR', '7Z']
powerpoint = ['PPT', 'PPTX', 'ODP']
text = ['TXT']
apps = ['EXE']
html = ['HTML']
word = ['DOC', 'DOCX']
secure = ['CER', 'KEY', 'REN', 'REQ']

all = excel + photos + music + video + python + pdf + zip_files + powerpoint + text + apps + html + word + secure

folders = [
    r"C:\Users\vivek\OneDrive",
    r"C:\Users\vivek\Downloads"
]


def organize(folder_name, file_type_list):
    #TODO

def delete_empty_folders():
    for folder in folders:
        folder = Path(folder)
        for x in range(10):
            for file in folder.rglob('**/**'):
                if file.is_dir():
                    try:
                        file.rmdir()
                    except:
                        pass    


organize('EXCEL', excel)
organize('PHOTOS', photos)
organize('MUSIC', music)
organize('VIDEO', video)
organize('PYTHON', python)
organize('PDF', pdf)
organize('ZIP', zip_files)
organize('POWERPOINT', powerpoint)
organize('TEXT', text)
organize('APPS', apps)
organize('HTML', html)
organize('WORD', word)
organize('SECURE', secure)
delete_empty_folders()
