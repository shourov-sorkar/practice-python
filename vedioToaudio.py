import imageio
import moviepy.editor

vedio = moviepy.editor.VideoFileClip('test.mp4')
audio = vedio.audio

audio.write_audiofile("done.mp3")

print("converted successfully!")