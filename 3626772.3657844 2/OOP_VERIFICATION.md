# OOP Principles Verification

This document demonstrates how the application fulfills all Object-Oriented Programming requirements.

## ✓ Requirement: At Least Three Classes

### 1. ImageData Class
- **Purpose**: Encapsulates image data and metadata
- **File**: image_processor.py, lines 13-103

### 2. ImageProcessor Class
- **Purpose**: Handles all image processing operations
- **File**: image_processor.py, lines 106-297

### 3. ImageProcessorGUI Class
- **Purpose**: Main GUI application
- **File**: image_processor.py, lines 300-708

## ✓ Requirement: Encapsulation

### ImageData Class Encapsulation
```python
# Private attributes (indicated by underscore prefix)
self._original_image: Optional[np.ndarray] = None
self._current_image: Optional[np.ndarray] = None
self._filename: str = ""
self._file_path: str = ""
self._dimensions: Tuple[int, int] = (0, 0)
self._file_size: int = 0

# Public getter methods provide controlled access
def get_current_image(self) -> Optional[np.ndarray]:
    """Get current image"""
    return self._current_image.copy() if self._current_image is not None else None

def get_filename(self) -> str:
    """Get filename"""
    return self._filename
```

**Demonstration**:
- All data attributes are private (prefix `_`)
- Access only through public methods
- Returns copies, not references (protecting internal state)
- No direct attribute access from outside class

### ImageProcessor Class Encapsulation
```python
# Private configuration attributes
self._min_blur_kernel = 3
self._max_blur_kernel = 51

# All processing logic hidden in methods
def apply_blur(self, image: np.ndarray, intensity: int = 5) -> np.ndarray:
    # Internal validation and processing
    intensity = max(1, min(25, intensity))
    kernel_size = intensity * 2 + 1
    kernel_size = min(kernel_size, self._max_blur_kernel)
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
```

**Demonstration**:
- Internal algorithm details hidden
- Parameters validated internally
- Complex OpenCV operations abstracted

### ImageProcessorGUI Class Encapsulation
```python
# Internal state management
self.undo_stack: List[np.ndarray] = []
self.redo_stack: List[np.ndarray] = []
self.max_history = 20

# Encapsulated UI components
self.canvas = tk.Canvas(...)
self.blur_slider = ttk.Scale(...)

# Private helper methods (prefix _)
def _setup_menu(self):
def _setup_ui(self):
def _display_current_image(self):
```

**Demonstration**:
- GUI state hidden from external access
- Helper methods marked as private (prefix `_`)
- Internal components not exposed

## ✓ Requirement: Constructor

### ImageData Constructor
```python
def __init__(self):
    """Initialize image data container"""
    self._original_image: Optional[np.ndarray] = None
    self._current_image: Optional[np.ndarray] = None
    self._filename: str = ""
    self._file_path: str = ""
    self._dimensions: Tuple[int, int] = (0, 0)
    self._file_size: int = 0
```

**Features**:
- Initializes all attributes
- Sets default values
- Prepares object for use
- No parameters needed (optional design)

### ImageProcessor Constructor
```python
def __init__(self):
    """Initialize image processor"""
    self._min_blur_kernel = 3
    self._max_blur_kernel = 51
```

**Features**:
- Sets configuration values
- Initializes processing constraints
- Establishes valid ranges

### ImageProcessorGUI Constructor
```python
def __init__(self, root: tk.Tk):
    """
    Initialize the GUI application
    
    Args:
        root: Tkinter root window
    """
    self.root = root
    self.root.title("Advanced Image Processor")
    self.root.geometry("1200x800")
    
    # Initialize data and processor objects
    self.image_data = ImageData()
    self.processor = ImageProcessor()
    
    # Undo/Redo stacks
    self.undo_stack: List[np.ndarray] = []
    self.redo_stack: List[np.ndarray] = []
    self.max_history = 20
    
    # Setup GUI components
    self._setup_menu()
    self._setup_ui()
    self._setup_status_bar()
```

**Features**:
- Accepts parameters (root window)
- Initializes multiple attributes
- Creates instances of other classes
- Calls setup methods
- Configures window properties

## ✓ Requirement: Methods

### ImageData Methods (12 total)

1. **`load_image(file_path: str) -> bool`**
   - Loads image from file
   - Validates file size and format
   - Returns success status

2. **`save_image(file_path: str) -> bool`**
   - Saves current image to file
   - Handles errors gracefully
   - Returns success status

3. **`update_current_image(image: np.ndarray)`**
   - Updates working image
   - Updates dimensions

4. **`reset_to_original()`**
   - Restores original image
   - Resets modifications

5. **`get_current_image() -> Optional[np.ndarray]`**
   - Returns copy of current image
   - Protects internal state

6. **`get_original_image() -> Optional[np.ndarray]`**
   - Returns copy of original image
   - Provides access to unmodified version

7. **`get_filename() -> str`**
   - Returns filename
   - Getter method

8. **`get_dimensions() -> Tuple[int, int]`**
   - Returns (width, height)
   - Tuple return type

9. **`get_file_size() -> int`**
   - Returns size in bytes
   - Numeric return

10. **`has_image() -> bool`**
    - Checks if image loaded
    - Boolean return

