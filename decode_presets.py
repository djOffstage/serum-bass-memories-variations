#!/usr/bin/env python3
import base64
from pathlib import Path

source = Path("presets.zip.b64")
target = Path("AU_MT_Serum_Bass_Presets_Inspired.zip")

# The committed payload is unpadded base64. Normalize whitespace and restore the
# optional '=' padding before decoding so Python versions behave consistently.
encoded = "".join(source.read_text(encoding="utf-8").split())
if "PLACEHOLDER_TOO_LONG" in encoded:
    raise SystemExit(
        "presets.zip.b64 is a placeholder, not a real archive. "
        "Restore the actual payload before decoding."
    )
encoded += "=" * (-len(encoded) % 4)
data = base64.b64decode(encoded, validate=True)

target.write_bytes(data)
print(f"Decoded zip ready: {target} ({len(data)} bytes). Extract the 10 .fxp files.")
