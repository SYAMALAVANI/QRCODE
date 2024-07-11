import segno

qrcode = segno.make_qr("https://www.youtube.com/watch?v=RVLNBVK8auM")
qrcode_rotated = qrcode.to_pil(
  scale=5,
  light="lightblue",
  dark="green",
).rotate(45, expand=True)
qrcode_rotated.save("rotated_qrcode.png")