import segno
qrcode = segno.make_qr("Hello Abhi please go to school tomorrow.. !!")
qrcode.save(
  "darkblue_qrcode.png",
  scale=5,
  dark="darkblue",
  light="lightblue",
  quiet_zone="maroon",
)