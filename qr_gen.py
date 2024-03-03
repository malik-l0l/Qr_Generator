"""
qrcode == 7.3.1
"""
import os

import qrcode

FILE_NAME = 'qrcode.png'
SAVE_FILE_IN = f"{os.path.abspath(f'{FILE_NAME}')}"


def generate_qrcode(text):
    # making qr code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    # add data to qr code
    qr.add_data(text)
    qr.make(fit=True)

    # decorate
    img = qr.make_image(fill_color="Black",
                        back_color="White")

    # save qrcode
    img.save(SAVE_FILE_IN)


if __name__ == '__main__':
    print("-- -- QR_MAKER -- --")
    generate_qrcode(input("Paste the link : "))
