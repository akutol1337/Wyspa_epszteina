import tkinter as tk
from tkinter import filedialog, messagebox

def caesar_cipher(text: str, key: int) -> str:
    if key == 0:
        return text
    encrypted_chars = []
    for char in text:
        if char == ' ':
            encrypted_chars.append(char)
        elif 'a' <= char <= 'z':
            ascii_offset = ord('a')
            current_pos = ord(char) - ascii_offset
            new_pos = (current_pos + key) % 26
            encrypted_chars.append(chr(new_pos + ascii_offset))
        else:
            encrypted_chars.append(char)
    return "".join(encrypted_chars)

class CaesarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Szyfrowanie. Wykonane przez 00000000000")
        self.root.geometry("750x450")
        self.root.configure(bg="#5F9EA0") 
        self.root.resizable(False, False)

        self.lbl_key = tk.Label(root, text="Podaj wartość klucza", bg="#5F9EA0", fg="#FAEBD7", font=("Arial", 12, "bold"))
        self.lbl_key.place(x=20, y=20)

        self.entry_key = tk.Entry(root, font=("Arial", 12), width=10)
        self.entry_key.place(x=20, y=50)

        self.lbl_text = tk.Label(root, text="Podaj tekst", bg="#5F9EA0", fg="#FAEBD7", font=("Arial", 12, "bold"))
        self.lbl_text.place(x=20, y=100)

        self.txt_input = tk.Text(root, font=("Arial", 11), width=40, height=12, wrap=tk.WORD)
        self.txt_input.place(x=20, y=130)

        self.btn_cipher = tk.Button(root, text="Zaszyfruj", bg="#ADD8E6", font=("Arial", 10, "bold"), command=self.handle_cipher)
        self.btn_cipher.place(x=380, y=210, width=80, height=35)

        self.lbl_result = tk.Label(root, text="Tekst zaszyfrowany", bg="#5F9EA0", fg="#FAEBD7", font=("Arial", 12, "bold"))
        self.lbl_result.place(x=480, y=20)

        self.result_frame = tk.Frame(root, bg="#5F9EA0", highlightbackground="#FAEBD7", highlightthickness=2, bd=0)
        self.result_frame.place(x=480, y=50, width=240, height=290)

        self.txt_output = tk.Text(self.result_frame, bg="#5F9EA0", fg="#F0F8FF", font=("Arial", 11, "bold"), 
                                  wrap=tk.WORD, bd=0, highlightthickness=0)
        self.txt_output.place(x=10, y=10, width=220, height=270)
        self.txt_output.config(state=tk.DISABLED) 

        self.btn_save = tk.Button(root, text="Zapisz szyfr w pliku", bg="#ADD8E6", font=("Arial", 10, "bold"), command=self.handle_save)
        self.btn_save.place(x=480, y=360, width=240, height=35)

    def handle_cipher(self):
        raw_key = self.entry_key.get().strip()
        try:
            key = int(raw_key)
        except ValueError:
            key = 0
            self.entry_key.delete(0, tk.END)
            self.entry_key.insert(0, "0")

        text_to_cipher = self.txt_input.get("1.0", tk.END).strip("\n")

        encrypted_text = caesar_cipher(text_to_cipher, key)

        self.txt_output.config(state=tk.NORMAL)
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert("1.0", encrypted_text)
        self.txt_output.config(state=tk.DISABLED)

    def handle_save(self):
        text_to_save = self.txt_output.get("1.0", tk.END).strip("\n")
        
        if not text_to_save:
            messagebox.showwarning("Ostrzeżenie", "Brak tekstu do zapisania! Najpierw wykonaj szyfrowanie.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")],
            title="Zapisz szyfr jako..."
        )

        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text_to_save)
                messagebox.showinfo("Sukces", "Plik został zapisany pomyślnie.")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarApp(root)
    root.mainloop()