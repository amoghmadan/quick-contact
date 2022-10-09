from io import BytesIO

import qrcode
from qrcode.image.pil import PilImage


def generate_qr(text: str) -> bytes:
    """
    Convert text to QR
    :param text: str
    :return: bytes
    """
    image: PilImage = qrcode.make(text)
    with BytesIO() as buffered:
        image.save(buffered, "PNG")
        ret: bytes = buffered.getvalue()
    return ret
