# Advanced Image Processing Application

A comprehensive desktop application demonstrating Object-Oriented Programming principles, GUI development using Tkinter, and image processing using OpenCV.

## Features

### Object-Oriented Programming
The application is structured using three main classes:

1. **ImageData** - Encapsulates image data and metadata
   - Handles image loading, saving, and validation
   - Manages original and current image states
   - Provides encapsulated access to image properties

2. **ImageProcessor** - Handles all image processing operations
   - Implements all OpenCV-based filters and effects
   - Provides parameter validation and error handling
   - Encapsulates processing algorithms

3. **ImageProcessorGUI** - Main application interface
   - Manages the Tkinter GUI
   - Coordinates interaction between ImageData and ImageProcessor
   - Handles user input and display updates

### Image Processing Features (OpenCV)

1. **Grayscale Conversion** - Convert images to black and white
2. **Blur Effect** - Apply Gaussian blur with adjustable intensity (1-25)
3. **Edge Detection** - Canny edge detection algorithm
4. **Brightness Adjustment** - Adjust brightness (-100 to +100)
5. **Contrast Adjustment** - Adjust contrast (0.5x to 3.0x)
6. **Image Rotation** - Rotate by 90°, 180°, or 270°
7. **Image Flip** - Flip horizontally or vertically
8. **Resize/Scale** - Resize image (10% to 200% of original size)

### GUI Features (Tkinter)

#### Menu Bar
- **File Menu**
  - Open (Ctrl+O) - Load images (JPG, PNG, BMP)
  - Save (Ctrl+S) - Save to current file
  - Save As (Ctrl+Shift+S) - Save to new file
  - Exit (Ctrl+Q) - Close application

- **Edit Menu**
  - Undo (Ctrl+Z) - Undo last operation
  - Redo (Ctrl+Y) - Redo last undone operation
  - Reset to Original - Restore original image

#### Control Panel
- Scrollable sidebar with all processing tools
- Interactive sliders for:
  - Blur intensity
  - Brightness adjustment
  - Contrast factor
  - Resize scale
- Organized sections for easy navigation

#### Image Display Area
- Canvas with dark background
- Automatic image scaling to fit window
- Centered display
- Maintains aspect ratio

#### Status Bar
- Displays current filename
- Shows image dimensions
- Displays file size in KB

## Installation & Setup

### Requirements
- Python 3.7 or higher
- Required packages (see requirements.txt):
  - opencv-python
  - numpy
  - pillow
  - tkinter (usually included with Python)

### Installation Steps

1. **Install Python** (if not already installed)
   - Download from https://www.python.org/downloads/
   - Ensure "Add Python to PATH" is checked during installation

2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python image_processor.py
   ```

## Usage Guide

### Loading an Image
1. Click **File > Open** or press **Ctrl+O**
2. Select an image file (JPG, PNG, or BMP)
3. Maximum file size: 10MB
4. Image will be displayed on the canvas

### Applying Effects
1. Ensure an image is loaded
2. Navigate to the desired effect in the control panel
3. Adjust sliders if available
4. Click the corresponding button to apply the effect

### Using Undo/Redo
- **Undo**: Click **Edit > Undo** or press **Ctrl+Z**
- **Redo**: Click **Edit > Redo** or press **Ctrl+Y**
- History limit: 20 operations
- Undo/Redo applies to all image operations

### Saving Images
1. **Save**: Click **File > Save** or press **Ctrl+S**
   - Saves to the original file location
   - First-time saves will prompt for location

2. **Save As**: Click **File > Save As** or press **Ctrl+Shift+S**
   - Choose new filename and location
   - Select desired format (PNG, JPG, BMP)

### Resetting Image
- Click **Edit > Reset to Original** to restore the original image
- This action cannot be undone

## Error Handling & Input Validation

The application includes comprehensive error handling:

### File Validation
- File existence check
- File size limit (10MB maximum)
- Supported format validation
- Read/write permission checks

### Input Validation
- Slider values are constrained to safe ranges
- Invalid operations are prevented
- User-friendly error messages

### Runtime Error Handling
- Try-catch blocks for all operations
- Graceful fallback on errors
- Clear error messages to users

## Cross-Platform Compatibility

The application runs on:
- **Windows** - Fully tested and supported
- **macOS** - Compatible with all features
- **Linux** - Compatible with all features

Tkinter and OpenCV are cross-platform, ensuring consistent behavior across operating systems.

## Technical Details

### OOP Principles Demonstrated

1. **Encapsulation**
   - Private attributes with underscore prefix
   - Public getter methods for controlled access
   - Internal state hidden from external classes

2. **Constructor**
   - `__init__` methods in all classes
   - Proper initialization of attributes
   - Parameter passing and default values

3. **Methods**
   - Instance methods for object behavior
   - Clear separation of concerns
   - Well-defined interfaces

4. **Class Interaction**
   - GUI class uses ImageData and ImageProcessor
   - Clean separation between data, processing, and presentation
   - Dependency injection pattern

### Design Patterns
- **Model-View-Controller (MVC)** inspired architecture
- **Strategy Pattern** for image processing operations
- **Command Pattern** for undo/redo functionality

### Code Quality
- Type hints for better code clarity
- Comprehensive docstrings
- Error handling throughout
- Input validation at all entry points

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Image | Ctrl+O |
| Save Image | Ctrl+S |
| Save As | Ctrl+Shift+S |
| Exit | Ctrl+Q |
| Undo | Ctrl+Z |
| Redo | Ctrl+Y |

## Troubleshooting

### Issue: Application won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version is 3.7 or higher: `python --version`

### Issue: Can't load image
- Check file size (must be under 10MB)
- Verify file format (JPG, PNG, or BMP)
- Ensure file is not corrupted

### Issue: Slow performance
- Large images may take time to process
- Consider resizing image to smaller dimensions
- Close other applications to free memory

### Issue: Undo/Redo not working
- Ensure an image is loaded
- Undo/Redo only applies to image operations
- Check if history limit (20 operations) was reached

## License

This project is created for educational purposes to demonstrate OOP principles, GUI development, and image processing.

## Author

Created as a demonstration of:
- Object-Oriented Programming in Python
- Tkinter GUI Development
- OpenCV Image Processing
- Software Engineering Best Practices
