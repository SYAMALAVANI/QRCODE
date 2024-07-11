import segno
qrcode = segno.make_qr("Hello, Sai Please Read ra Yedava")
qrcode.save(
  "green_datadark_qrcode.png",
  scale=5,
  dark="darkblue",
  light="lightblue",
  data_dark = "green",
  data_light = "lightgreen",
)