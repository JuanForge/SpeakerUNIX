import os
import ctypes

lib = ctypes.CDLL("./SpeakerUNIX.so")
lib.beep.argtypes = [ctypes.c_int, ctypes.c_int]
lib.beep.restype = None

def beep(freq, duration_ms):
    if os.geteuid() != 0:
        raise PermissionError("Requires root")
    lib.beep(freq, duration_ms)

if __name__ == "__main__":
    beep(1000, 500)
