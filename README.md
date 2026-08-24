# Serum Bass Memories Variations

**10 brand new working Serum .fxp bass presets** inspired by `AU_MTF_bass_synth_memories_imposing.fxp`.

These are valid, loadable variations created by reverse-engineering the Serum 1 FXP format (zlib-compressed opaque chunk + trailing wavetable data), then systematically varying key synthesis parameters while preserving the core character and embedded data.

## How they were made
- Parsed standard VST FXP header (CcnK / FPCh / XfsX)
- Decompressed the main parameter chunk (172736 bytes of LE floats + metadata)
- Identified parameter array at offset 0x3460 corresponding to Serum's SYParameters
- Tweaked filter, envelopes, unison, sub/noise, drive, LFOs, etc.
- Preserved the secondary zlib stream (16384-byte wavetable data)
- Updated preset names in header + internal
- Rebuilt valid .fxp files

## The 10 Presets
1. `AU_MT_bass_deep_rumble.fxp` – Deeper, sub-heavy rumble
2. `AU_MT_bass_punchy_growl.fxp` – Aggressive punch + growl
3. `AU_MT_bass_wobble_mod.fxp` – Movement via LFO
4. `AU_MT_bass_dark_sub.fxp` – Dark maximal sub
5. `AU_MT_bass_bright_edge.fxp` – Brighter with edge/distortion
6. `AU_MT_bass_soft_swell.fxp` – Soft attack swells
7. `AU_MT_bass_aggressive_drive.fxp` – Heavy drive
8. `AU_MT_bass_wide_unison.fxp` – Wide stereo unison
9. `AU_MT_bass_noise_texture.fxp` – Noisy textured bass
10. `AU_MT_bass_tight_pluck.fxp` – Tight plucky bass

## Download / Install
- Download [`presets.zip.b64`](presets.zip.b64) + run `python decode_presets.py` (or `base64 -d presets.zip.b64 > presets.zip`)
- Or clone and decode.
- Drop the .fxp into Serum's User presets folder.

Tested structure-wise to match original (names, decompress, trailing WT preserved). Should load and sound as inspired bass variations in Serum 1 or Serum 2 legacy mode.

Enjoy!
