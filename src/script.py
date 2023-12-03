import os
import shutil

source_dir = "C:/Users/Bartek/Downloads"
dest_dir_programs = "E:/POBRANE/Programs"
dest_dir_videos = "E:/POBRANE/Videos"
dest_dir_archive = "E:/POBRANE/Archive"
dest_dir_documents = "E:/POBRANE/Documents"
dest_dir_pictures = "E:/POBRANE/Pictures"
dest_dir_audio = "E:/POBRANE/Audio"
dest_dir_torrents = "E:/POBRANE/Torrents"
dest_dir_code = "E:/POBRANE/Code"
dest_dir_spreadsheet = "E:/POBRANE/Spreadsheets"
dest_dir_presentation = "E:/POBRANE/Presentations"


programs_format = [".exe",".msi"]
videos_format = [".mp4",".mov",".avi"]
archive_format = [".zip",".rar", ".7z"]
documents_format = [".pdf",".docx"]
pictures_format = [".jpg","png","tif","tiff","svg","raw"]
audio_format = [".mp3","wav"]
torrent_format = [".iso", ".torrent"]
code_format = [".html",".css",".js",".php",".tsx",".py",".sql",".cpp",".c",".java"]
spreadsheet_format = [".xlsx"]
presentation_format = [".pptx"]


def move_files(directory, formats, destination):
    files = os.listdir(directory)
    
    for file in files:
        if any(file.lower().endswith(ext) for ext in formats):
            source_path = os.path.join(directory, file)
            destination_path = os.path.join(destination, file)
            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {destination}")


def main():
    move_files(source_dir, programs_format, dest_dir_programs)
    move_files(source_dir, videos_format, dest_dir_videos)
    move_files(source_dir, archive_format, dest_dir_archive)
    move_files(source_dir, documents_format, dest_dir_documents)
    move_files(source_dir, pictures_format, dest_dir_pictures)
    move_files(source_dir, audio_format, dest_dir_audio)
    move_files(source_dir, torrent_format, dest_dir_torrents)
    move_files(source_dir, code_format, dest_dir_code)
    move_files(source_dir, spreadsheet_format, dest_dir_spreadsheet)
    move_files(source_dir, presentation_format, dest_dir_presentation)


if __name__ == '__main__':
    main()