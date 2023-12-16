import sys
from pathlib import Path

images_files, video_files, audio_files, documents_files = [], [], [], []
folders, archives, others = [], [], []
unknown, extensions = set(), set()

registered_extensions = {
    'JPEG': images_files,
    'PNG': images_files,
    'JPG': images_files,
    'SVG': images_files,
    'AVI': video_files,
    'MP4': video_files,
    'MOV': video_files,
    'MKV': video_files,
    'DOC': documents_files,
    'DOCX': documents_files,
    'TXT': documents_files,
    'PDF': documents_files,
    'XLSX': documents_files,
    'PPTX': documents_files,
    'MP3': audio_files,
    'OGG': audio_files,
    'WAV': audio_files,
    'AMR': audio_files,
    'ZIP': archives,
    'GZ': archives,
    'TAR': archives
}

def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('IMAGES', 'VIDEO', 'AUDIO', 'DOCUMENTS', 'ARCHIVES', 'OTHER'):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)

# if __name__ == '__main__':
#     path = sys.argv[1]
#     print(f"Start in {path}")
#     folder = Path(path)
#     scan(folder)
