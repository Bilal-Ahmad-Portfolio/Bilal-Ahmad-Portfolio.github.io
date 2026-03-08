from PIL import Image
import subprocess
import sys
import os

def get_image_dimensions(path):
    with Image.open(path) as img:
        return img.width, img.height

def file_manager():
    if len(sys.argv) != 2:
        print("Usage: python file.py <file_name>")
        sys.exit(1)
    
    orignalfname = sys.argv[1]
    w,h = get_image_dimensions(orignalfname)
    dime = f"{w}x{h}"
    fname, ext = os.path.splitext(orignalfname)

    if ext.lower() not in ['.jpg', '.jpeg', '.png']:
        print("Unsupported file format. Please use .jpg, .jpeg, or .png.")
        sys.exit(1)

    if os.path.exists(f"{orignalfname}"):
        print(f"Processing {orignalfname} with dimensions {w}x{h}")
        return fname, ext, dime
    else:
        print(f"{orignalfname} not found, exiting...")
        sys.exit(1)

def main():
    fname, ext, dime = file_manager()    


    # 2560 x 1440, 2560 x 1439
    if dime == '2560x1440' or dime == '2560x1439':
        if fname.endswith("-scaled"):
            fname = fname[:-7]
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}-scaled{ext}" -vcodec mjpeg -q:v 5 -vf scale=200:-1 "{fname}-200x113{ext}"')  
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}-scaled{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x432{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}-scaled{ext}" -vcodec mjpeg -q:v 5 -vf scale=1536:-1 "{fname}-1536x864{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}-scaled{ext}" -vcodec mjpeg -q:v 5 -vf scale=2048:-1 "{fname}-2048x1152{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}-scaled{ext}" -vcodec mjpeg -q:v 5 -vf scale=2560:-1 "{fname}-scaled{ext}"')
        else:
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=200:-1 "{fname}-200x113{ext}"')  
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x432{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1536:-1 "{fname}-1536x864{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=2048:-1 "{fname}-2048x1152{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=2560:-1 "{fname}{ext}"')

    # 2560 x 1433, 1357 x 760
    elif dime == '2560x1433' or dime == '1357x760':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-200x113{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x430{ext}"')
        if dime == '2560x1433':
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1536:-1 "{fname}-1536x860{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=2048:-1 "{fname}-2048x1147{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=2560:-1 "{fname}{ext}"')
        else:
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1357:-1 "{fname}{ext}"')
   
    # 1920 x 1080, 1440 x 810
    elif dime == '1920x1080' or dime == '1440x810':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=200:-1 "{fname}-200x113{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x432{ext}"')
        if dime == '1920x1080':            
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1536:-1 "{fname}-1536x864{ext}"')
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1920:-1 "{fname}{ext}"')
        else:
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1440:-1 "{fname}{ext}"')
    
    # 1500 x 1500, 1200 x 1200
    elif dime == '1280x1280' or dime == '1500x1500':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=113:-1 "{fname}-113x113{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x768{ext}"')     
        # 1500x1500
        if dime == '1500x1500':
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1500:-1 "{fname}{ext}"')        
        # 1280x1280
        if dime == '1280x1280':
            subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1280:-1 "{fname}{ext}"')
 
    # 1878 x 1055
    elif dime == '1878x1055':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1536:-1 "{fname}-1536x863{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x431{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=200:-1 "{fname}-200x113{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1878:-1 "{fname}{ext}"')

    # 1878 x 996
    elif dime == '1878x996':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1536:-1 "{fname}-1536x815{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x407{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=200:-1 "{fname}-200x106{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1878:-1 "{fname}{ext}"')

    # 1806 x 952
    elif dime == '1806x952':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1536:-1 "{fname}-1536x810{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x405{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=200:-1 "{fname}-200x105{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1806:-1 "{fname}{ext}"')

    # 1431 x 583
    elif dime == '1431x583':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x313{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=200:-1 "{fname}-200x81{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1431:-1 "{fname}{ext}"')

    # 1280 x 1264
    elif dime == '1280x1264':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x758{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=114:-1 "{fname}-114x113{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1280:-1 "{fname}{ext}"')

    # 1280 x 720
    elif dime == '1280x720':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=200:-1 "{fname}-200x113{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x432{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=1280:-1 "{fname}{ext}"')

    # 787 x 749
    elif dime == '787x749':
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=768:-1 "{fname}-768x731{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=119:-1 "{fname}-119x113{ext}"')
        subprocess.run(rf'ffmpeg -hide_banner -loglevel error -y -i "{fname}{ext}" -vcodec mjpeg -q:v 5 -vf scale=787:-1 "{fname}{ext}"')

    else:
        print(f"Unsupported aspect ratio: {dime}")
        sys.exit(1)

if __name__ == "__main__":
    main()