import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://www.youtube.com/@meroinfohub")
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("Mero_Info_Hub.png")
