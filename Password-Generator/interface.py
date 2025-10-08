import tkinter as tk
from tkinter import ttk
from generator import PasswordGenerator

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.create_widgets()

    def create_widgets(self):
        # Heading label
        self.heading = ttk.Label(self.root, text = "Password Generator")
        self.heading.pack(pady=10)

        # Label for the password length section
        self.length = ttk.Label(self.root, text = "Select Length")
        self.length.pack(pady=10)

        # Slider to select password length
        self.slider_value = tk.DoubleVar(value=12)
        self.slider = ttk.Scale(self.root, from_ = 8, to = 20, orient = "horizontal", variable = self.slider_value, command=self.update_slider_label)
        self.slider.pack(pady=10)

        # Label to display the current slider value
        self.slider_label = ttk.Label(self.root, text=f"Length: {int(self.slider_value.get())}")
        self.slider_label.pack()

        # Section label for character set options
        self.includes = ttk.Label(self.root, text = "Includes")
        self.includes.pack(pady=10)

        # Checkbox: Include uppercase letters
        self.upper_bool = tk.BooleanVar()
        self.upper_check = ttk.Checkbutton(self.root, text = "uppercase", variable = self.upper_bool)
        self.upper_check.pack(pady=10)

        # Checkbox: Include lowercase letters
        self.lower_bool = tk.BooleanVar()
        self.lower_check = ttk.Checkbutton(self.root, text = "lowercase", variable = self.lower_bool)
        self.lower_check.pack(pady=10)

        # Checkbox: Include numbers
        self.num_bool = tk.BooleanVar()
        self.num_check = ttk.Checkbutton(self.root, text = "numbers", variable = self.num_bool)
        self.num_check.pack(pady=10)

        # Checkbox: Include special characters
        self.special_bool = tk.BooleanVar()
        self.special_check = ttk.Checkbutton(self.root, text = "special", variable = self.special_bool)
        self.special_check.pack(pady=10)

        # Button to generate the password
        self.button = ttk.Button(self.root, text="Generate Password", command = self.on_submit)
        self.button.pack(pady=10)

        # Label to show "Password saved" message
        self.output_label = ttk.Label(self.root, text="")
        self.output_label.pack(pady=5)

        # Label to show error message in red
        self.error_label = ttk.Label(self.root, text="", foreground="red")
        self.error_label.pack(pady=5)

    def update_slider_label(self, value):
        """Update the slider label to reflect the current selected length"""
        self.slider_label.config(text=f"Length: {int(float(value))}")   

    def on_submit(self):
        """Callback when 'Generate Password' button is pressed"""
        self.error_label.config(text="")

        length = int(self.slider_value.get()) 
        set_upper = self.upper_bool.get()
        set_lower = self.lower_bool.get()
        set_num = self.num_bool.get()
        set_special = self.special_bool.get()
        
        try:
            generator = PasswordGenerator(length, set_upper, set_lower, set_num, set_special)
            password = generator.generate_password()
            self.output_label.config(text=f"Password saved")
        except ValueError as e:
            self.output_label.config(text="")
            self.error_label.config(text=str(e))

    def run(self):
        """Start the GUI event loop"""
        self.root.mainloop()

if __name__ == "__main__":
    app = Interface()
    app.run()