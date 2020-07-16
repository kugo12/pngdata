# pngdata
Write data to PNG file format

## Installation

```bash
python -m pip install pngdata
```

## CLI Usage

Encode
```bash
python -m pngdata e <file path> <text to encode>
```
Decode
```bash
python -m pngdata d <file path>
```

## Examples

```python
from pngdata import PNGData

with open('example.png', 'wb') as f:
    PNGData.encode('example text', f)

with open('example.png', 'rb') as f:
    data = PNGData.decode(f)
    print(data)  # prints "example text"

# if no fp argument supplied encode returns BytesIO
png_encoded = PNGData.encode('example text')
png_decoded = PNGData.decode(png_encoded)
print(png_decoded)  # prints "example text"

# of course you can save BytesIO to file
with open('example.png', 'wb') as f:
    # seek needed, because png_encoded was read before
    png_encoded.seek(0)
    f.write(png_encoded.read())

with open('example.png', 'rb') as f:
    data = PNGData.decode(f)
    print(data)  # prints "example text"
```