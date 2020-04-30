import subprocess
import stateCheck

def generate(color: str):
    color = color.strip()
    # print(f".\\ffmpeg\\bin\\ffmpeg.exe -y -hwaccel cuvid -f lavfi -r 0.1 -i color=color={color}  -t 3600 colors/{color}.mp4")
    subprocess.run(
        f".\\ffmpeg\\bin\\ffmpeg.exe -y -hwaccel cuvid -f lavfi -r 0.1 -i color=color={color}  -t 3600 colors/{color}.mp4",
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open("colorsWritten.txt","a") as file2:
        file2.write(color)
        file2.close()
    stateCheck.check_state()