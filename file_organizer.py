import os 
import shutil 

def list_files(folders):
    return [f for f in os.listdir(folders) if os.path.isfile(os.path.join(folders,f))]
        
def get_extension(filename):
    name,ext=os.path.splitext(filename)
    return ext

def create_folder_if_missing( path):
    if not(os.path.exists(path)):
        os.makedirs(path)

def organize(folder):
    create_folder_if_missing(os.path.join(folder,'images'))
    create_folder_if_missing(os.path.join(folder,'pdfs'))
    create_folder_if_missing(os.path.join(folder,'code'))
    create_folder_if_missing(os.path.join(folder,'audio'))
    create_folder_if_missing(os.path.join(folder,'video'))
    create_folder_if_missing(os.path.join(folder,'misc'))
    files=list_files(folder)
    for f in files:
        ext=get_extension(f)
        if ext in ['.jpg','.jpeg','.png','.gif']:
            shutil.move(os.path.join(folder, f), os.path.join(folder, 'images', f))
        elif ext=='.pdf':
            shutil.move(os.path.join(folder,f),os.path.join(folder,'pdfs',f))
        elif ext in ['.py','.js','.html','.css']:
            shutil.move(os.path.join(folder,f),os.path.join(folder,'code',f))
        elif ext in ['.mp3','.wav']:
            shutil.move(os.path.join(folder,f),os.path.join(folder,'audio',f))
        elif ext in ['.mp4','.mov']:
            shutil.move(os.path.join(folder,f),os.path.join(folder,'video',f))
        else:
            shutil.move(os.path.join(folder,f),os.path.join(folder,'misc',f))   

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ")
    organize(folder)
    print("Done.")
