import tkinter as tk
import os
from tkinter import Menu, filedialog, messagebox, Scale, HORIZONTAL
import cv2
from PIL import Image, ImageTk
import numpy as np

class ImageProcessor:
    def __init__(self, image=None):
        self.image = image  # store current image (NumPy array)
    def to_grayscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # Grayscale:contentReference[oaicite:40]{index=40}
    def blur(self, k):
        self.image = cv2.GaussianBlur(self.image, (k,k), 0)         # Gaussian blur:contentReference[oaicite:41]{index=41}
    def detect_edges(self, th1, th2):
        self.image = cv2.Canny(self.image, th1, th2)               # Canny edges:contentReference[oaicite:42]{index=42}
    def adjust_brightness_contrast(self, alpha, beta):
        # using OpenCV convertScaleAbs
        self.image = cv2.convertScaleAbs(self.image, alpha=alpha, beta=beta)  # linear transform:contentReference[oaicite:43]{index=43}
    def rotate(self, code):
        self.image = cv2.rotate(self.image, code)                  # ROTATE_90 etc:contentReference[oaicite:44]{index=44}
    def flip(self, code):
        self.image = cv2.flip(self.image, code)                    # flipCode: 0=x-axis,1=y-axis:contentReference[oaicite:45]{index=45}
    def resize(self, fx, fy):
        self.image = cv2.resize(self.image, None, fx=fx, fy=fy)    # resize:contentReference[oaicite:46]{index=46}

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Editor")
        self.processor = ImageProcessor()
        self.history = []  # undo stack
        self.redo_stack = []
        # Setup menus (File, Edit) as in:contentReference[oaicite:47]{index=47}:contentReference[oaicite:48]{index=48}
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.undo)
        editmenu.add_command(label="Redo", command=self.redo)
        menubar.add_cascade(label="Edit", menu=editmenu)
        self.root.config(menu=menubar)
        # Canvas for image display:
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()
        # Example control: brightness slider
        self.brightness_slider = Scale(self.root, from_=-100, to=100,
                                      orient=HORIZONTAL, label="Brightness",
                                      command=self.on_brightness)
        self.brightness_slider.pack()
        # (Similarly add sliders/buttons for other effects)
    def open_file(self):
        path = filedialog.askopenfilename(title="Open")
        if not path: 
            return
        if os.path.getsize(path) > 10*1024*1024:  # 10 MB limit
            messagebox.showerror("Error", "File too large")
            return
        img = cv2.imread(path)
        if img is None:
            messagebox.showerror("Error", "Could not open image")
            return
        self.processor.image = img
        self.update_image_display()
        # clear history stacks
        self.history.clear(); self.redo_stack.clear()
    def update_image_display(self):
        img = self.processor.image
        # Convert BGR->RGB for display
        if img.ndim == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)
        photo = ImageTk.PhotoImage(image=img_pil)
        self.canvas.create_image(0,0, image=photo, anchor=tk.NW)
        self.canvas.image = photo  # keep reference:contentReference[oaicite:49]{index=49}:contentReference[oaicite:50]{index=50}
    def save_file(self):
        if self.processor.image is None:
            return
        if not self.current_path:
            self.save_as()
        else:
            cv2.imwrite(self.current_path, self.processor.image)  # save:contentReference[oaicite:51]{index=51}
            messagebox.showinfo("Saved", "Image saved")
    def save_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if not path: return
        self.current_path = path
        cv2.imwrite(path, self.processor.image)
        messagebox.showinfo("Saved", "Image saved")
    def on_brightness(self, val):
        if self.processor.image is None: return
        # Record state for undo
        self.history.append(self.processor.image.copy())
        self.redo_stack.clear()
        alpha = 1.0
        beta = int(val)  # simple brightness shift
        self.processor.adjust_brightness_contrast(alpha, beta)
        self.update_image_display()
    def undo(self):
        if not self.history: return
        self.redo_stack.append(self.processor.image.copy())
        self.processor.image = self.history.pop()
        self.update_image_display()
    def redo(self):
        if not self.redo_stack: return
        self.history.append(self.processor.image.copy())
        self.processor.image = self.redo_stack.pop()
        self.update_image_display()
    # (Handlers for other effects would be similar)

app = MainApp()
app.root.mainloop()