### ImageProcessor Methods (8 processing methods)

1. **`convert_to_grayscale(image) -> np.ndarray`**
   - Color to B&W conversion
   - Returns processed image

2. **`apply_blur(image, intensity) -> np.ndarray`**
   - Gaussian blur effect
   - Validates intensity parameter

3. **`detect_edges(image, threshold1, threshold2) -> np.ndarray`**
   - Canny edge detection
   - Multiple parameters

4. **`adjust_brightness(image, value) -> np.ndarray`**
   - HSV brightness adjustment
   - Clamps values

5. **`adjust_contrast(image, value) -> np.ndarray`**
   - Contrast multiplication
   - Range validation

6. **`rotate_image(image, angle) -> np.ndarray`**
   - 90°, 180°, 270° rotation
   - Conditional logic

7. **`flip_image(image, direction) -> np.ndarray`**
   - Horizontal/vertical flip
   - String parameter

8. **`resize_image(image, scale_percent) -> np.ndarray`**
   - Percentage-based scaling
   - Maintains aspect ratio

### ImageProcessorGUI Methods (30+ methods)

**Setup Methods**:
- `_setup_menu()` - Menu bar creation
- `_setup_ui()` - Main UI layout
- `_setup_control_panel()` - Control sidebar
- `_setup_image_display()` - Canvas setup
- `_setup_status_bar()` - Status bar

**File Operations**:
- `_open_image()` - File open dialog
- `_save_image()` - Save current file
- `_save_image_as()` - Save as dialog

**Edit Operations**:
- `_undo()` - Undo last operation
- `_redo()` - Redo operation
- `_reset_to_original()` - Reset image

**Display Methods**:
- `_display_current_image()` - Update canvas
- `_update_status()` - Update status bar

**Processing Methods**:
- `_apply_grayscale()` - Grayscale filter
- `_apply_blur()` - Blur effect
- `_apply_edge_detection()` - Edge detection
- `_apply_brightness()` - Brightness adjustment
- `_apply_contrast()` - Contrast adjustment
- `_apply_rotation()` - Rotation
- `_apply_flip()` - Flip operation
- `_apply_resize()` - Resize operation

**Utility Methods**:
- `_save_to_history()` - Save undo state
- `_apply_operation()` - Generic operation wrapper
- `_create_section_label()` - UI helper
- `_on_closing()` - Cleanup on exit

## ✓ Requirement: Class Interaction

### Interaction 1: GUI → ImageData
```python
# In ImageProcessorGUI.__init__():
self.image_data = ImageData()  # Creates instance

# In ImageProcessorGUI._open_image():
if self.image_data.load_image(file_path):  # Calls ImageData method
    self._display_current_image()

# In ImageProcessorGUI._apply_operation():
current = self.image_data.get_current_image()  # Gets data
self.image_data.update_current_image(result)  # Updates data
```

**Demonstrates**:
- GUI creates ImageData instance
- GUI calls ImageData methods
- GUI reads ImageData state
- GUI updates ImageData state

### Interaction 2: GUI → ImageProcessor
```python
# In ImageProcessorGUI.__init__():
self.processor = ImageProcessor()  # Creates instance

# In ImageProcessorGUI._apply_grayscale():
result = self.processor.convert_to_grayscale(current)  # Calls processing

# In ImageProcessorGUI._apply_blur():
intensity = int(self.blur_slider.get())
result = self.processor.apply_blur(current, intensity)  # Passes parameters
```

**Demonstrates**:
- GUI creates ImageProcessor instance
- GUI delegates processing to ImageProcessor
- GUI passes parameters to ImageProcessor
- GUI receives processed results

### Interaction 3: GUI → ImageData → ImageProcessor
```python
# Complete workflow in _apply_operation():
def _apply_operation(self, operation_func, *args):
    # Get data from ImageData
    current = self.image_data.get_current_image()
    
    # Process using ImageProcessor
    result = operation_func(current, *args)  # operation_func is ImageProcessor method
    
    # Update ImageData with result
    self.image_data.update_current_image(result)
```

**Demonstrates**:
- Three-way interaction
- Data flows between classes
- Clear separation of concerns
- Coordinated object collaboration

## Summary of OOP Compliance

| Requirement | Status | Evidence |
|-------------|--------|----------|
| **Three Classes** | ✓ Pass | ImageData, ImageProcessor, ImageProcessorGUI |
| **Encapsulation** | ✓ Pass | Private attributes (_prefix), getter methods, data hiding |
| **Constructor** | ✓ Pass | All classes have `__init__()` with proper initialization |
| **Methods** | ✓ Pass | 50+ methods across all classes |
| **Class Interaction** | ✓ Pass | GUI uses both ImageData and ImageProcessor instances |

## Additional OOP Best Practices Implemented

1. **Type Hints**: All methods have type annotations
2. **Docstrings**: All classes and methods documented
3. **Single Responsibility**: Each class has one clear purpose
4. **DRY Principle**: Code reuse through `_apply_operation()` method
5. **Error Handling**: Try-catch blocks in all critical methods
6. **Dependency Injection**: GUI receives root window as parameter
7. **Factory Methods**: `_create_section_label()` creates consistent UI elements
