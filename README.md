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
import pngdata

pngdata.encode('example text', 'example.png')

data = pngdata.decode('example.png')
print(data)  # prints "example text"

# if no fp argument supplied encode returns BytesIO
png_encoded = pngdata.encode('example text')
png_decoded = pngdata.decode(png_encoded)
print(png_decoded)  # prints "example text"

# of course you can save BytesIO to file
with open('bytesio.png', 'wb') as f:
    # seek needed, because png_encoded was read before
    png_encoded.seek(0)
    f.write(png_encoded.read())

data = pngdata.decode('bytesio.png')
print(data)  # prints "example text"
```