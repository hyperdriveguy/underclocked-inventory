import qrcode
import subprocess

def print_barcode(data):
    pil_qr = qrcode.make(data=data, error_correction=qrcode.constants.ERROR_CORRECT_Q)
    pil_qr.save('/tmp/inventory_qr.png')
    subprocess.run('lp -d Reciept /tmp/inventory_qr.png', check=True)
    
