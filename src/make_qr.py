import qrcode
import subprocess

def print_barcode(data):
    """Prints a QR code for any given data.

    Args:
        data: data to be encoded on the QR code

    Returns:
        tuple( printer_message, printer_errors, exit_code )
    """
    pil_qr = qrcode.make(data=data, error_correction=qrcode.constants.ERROR_CORRECT_Q)
    # TODO don't hardcode some directories?
    pil_qr.save('/tmp/inventory_qr.png')
    print_status = subprocess.run(['lp', '-d', 'Reciept', '/tmp/inventory_qr.png'], text=True, capture_output=True)
    # print('lp says:', print_status.stdout.strip())
    # print('errors:', print_status.stderr.strip())
    # print('exit code: ', print_status.returncode)
    return (print_status.stdout.strip(),
        print_status.stderr.strip(),
        print_status.returncode)
