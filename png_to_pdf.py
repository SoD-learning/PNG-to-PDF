import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class PngToPdfConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PNG to PDF Converter")
        self.root.geometry("500x600")

        # Title label
        self.app_name_label = tk.Label(root, text="PNG to PDF Converter", font=("Arial", 30))
        self.app_name_label.pack(pady=30)

        # Instructions label title
        self.instructions_label = tk.Label(root, text="Instructions", font=("Arial", 14))
        self.instructions_label.pack(anchor='w', pady=10, padx=30)

        # Instructions label 1
        self.instructions_label1 = tk.Label(root, text="1. Click the 'Select PNG' button and choose your .png image.", font=("Arial", 10))
        self.instructions_label1.pack(anchor='w', padx=30)

        # Instructions label 2
        self.instructions_label2 = tk.Label(root, text="2. Click the 'Convert to PDF' button under the thumbnail.", font=("Arial", 10))
        self.instructions_label2.pack(anchor='w', padx=30)

        # Instructions label 3
        self.instructions_label3 = tk.Label(root, text="3. Save the PDF file in your desired location.", font=("Arial", 10))
        self.instructions_label3.pack(anchor='w', padx=30)

        # Select PNG button
        self.select_button = tk.Button(root, padx=20, text="Select PNG", command=self.select_png)
        self.select_button.pack(pady=20)

        # Label for selected PNG
        self.selected_png_label = tk.Label(root, text="No PNG selected", font=("Arial", 10))
        self.selected_png_label.pack(pady=5)

        # Canvas for image preview
        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()

        # Convert to PDF button
        self.convert_button = tk.Button(root, padx=20, text="Convert to PDF", command=self.convert_to_pdf)
        # self.convert_button.pack(pady=10)

        # Status label
        self.status_label = tk.Label(root, text="", font=("Arial", 10))
        self.status_label.pack()

        # Variable to store the selected PNG file path
        self.selected_png = None

    def select_png(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if file_path:
            self.selected_png = file_path
            self.selected_png_label.config(text=os.path.basename(file_path))
            self.preview_image(file_path)
            # Show the convert button after a file is selected
            self.convert_button.pack()
            

    def convert_to_pdf(self):
        if self.selected_png:
            try:
                image = Image.open(self.selected_png)
                pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                if pdf_path:
                    image.convert('RGB').save(pdf_path)
                    self.status_label.config(text="Conversion successful!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showinfo("Info", "Please select a PNG file first")

    def preview_image(self, file_path):
        # Open the image, resize it to fit the canvas, and create an ImageTk.PhotoImage object
        image = Image.open(file_path)
        image.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(image)

        # Add the image to the canvas
        self.canvas.create_image(100, 100, image=photo)
        self.canvas.image = photo  # Keep a reference to avoid garbage collection

# Create the main window and run the application
root = tk.Tk()
app = PngToPdfConverterApp(root)
root.mainloop()
