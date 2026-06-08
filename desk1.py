import tkinter as tk

class RGBColorSampler:
    def __init__(self, root):
        self.root = root

        self.root.title("Wzornik kolorów RGB. Wykonał 00000000000")
        self.root.configure(bg="#FFF8DC")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        self.current_color_view = tk.Frame(self.root, bg="#FFFFFF", height=100, bd=1, relief="solid")
        self.current_color_view.pack(fill="x", padx=20, pady=15)

        self.info_label = tk.Label(
            self.root, 
            text="Dobierz kolor suwakami i zapisz przyciskiem:", 
            bg="#FFF8DC", 
            font=("Arial", 10)
        )
        self.info_label.pack(anchor="w", padx=20, pady=5)
        
        self.sliders_frame = tk.Frame(self.root, bg="#FFF8DC")
        self.sliders_frame.pack(fill="x", padx=20, pady=5)
        
        self.r_val = tk.IntVar(value=255)
        self.g_val = tk.IntVar(value=255)
        self.b_val = tk.IntVar(value=255)
        
        tk.Label(self.sliders_frame, text="R", bg="#FFF8DC", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
        self.slider_r = tk.Scale(self.sliders_frame, from_=0, to=255, orient="horizontal", variable=self.r_val, showvalue=False, command=self.update_live_color, bg="#FFF8DC", highlightthickness=0)
        self.slider_r.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.lbl_r_num = tk.Label(self.sliders_frame, text="255", bg="#FFF8DC", width=4, anchor="e")
        self.lbl_r_num.grid(row=0, column=2, padx=5, pady=5)
        
        tk.Label(self.sliders_frame, text="G", bg="#FFF8DC", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
        self.slider_g = tk.Scale(self.sliders_frame, from_=0, to=255, orient="horizontal", variable=self.g_val, showvalue=False, command=self.update_live_color, bg="#FFF8DC", highlightthickness=0)
        self.slider_g.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.lbl_g_num = tk.Label(self.sliders_frame, text="255", bg="#FFF8DC", width=4, anchor="e")
        self.lbl_g_num.grid(row=1, column=2, padx=5, pady=5)
        
        tk.Label(self.sliders_frame, text="B", bg="#FFF8DC", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=5)
        self.slider_b = tk.Scale(self.sliders_frame, from_=0, to=255, orient="horizontal", variable=self.b_val, showvalue=False, command=self.update_live_color, bg="#FFF8DC", highlightthickness=0)
        self.slider_b.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.lbl_b_num = tk.Label(self.sliders_frame, text="255", bg="#FFF8DC", width=4, anchor="e")
        self.lbl_b_num.grid(row=2, column=2, padx=5, pady=5)
        
        self.sliders_frame.grid_columnconfigure(1, weight=1)

        self.btn_save = tk.Button(
            self.root, 
            text="Pobierz", 
            bg="#CD853F", 
            fg="black", 
            font=("Arial", 10), 
            command=self.save_sampled_color
        )
        self.btn_save.pack(pady=15)

        self.saved_color_label = tk.Label(
            self.root, 
            text="255, 255, 255", 
            bg="#FFFFFF", 
            fg="black", 
            font=("Arial", 11), 
            height=2, 
            width=25, 
            bd=1, 
            relief="solid"
        )
        self.saved_color_label.pack(pady=5)

    def update_live_color(self, *args):
        r = self.r_val.get()
        g = self.g_val.get()
        b = self.b_val.get()
        
        self.lbl_r_num.config(text=str(r))
        self.lbl_g_num.config(text=str(g))
        self.lbl_b_num.config(text=str(b))
        
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        self.current_color_view.config(bg=hex_color)

    def save_sampled_color(self):
        r = self.r_val.get()
        g = self.g_val.get()
        b = self.b_val.get()
        
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        
        text_color = "white" if (r*0.299 + g*0.587 + b*0.114) < 128 else "black"
        
        self.saved_color_label.config(
            text=f"{r}, {g}, {b}", 
            bg=hex_color,
            fg=text_color
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = RGBColorSampler(root)
    root.mainloop()