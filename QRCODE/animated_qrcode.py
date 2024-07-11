import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=9S_tPUbbdLk&list=RD9S_tPUbbdLk&start_radio=1")
pages_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qrcode.to_artistic(
    background=pages_url,
    target="animated_qrcode.gif",
    scale=5,
)