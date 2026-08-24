#!/usr/bin/env python3
import base64, sys, os
with open("presets.zip.b64", "r") as f:
    data = base64.b64decode(f.read())
with open("AU_MT_Serum_Bass_Presets_Inspired.zip", "wb") as f:
    f.write(data)
print("Decoded zip ready. Extract the 10 .fxp files.")
