# Project Structure & Architecture

## File Organization

```
image_processor/
│
├── image_processor.py      # Main application file
├── requirements.txt         # Python dependencies
├── README.md               # Full documentation
├── QUICKSTART.md           # Quick start guide
└── PROJECT_STRUCTURE.md    # This file
```

## Class Architecture

### 1. ImageData Class
**Purpose**: Data management and encapsulation

**Attributes** (Private/Encapsulated):
- `_original_image`: Original loaded image (numpy array)
- `_current_image`: Current working image with applied effects
- `_filename`: Name of the image file
- `_file_path`: Full path to the image file
- `_dimensions`: Tuple of (width, height)
- `_file_size`: File size in bytes

**Methods**:
- `__init__()`: Constructor - initializes all attributes
- `load_image(file_path)`: Load and validate image file
- `save_image(file_path)`: Save current image to disk
- `update_current_image(image)`: Update working image
- `reset_to_original()`: Reset to original state
- `get_current_image()`: Getter for current image
- `get_original_image()`: Getter for original image
- `get_filename()`: Getter for filename
- `get_dimensions()`: Getter for dimensions
- `get_file_size()`: Getter for file size
- `has_image()`: Check if image is loaded

**OOP Principles Demonstrated**:
- ✓ Encapsulation (private attributes with _ prefix)
- ✓ Constructor (__init__)
- ✓ Methods (instance methods)
- ✓ Getter methods for controlled access

### 2. ImageProcessor Class
**Purpose**: Image processing operations using OpenCV

**Attributes** (Private):
- `_min_blur_kernel`: Minimum blur kernel size
- `_max_blur_kernel`: Maximum blur kernel size

**Methods**:
- `__init__()`: Constructor - initializes processor settings
- `convert_to_grayscale(image)`: Grayscale conversion
- `apply_blur(image, intensity)`: Gaussian blur with validation
- `detect_edges(image, threshold1, threshold2)`: Canny edge detection
- `adjust_brightness(image, value)`: Brightness adjustment
- `adjust_contrast(image, value)`: Contrast adjustment
- `rotate_image(image, angle)`: Image rotation (90°, 180°, 270°)
- `flip_image(image, direction)`: Horizontal/vertical flip
- `resize_image(image, scale_percent)`: Image scaling

**OOP Principles Demonstrated**:
- ✓ Encapsulation (processing algorithms hidden)
- ✓ Constructor (__init__)
- ✓ Methods (processing operations)
- ✓ Input validation

### 3. ImageProcessorGUI Class
**Purpose**: User interface and application coordination

**Attributes**:
- `root`: Tkinter root window
- `image_data`: Instance of ImageData class
- `processor`: Instance of ImageProcessor class
- `undo_stack`: List for undo history
- `redo_stack`: List for redo history
- `max_history`: Maximum undo/redo operations
- `display_image`: Current PhotoImage for display
- Various GUI components (canvas, sliders, buttons, etc.)

**Methods**:
- `__init__(root)`: Constructor - initializes GUI and components
- `_setup_menu()`: Create menu bar
- `_setup_ui()`: Create main UI layout
- `_setup_control_panel()`: Create control sidebar
- `_setup_image_display()`: Create image canvas
- `_setup_status_bar()`: Create status bar
- `_update_status()`: Update status bar text
- `_save_to_history()`: Save state for undo
- `_undo()`: Undo last operation
- `_redo()`: Redo last undone operation
- `_reset_to_original()`: Reset to original image
- `_open_image()`: Open image file dialog
- `_save_image()`: Save current image
- `_save_image_as()`: Save as dialog
- `_display_current_image()`: Update canvas display
- `_apply_operation()`: Generic operation wrapper
- `_apply_grayscale()`: Apply grayscale filter
- `_apply_blur()`: Apply blur effect
- `_apply_edge_detection()`: Apply edge detection
- `_apply_brightness()`: Apply brightness adjustment
- `_apply_contrast()`: Apply contrast adjustment
- `_apply_rotation()`: Apply rotation
- `_apply_flip()`: Apply flip
- `_apply_resize()`: Apply resize
- `_on_closing()`: Handle window close event

**OOP Principles Demonstrated**:
- ✓ Class Interaction (uses ImageData and ImageProcessor)
- ✓ Constructor (__init__)
- ✓ Methods (GUI event handlers)
- ✓ Encapsulation (internal GUI state)

## Class Interaction Diagram

