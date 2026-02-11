# Quick Start Guide

## Installation (3 Steps)

1. **Install Python** (if needed)
   - Download from python.org
   - Version 3.7 or higher required

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application**
   ```bash
   python image_processor.py
   ```

## First Time Use

1. **Load an Image**
   - Click "File" → "Open" (or press Ctrl+O)
   - Select a JPG, PNG, or BMP file (max 10MB)

2. **Try Some Effects**
   - Click "Grayscale" to convert to black & white
   - Use the "Blur Effect" slider and click "Apply Blur"
   - Try "Edge Detection" for cool outlines

3. **Undo if Needed**
   - Press Ctrl+Z to undo
   - Press Ctrl+Y to redo

4. **Save Your Work**
   - Click "File" → "Save As" (or press Ctrl+Shift+S)
   - Choose location and format

## Tips

- **Sliders**: Adjust before clicking apply button
- **Undo**: Supports up to 20 operations
- **Reset**: Use "Edit" → "Reset to Original" to start over
- **File Size**: Keep images under 10MB for best performance

## Common Operations

### Make Image Black & White
1. Load image
2. Click "Grayscale"
3. Done!

### Adjust Brightness
1. Load image
2. Move "Brightness" slider (-100 to 100)
3. Click "Apply Brightness"

### Rotate Image
1. Load image
2. Click "Rotate 90°", "Rotate 180°", or "Rotate 270°"

### Resize Image
1. Load image
2. Move "Resize" slider (10% to 200%)
3. Click "Apply Resize"

## Troubleshooting

**Can't open app?**
- Run: `pip install opencv-python numpy pillow`

**Image won't load?**
- Check file is JPG, PNG, or BMP
- Ensure file is under 10MB

**Need help?**
- Check README.md for detailed documentation
