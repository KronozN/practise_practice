"""
Advanced Image Processing Application
Demonstrates OOP, Tkinter GUI, and OpenCV Image Processing
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk
import os
from typing import Optional, List, Tuple


class ImageData:
    """
    Encapsulates image data and metadata.
    Demonstrates: Encapsulation, Constructor, Methods
    """
    
    def __init__(self):
        """Initialize image data container"""
        self._original_image: Optional[np.ndarray] = None
        self._current_image: Optional[np.ndarray] = None
        self._filename: str = ""
        self._file_path: str = ""
        self._dimensions: Tuple[int, int] = (0, 0)
        self._file_size: int = 0
        
    def load_image(self, file_path: str) -> bool:
        """
        Load an image from file path with validation
        
        Args:
            file_path: Path to the image file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Validate file exists
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            # Check file size (max 10MB)
            file_size = os.path.getsize(file_path)
            if file_size > 10 * 1024 * 1024:
                raise ValueError("File size exceeds 10MB limit")
            
            # Load image
            image = cv2.imread(file_path)
            if image is None:
                raise ValueError("Unable to read image file")
            
            # Store image data
            self._original_image = image.copy()
            self._current_image = image.copy()
            self._filename = os.path.basename(file_path)
            self._file_path = file_path
            self._dimensions = (image.shape[1], image.shape[0])  # (width, height)
            self._file_size = file_size
            
            return True
            
        except Exception as e:
            print(f"Error loading image: {e}")
            return False
    
    def save_image(self, file_path: str) -> bool:
        """
        Save current image to file
        
        Args:
            file_path: Path where image should be saved
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if self._current_image is None:
                raise ValueError("No image to save")
            
            success = cv2.imwrite(file_path, self._current_image)
            if not success:
                raise IOError("Failed to save image")
            
            return True
            
        except Exception as e:
            print(f"Error saving image: {e}")
            return False
    
    def update_current_image(self, image: np.ndarray):
        """Update the current working image"""
        if image is not None:
            self._current_image = image.copy()
            self._dimensions = (image.shape[1], image.shape[0])
    
    def reset_to_original(self):
        """Reset current image to original"""
        if self._original_image is not None:
            self._current_image = self._original_image.copy()
    
    # Getter methods (Encapsulation)
    def get_current_image(self) -> Optional[np.ndarray]:
        """Get current image"""
        return self._current_image.copy() if self._current_image is not None else None
    
    def get_original_image(self) -> Optional[np.ndarray]:
        """Get original image"""
        return self._original_image.copy() if self._original_image is not None else None
    
    def get_filename(self) -> str:
        """Get filename"""
        return self._filename
    
    def get_dimensions(self) -> Tuple[int, int]:
        """Get image dimensions (width, height)"""
        return self._dimensions
    
    def get_file_size(self) -> int:
        """Get file size in bytes"""
        return self._file_size
    
    def has_image(self) -> bool:
        """Check if image is loaded"""
        return self._current_image is not None


class ImageProcessor:
    """
    Handles all image processing operations using OpenCV.
    Demonstrates: Encapsulation, Methods, Class Interaction
    """
    
    def __init__(self):
        """Initialize image processor"""
        self._min_blur_kernel = 3
        self._max_blur_kernel = 51
    
    def convert_to_grayscale(self, image: np.ndarray) -> np.ndarray:
        """
        Convert image to grayscale
        
        Args:
            image: Input image (BGR format)
            
        Returns:
            Grayscale image (BGR format for consistency)
        """
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Convert back to BGR for consistent display
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            print(f"Error in grayscale conversion: {e}")
            return image
    
    def apply_blur(self, image: np.ndarray, intensity: int = 5) -> np.ndarray:
        """
        Apply Gaussian blur
        
        Args:
            image: Input image
            intensity: Blur intensity (1-25, will be converted to odd kernel size)
            
        Returns:
            Blurred image
        """
        try:
            # Validate intensity
            intensity = max(1, min(25, intensity))
            # Convert to odd kernel size
            kernel_size = intensity * 2 + 1
            kernel_size = min(kernel_size, self._max_blur_kernel)
            
            return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        except Exception as e:
            print(f"Error applying blur: {e}")
            return image
    
    def detect_edges(self, image: np.ndarray, threshold1: int = 100, 
                     threshold2: int = 200) -> np.ndarray:
        """
        Apply Canny edge detection
        
        Args:
            image: Input image
            threshold1: First threshold for hysteresis
            threshold2: Second threshold for hysteresis
            
        Returns:
            Edge-detected image
        """
        try:
            # Convert to grayscale first
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, threshold1, threshold2)
            # Convert back to BGR
            return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            print(f"Error in edge detection: {e}")
            return image
    
    def adjust_brightness(self, image: np.ndarray, value: int) -> np.ndarray:
        """
        Adjust image brightness
        
        Args:
            image: Input image
            value: Brightness adjustment (-100 to 100)
            
        Returns:
            Brightness-adjusted image
        """
        try:
            value = max(-100, min(100, value))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv)
            
            # Adjust V channel
            v = np.clip(v.astype(np.int16) + value, 0, 255).astype(np.uint8)
            
            final_hsv = cv2.merge([h, s, v])
            return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        except Exception as e:
            print(f"Error adjusting brightness: {e}")
            return image
    
    def adjust_contrast(self, image: np.ndarray, value: float) -> np.ndarray:
        """
        Adjust image contrast
        
        Args:
            image: Input image
            value: Contrast factor (0.5 to 3.0)
            
        Returns:
            Contrast-adjusted image
        """
        try:
            value = max(0.5, min(3.0, value))
            # Apply contrast adjustment
            adjusted = cv2.convertScaleAbs(image, alpha=value, beta=0)
            return adjusted
        except Exception as e:
            print(f"Error adjusting contrast: {e}")
            return image
    
    def rotate_image(self, image: np.ndarray, angle: int) -> np.ndarray:
        """
        Rotate image by specified angle
        
        Args:
            image: Input image
            angle: Rotation angle (90, 180, or 270)
            
        Returns:
            Rotated image
        """
        try:
            if angle == 90:
                return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            elif angle == 180:
                return cv2.rotate(image, cv2.ROTATE_180)
            elif angle == 270:
                return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            else:
                return image
        except Exception as e:
            print(f"Error rotating image: {e}")
            return image
    
    def flip_image(self, image: np.ndarray, direction: str) -> np.ndarray:
        """
        Flip image horizontally or vertically
        
        Args:
            image: Input image
            direction: 'horizontal' or 'vertical'
            
        Returns:
            Flipped image
        """
        try:
            if direction == 'horizontal':
                return cv2.flip(image, 1)
            elif direction == 'vertical':
                return cv2.flip(image, 0)
            else:
                return image
        except Exception as e:
            print(f"Error flipping image: {e}")
            return image
    
    def resize_image(self, image: np.ndarray, scale_percent: int) -> np.ndarray:
        """
        Resize image by percentage
        
        Args:
            image: Input image
            scale_percent: Scale percentage (10 to 200)
            
        Returns:
            Resized image
        """
        try:
            scale_percent = max(10, min(200, scale_percent))
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            
            if width < 1 or height < 1:
                return image
            
            return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        except Exception as e:
            print(f"Error resizing image: {e}")
            return image


class ImageProcessorGUI:
    """
    Main GUI application class.
    Demonstrates: Class Interaction, Encapsulation, Methods
    """
    
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
        
        # Current display image
        self.display_image = None
        
        # Setup GUI components
        self._setup_menu()
        self._setup_ui()
        self._setup_status_bar()
        
        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _setup_menu(self):
        """Setup menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self._open_image, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self._save_image, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self._save_image_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._on_closing, accelerator="Ctrl+Q")
        
        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self._undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self._redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Reset to Original", command=self._reset_to_original)
        
        # Keyboard shortcuts
        self.root.bind('<Control-o>', lambda e: self._open_image())
        self.root.bind('<Control-s>', lambda e: self._save_image())
        self.root.bind('<Control-Shift-S>', lambda e: self._save_image_as())
        self.root.bind('<Control-q>', lambda e: self._on_closing())
        self.root.bind('<Control-z>', lambda e: self._undo())
        self.root.bind('<Control-y>', lambda e: self._redo())
    
    def _setup_ui(self):
        """Setup main UI components"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Controls
        self._setup_control_panel(main_frame)
        
        # Right panel - Image display
        self._setup_image_display(main_frame)
    
    def _setup_control_panel(self, parent):
        """Setup control panel with buttons and sliders"""
        control_frame = ttk.Frame(parent, width=300)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))
        control_frame.pack_propagate(False)
        
        # Title
        title_label = ttk.Label(control_frame, text="Image Processing Tools", 
                               font=('Arial', 12, 'bold'))
        title_label.pack(pady=10)
        
        # Scrollable frame for controls
        canvas = tk.Canvas(control_frame, bg='#f0f0f0')
        scrollbar = ttk.Scrollbar(control_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Basic Filters Section
        self._create_section_label(scrollable_frame, "Basic Filters")
        
        ttk.Button(scrollable_frame, text="Grayscale", 
                  command=self._apply_grayscale).pack(fill=tk.X, padx=10, pady=2)
        
        ttk.Button(scrollable_frame, text="Edge Detection", 
                  command=self._apply_edge_detection).pack(fill=tk.X, padx=10, pady=2)
        
        # Blur Section with Slider
        self._create_section_label(scrollable_frame, "Blur Effect")
        
        blur_frame = ttk.Frame(scrollable_frame)
        blur_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(blur_frame, text="Intensity:").pack()
        self.blur_slider = ttk.Scale(blur_frame, from_=1, to=25, orient=tk.HORIZONTAL)
        self.blur_slider.set(5)
        self.blur_slider.pack(fill=tk.X)
        
        ttk.Button(blur_frame, text="Apply Blur", 
                  command=self._apply_blur).pack(fill=tk.X, pady=2)
        
        # Brightness Section with Slider
        self._create_section_label(scrollable_frame, "Brightness")
        
        brightness_frame = ttk.Frame(scrollable_frame)
        brightness_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(brightness_frame, text="Adjustment (-100 to 100):").pack()
        self.brightness_slider = ttk.Scale(brightness_frame, from_=-100, to=100, 
                                          orient=tk.HORIZONTAL)
        self.brightness_slider.set(0)
        self.brightness_slider.pack(fill=tk.X)
        
        ttk.Button(brightness_frame, text="Apply Brightness", 
                  command=self._apply_brightness).pack(fill=tk.X, pady=2)
        
        # Contrast Section with Slider
        self._create_section_label(scrollable_frame, "Contrast")
        
        contrast_frame = ttk.Frame(scrollable_frame)
        contrast_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(contrast_frame, text="Factor (0.5 to 3.0):").pack()
        self.contrast_slider = ttk.Scale(contrast_frame, from_=0.5, to=3.0, 
                                        orient=tk.HORIZONTAL)
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack(fill=tk.X)
        
        ttk.Button(contrast_frame, text="Apply Contrast", 
                  command=self._apply_contrast).pack(fill=tk.X, pady=2)
        
        # Rotation Section
        self._create_section_label(scrollable_frame, "Rotation")
        
        rotation_frame = ttk.Frame(scrollable_frame)
        rotation_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(rotation_frame, text="Rotate 90°", 
                  command=lambda: self._apply_rotation(90)).pack(fill=tk.X, pady=2)
        ttk.Button(rotation_frame, text="Rotate 180°", 
                  command=lambda: self._apply_rotation(180)).pack(fill=tk.X, pady=2)
        ttk.Button(rotation_frame, text="Rotate 270°", 
                  command=lambda: self._apply_rotation(270)).pack(fill=tk.X, pady=2)
        
        # Flip Section
        self._create_section_label(scrollable_frame, "Flip")
        
        flip_frame = ttk.Frame(scrollable_frame)
        flip_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(flip_frame, text="Flip Horizontal", 
                  command=lambda: self._apply_flip('horizontal')).pack(fill=tk.X, pady=2)
        ttk.Button(flip_frame, text="Flip Vertical", 
                  command=lambda: self._apply_flip('vertical')).pack(fill=tk.X, pady=2)
        
        # Resize Section with Slider
        self._create_section_label(scrollable_frame, "Resize")
        
        resize_frame = ttk.Frame(scrollable_frame)
        resize_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(resize_frame, text="Scale (10% to 200%):").pack()
        self.resize_slider = ttk.Scale(resize_frame, from_=10, to=200, 
                                      orient=tk.HORIZONTAL)
        self.resize_slider.set(100)
        self.resize_slider.pack(fill=tk.X)
        
        ttk.Button(resize_frame, text="Apply Resize", 
                  command=self._apply_resize).pack(fill=tk.X, pady=2)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _create_section_label(self, parent, text):
        """Create a section label"""
        label = ttk.Label(parent, text=text, font=('Arial', 10, 'bold'))
        label.pack(pady=(15, 5), padx=10, anchor='w')
        ttk.Separator(parent, orient='horizontal').pack(fill='x', padx=10)
    
    def _setup_image_display(self, parent):
        """Setup image display area"""
        display_frame = ttk.Frame(parent)
        display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Canvas for image
        self.canvas = tk.Canvas(display_frame, bg='#2b2b2b', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Placeholder text
        self.canvas.create_text(
            400, 300,
            text="No Image Loaded\n\nClick File > Open to load an image",
            font=('Arial', 16),
            fill='#ffffff',
            tags='placeholder'
        )
    
    def _setup_status_bar(self):
        """Setup status bar"""
        self.status_bar = ttk.Label(self.root, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def _update_status(self, message: str = ""):
        """Update status bar"""
        if not message and self.image_data.has_image():
            filename = self.image_data.get_filename()
            width, height = self.image_data.get_dimensions()
            size_kb = self.image_data.get_file_size() / 1024
            message = f"File: {filename} | Size: {width}x{height} | {size_kb:.1f} KB"
        elif not message:
            message = "Ready"
        
        self.status_bar.config(text=message)
    
    def _save_to_history(self):
        """Save current image state to undo history"""
        if self.image_data.has_image():
            current = self.image_data.get_current_image()
            if current is not None:
                self.undo_stack.append(current)
                # Limit history size
                if len(self.undo_stack) > self.max_history:
                    self.undo_stack.pop(0)
                # Clear redo stack when new operation is performed
                self.redo_stack.clear()
    
    def _undo(self):
        """Undo last operation"""
        if not self.image_data.has_image():
            messagebox.showwarning("Warning", "No image loaded")
            return
        
        if not self.undo_stack:
            messagebox.showinfo("Info", "Nothing to undo")
            return
        
        # Save current state to redo stack
        current = self.image_data.get_current_image()
        self.redo_stack.append(current)
        
        # Restore previous state
        previous = self.undo_stack.pop()
        self.image_data.update_current_image(previous)
        self._display_current_image()
        self._update_status()
    
    def _redo(self):
        """Redo last undone operation"""
        if not self.image_data.has_image():
            messagebox.showwarning("Warning", "No image loaded")
            return
        
        if not self.redo_stack:
            messagebox.showinfo("Info", "Nothing to redo")
            return
        
        # Save current state to undo stack
        current = self.image_data.get_current_image()
        self.undo_stack.append(current)
        
        # Restore redone state
        redone = self.redo_stack.pop()
        self.image_data.update_current_image(redone)
        self._display_current_image()
        self._update_status()
    
    def _reset_to_original(self):
        """Reset image to original state"""
        if not self.image_data.has_image():
            messagebox.showwarning("Warning", "No image loaded")
            return
        
        if messagebox.askyesno("Confirm Reset", "Reset image to original? This cannot be undone."):
            self._save_to_history()
            self.image_data.reset_to_original()
            self._display_current_image()
            self._update_status()
    
    def _open_image(self):
        """Open image file"""
        file_path = filedialog.askopenfilename(
            title="Open Image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("PNG files", "*.png"),
                ("BMP files", "*.bmp"),
                ("All files", "*.*")
            ]
        )
        
        if not file_path:
            return
        
        try:
            if self.image_data.load_image(file_path):
                # Clear history
                self.undo_stack.clear()
                self.redo_stack.clear()
                
                # Display image
                self._display_current_image()
                self._update_status()
                messagebox.showinfo("Success", "Image loaded successfully!")
            else:
                messagebox.showerror("Error", "Failed to load image. Please check the file format and size (max 10MB).")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the image:\n{str(e)}")
    
    def _save_image(self):
        """Save image to current file"""
        if not self.image_data.has_image():
            messagebox.showwarning("Warning", "No image to save")
            return
        
        # If no original file path, use Save As
        if not self.image_data._file_path:
            self._save_image_as()
            return
        
        try:
            if self.image_data.save_image(self.image_data._file_path):
                messagebox.showinfo("Success", "Image saved successfully!")
            else:
                messagebox.showerror("Error", "Failed to save image")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving:\n{str(e)}")
    
    def _save_image_as(self):
        """Save image as new file"""
        if not self.image_data.has_image():
            messagebox.showwarning("Warning", "No image to save")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save Image As",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("BMP files", "*.bmp"),
                ("All files", "*.*")
            ]
        )
        
        if not file_path:
            return
        
        try:
            if self.image_data.save_image(file_path):
                messagebox.showinfo("Success", "Image saved successfully!")
            else:
                messagebox.showerror("Error", "Failed to save image")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving:\n{str(e)}")
    
    def _display_current_image(self):
        """Display current image on canvas"""
        if not self.image_data.has_image():
            return
        
        try:
            # Get current image
            image = self.image_data.get_current_image()
            if image is None:
                return
            
            # Convert BGR to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Get canvas size
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            # Calculate scaling to fit canvas
            img_height, img_width = image_rgb.shape[:2]
            
            scale_w = canvas_width / img_width
            scale_h = canvas_height / img_height
            scale = min(scale_w, scale_h, 1.0)  # Don't upscale
            
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            
            # Resize for display
            if scale < 1.0:
                display_img = cv2.resize(image_rgb, (new_width, new_height), 
                                        interpolation=cv2.INTER_AREA)
            else:
                display_img = image_rgb
            
            # Convert to PhotoImage
            pil_image = Image.fromarray(display_img)
            self.display_image = ImageTk.PhotoImage(pil_image)
            
            # Clear canvas and display image
            self.canvas.delete('all')
            
            x = (canvas_width - new_width) // 2
            y = (canvas_height - new_height) // 2
            
            self.canvas.create_image(x, y, anchor=tk.NW, image=self.display_image)
            
        except Exception as e:
            print(f"Error displaying image: {e}")
            messagebox.showerror("Error", f"Failed to display image:\n{str(e)}")
    
    def _apply_operation(self, operation_func, *args):
        """Generic method to apply an operation and update display"""
        if not self.image_data.has_image():
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            # Save current state to history
            self._save_to_history()
            
            # Get current image
            current = self.image_data.get_current_image()
            
            # Apply operation
            result = operation_func(current, *args)
            
            # Update image
            self.image_data.update_current_image(result)
            
            # Display result
            self._display_current_image()
            self._update_status()
            
        except Exception as e:
            messagebox.showerror("Error", f"Operation failed:\n{str(e)}")
    
    def _apply_grayscale(self):
        """Apply grayscale filter"""
        self._apply_operation(self.processor.convert_to_grayscale)
    
    def _apply_blur(self):
        """Apply blur effect"""
        intensity = int(self.blur_slider.get())
        self._apply_operation(self.processor.apply_blur, intensity)
    
    def _apply_edge_detection(self):
        """Apply edge detection"""
        self._apply_operation(self.processor.detect_edges)
    
    def _apply_brightness(self):
        """Apply brightness adjustment"""
        value = int(self.brightness_slider.get())
        self._apply_operation(self.processor.adjust_brightness, value)
    
    def _apply_contrast(self):
        """Apply contrast adjustment"""
        value = float(self.contrast_slider.get())
        self._apply_operation(self.processor.adjust_contrast, value)
    
    def _apply_rotation(self, angle: int):
        """Apply rotation"""
        self._apply_operation(self.processor.rotate_image, angle)
    
    def _apply_flip(self, direction: str):
        """Apply flip"""
        self._apply_operation(self.processor.flip_image, direction)
    
    def _apply_resize(self):
        """Apply resize"""
        scale = int(self.resize_slider.get())
        self._apply_operation(self.processor.resize_image, scale)
    
    def _on_closing(self):
        """Handle window close event"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()


def main():
    """Main entry point"""
    try:
        root = tk.Tk()
        app = ImageProcessorGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Fatal error: {e}")
        messagebox.showerror("Fatal Error", f"Application failed to start:\n{str(e)}")


if __name__ == "__main__":
    main()