```
┌─────────────────────────┐
│  ImageProcessorGUI      │
│  (Main Application)     │
│                         │
│  - Manages UI           │
│  - Handles user input   │
│  - Coordinates workflow │
└────────┬────────┬───────┘
         │        │
         │        │
         ▼        ▼
┌────────────┐  ┌──────────────┐
│ ImageData  │  │ ImageProcessor│
│            │  │              │
│ - Stores   │  │ - Processes  │
│   images   │  │   images     │
│ - Manages  │  │ - Applies    │
│   metadata │  │   filters    │
└────────────┘  └──────────────┘
```

## Data Flow

1. **Loading Image**:
   ```
   User → GUI → ImageData.load_image() → File System
   ```

2. **Applying Effect**:
   ```
   User → GUI → ImageData.get_current_image() →
   ImageProcessor.apply_effect() → ImageData.update_current_image() →
   GUI.display_image()
   ```

3. **Saving Image**:
   ```
   User → GUI → ImageData.save_image() → File System
   ```

4. **Undo/Redo**:
   ```
   User → GUI.undo_stack/redo_stack → ImageData.update_current_image() →
   GUI.display_image()
   ```

## Error Handling Strategy

### File Operations
- File existence validation
- File size limits (10MB)
- Format validation (JPG, PNG, BMP)
- Read/write permission checks
- Try-catch blocks with user-friendly messages

### Image Processing
- Input parameter validation
- Range constraints on sliders
- Null/empty image checks
- OpenCV operation error handling
- Graceful fallback on failures

### GUI Operations
- Prevent operations without loaded image
- Confirmation dialogs for destructive actions
- Status updates for user feedback
- Keyboard shortcut handling

## Design Patterns Used

1. **Model-View-Controller (MVC)**
   - Model: ImageData (data)
   - View: ImageProcessorGUI (presentation)
   - Controller: ImageProcessorGUI (logic)

2. **Strategy Pattern**
   - ImageProcessor provides different processing algorithms
   - Swappable strategies for different effects

3. **Command Pattern**
   - Undo/Redo implementation
   - Operation history management

4. **Facade Pattern**
   - ImageProcessor provides simple interface to complex OpenCV operations

## Input Validation

### File Validation
- Maximum size: 10MB
- Supported formats: JPG, JPEG, PNG, BMP
- File existence check
- Readable file check

### Parameter Validation
- Blur intensity: 1-25 (converted to odd kernel size)
- Brightness: -100 to 100
- Contrast: 0.5 to 3.0
- Rotation: 90, 180, or 270 degrees
- Resize: 10% to 200%

### Runtime Validation
- Image loaded before operations
- Valid image format
- Sufficient memory
- Valid file paths for save

## Cross-Platform Considerations

### Operating System Compatibility
- **Windows**: Full support (tested)
- **macOS**: Full support (Tkinter + OpenCV compatible)
- **Linux**: Full support (Tkinter + OpenCV compatible)

### Path Handling
- Uses `os.path` for cross-platform paths
- Relative paths handled correctly
- File dialogs use native OS dialogs

### Display Scaling
- Canvas automatically adjusts to window size
- Images scaled to fit display
- Maintains aspect ratio
- Works on different DPI settings

## Performance Considerations

1. **Memory Management**
   - Images copied when needed (not referenced)
   - Undo stack limited to 20 operations
   - Large images automatically scaled for display

2. **Processing Efficiency**
   - OpenCV operations optimized
   - NumPy arrays for fast processing
   - Minimal image conversions

3. **UI Responsiveness**
   - Operations complete before UI update
   - Status bar provides feedback
   - Error handling prevents freezing

## Security Considerations

1. **File Size Limits**
   - Maximum 10MB prevents memory issues
   - Prevents potential DoS attacks

2. **Input Validation**
   - All user inputs validated
   - File paths sanitized
   - Format verification

3. **Error Messages**
   - No sensitive information exposed
   - User-friendly error descriptions
   - No stack traces to users (logged instead)

## Future Enhancement Possibilities

1. **Additional Features**
   - More filters (sepia, vintage, etc.)
   - Crop functionality
   - Color adjustments (hue, saturation)
   - Batch processing

2. **Performance**
   - Threading for large images
   - Progressive display updates
   - Caching processed images

3. **UI Improvements**
   - Real-time preview
   - Before/after comparison
   - Preset filter combinations
   - Customizable shortcuts

4. **File Support**
   - Additional formats (TIFF, WebP)
   - RAW image support
   - SVG export

## Testing Recommendations

1. **Unit Testing**
   - Test ImageData methods
   - Test ImageProcessor operations
   - Test input validation

2. **Integration Testing**
   - Test class interactions
   - Test complete workflows
   - Test error scenarios

3. **UI Testing**
   - Test all buttons and menus
   - Test keyboard shortcuts
   - Test file dialogs

4. **Edge Cases**
   - Very small images
   - Very large images (near 10MB)
   - Unusual aspect ratios
   - Corrupted files
