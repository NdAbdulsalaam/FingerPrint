from pyfingerprint.pyfingerprint import PyFingerprint

try:
    # Adjust the COM port and baud rate as needed
    f = PyFingerprint('COM3', 57600, 0xFFFFFFFF, 0x00000000)  # Example COM port

    if f.verifyPassword():
        print("Password verified.")
        while not f.readImage():
            print("Waiting for finger...")
        print("Finger detected.")
    else:
        print("Failed to verify password.")

except Exception as e:
    print("Unable to intract with the FingerPrint Scanner.\nFind error detail below")
    print(f'Error: {e}')
