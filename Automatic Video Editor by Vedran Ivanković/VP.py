import os
import subprocess
import random
from moviepy.editor import VideoFileClip
import time
import os
path = "C:/Users/Ivankovic/Desktop/list"

vids = []
x = os.listdir("C:/Users/Ivankovic/Desktop/list")
for xs in x:
    r = "file '"+ path +"/"+ xs+"'"
    vids.append(r)

print(vids)

with open('your_file.txt', 'w') as f:
    for item in vids:
        f.write("%s\n" % item)

#C:/Users/Ivankovic/Desktop/list/input.mp4
subprocess.call('ffmpeg -f concat -safe 0 -i your_file.txt -c copy C:/Users/Ivankovic/Desktop/out.mp4', shell=True)

inputforfiles = "C:/Users/Ivankovic/Desktop/out.mp4"
numofclips = int(input("Enter the number of clips: "))
lenghtofslide = input("Enter the lenght of slides: ")

seconds = 60


clip = VideoFileClip(inputforfiles)
dur = round(clip.duration)

def numtotime(num):
    SS = num%60
    MM = num/60
    return ("00:"+str(MM)+":"+str(SS))


def getLength(filename):
    result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    return [x for x in result.stdout.readlines() if "Duration" in x]


def cutthevideo(video):
    x = 0
    for c in range(1000,1000+numofclips):

        rnd = round(random.uniform((c-1000)/(numofclips+1)*dur, (c+1-1000)/(numofclips+1)*dur - 3))
        numtotime(rnd)
        subprocess.call('ffmpeg -ss {}.0 -i {} -c copy -t {}.0 {}.mp4'.format(rnd,video,lenghtofslide,c),
                        shell=True)




open('mylist.txt', 'w').close()
print("Cutting the videos")
print("==================")
cutthevideo(inputforfiles)
print("Cutting Done")
print("Saving all videos in one file")
print("==================")
subprocess.call('''(for %i in (*.mp4) do @echo file '%i') > mylist.txt''', shell=True)
# subprocess.call('''printf "file '%s'\n" ./*.wav > mylist.txt''', shell=True)
print("Prepearing for joining the videos")
print("==================")
subprocess.call('ffmpeg -f concat -safe 0 -i mylist.txt -c copy C:/Users/Ivankovic/Desktop/output.mp4', shell=True)
subprocess.call('ffmpeg -i C:/Users/Ivankovic/Desktop/output.mp4 -i Relax.mp3 -c:v copy -map 0:v:0 -map 1:a:0 -shortest'
                ' '
                'C:/Users/'
                'Ivankovic/Desktop/new.mp4', shell=True)

for c in range(1000,1000+numofclips):
    os.remove("{}.mp4".format(c))


os.remove("C:/Users/Ivankovic/Desktop/output.mp4")





os.remove("C:/Users/Ivankovic/Desktop/out.mp4")


print("All done")


