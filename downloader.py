import pytube
from pytube import YouTube
from pyscript import document

def download(event):
    input_text = document.querySelector("#youtubelink")
    input = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = YouTube(input).streams.filter(progressive=True,res="720p").first().download()





