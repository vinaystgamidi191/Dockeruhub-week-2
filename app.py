import qrcode

def generate_qr(url, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    url = "https://github.com/vinaystgamidi191"
    filename = "github_qr.png"
    generate_qr(url, filename)
    print(f"QR code generated for {url} saved as {filename}")
