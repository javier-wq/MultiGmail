import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from itertools import combinations
import pyperclip

class EmailVariationGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Variation Generator")
        self.root.geometry("600x500")
        
        # Main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input from the original email
        ttk.Label(main_frame, text="Enter your email address:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(main_frame, textvariable=self.email_var, width=40)
        self.email_entry.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Button to generate variations
        ttk.Button(main_frame, text="Generate Variations", command=self.generate_variations).grid(row=2, column=0, sticky=tk.W, pady=10)
        
        # List of results
        ttk.Label(main_frame, text="Variations generated:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.result_text = tk.Text(main_frame, width=50, height=15)
        self.result_text.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Scrollbar for the list of results
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=4, column=1, sticky=(tk.N, tk.S))
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        # Button to copy all results
        ttk.Button(main_frame, text="Copy All", command=self.copy_all).grid(row=5, column=0, sticky=tk.W, pady=10)

    def generate_variations(self):
        email = self.email_var.get()
        if not '@' in email:
            messagebox.showerror("Error", "Please enter a valid email address.")
            return
            
        local_part, domain = email.split('@')
        positions = range(1, len(local_part))
        variations = []
        
        # Generate all possible combinations of positions for the points
        for r in range(1, len(positions) + 1):
            for combo in combinations(positions, r):
                new_local = list(local_part)
                # Insert points at selected positions
                for pos in reversed(combo):
                    new_local.insert(pos, '.')
                variations.append(''.join(new_local) + '@' + domain)
        
        # Show results
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Original email: " + email + "\n\n")
        for i, var in enumerate(variations, 1):
            self.result_text.insert(tk.END, f"{i}. {var}\n")
            
        messagebox.showinfo("Success", f"{len(variations)} variations were generated.")

    def copy_all(self):
        content = self.result_text.get(1.0, tk.END)
        pyperclip.copy(content)
        messagebox.showinfo("Copied", "All variations have been copied to the clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailVariationGenerator(root)
    root.mainloop()