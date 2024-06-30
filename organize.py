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
    r"C:\Users\user_name\OneDrive",
    r"C:\Users\user_name\Downloads"
]


def organize(folder_name, file_type_list):
    for folder in folders:  
        folder = Path(folder)  
        for file in folder.rglob('*'):  
            if file.is_file():  
                suffix = file.suffix.replace('.', '').upper()  
                if any(suffix == ftype for ftype in all):  
                    if any(suffix == ftype for ftype in file_type_list):  
                        if not Path(f'{folder}/{folder_name}').exists():  
                            new_folder = Path(f'{folder}/{folder_name}')  
                            new_folder.mkdir()
                        try:
                            file.rename(f'{folder}/{folder_name}/{file.name}')  
                        except FileExistsError:
                            file.unlink()  
                else:
                    if not Path(folder / suffix).exists():  
                        new_folder = Path(folder / suffix)
                        new_folder.mkdir()  
                    try:
                        file.rename(folder / suffix / file.name)  
                    except FileExistsError:  
                        file.unlink()  

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
