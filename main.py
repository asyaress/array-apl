import customtkinter as ctk
from tkinter import messagebox
import sys

class ArrayProgram:
    def __init__(self):
        # Inisialisasi array
        self.array = []
        
        # Setup window
        self.window = ctk.CTk()
        self.window.title("Program Array 1 Dimensi")
        self.window.geometry("800x600")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title = ctk.CTkLabel(
            main_frame,
            text="Program Array 1 Dimensi",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(0, 20))
        
        # Array display section
        display_frame = ctk.CTkFrame(main_frame)
        display_frame.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(
            display_frame,
            text="Isi Array:",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=(10, 5))
        
        self.array_display = ctk.CTkTextbox(
            display_frame,
            height=100,
            font=ctk.CTkFont(size=14)
        )
        self.array_display.pack(fill="x", padx=10, pady=(0, 10))
        
        # Info label
        self.info_label = ctk.CTkLabel(
            display_frame,
            text=f"Jumlah elemen: {len(self.array)}",
            font=ctk.CTkFont(size=12)
        )
        self.info_label.pack(pady=(0, 10))
        
        # Update display after all elements created
        self.update_display()
        
        # Operations section
        operations_frame = ctk.CTkFrame(main_frame)
        operations_frame.pack(fill="both", expand=True)
        
        # Left column - Add/Delete
        left_col = ctk.CTkFrame(operations_frame)
        left_col.pack(side="left", fill="both", expand=True, padx=(10, 5), pady=10)
        
        # Add element
        ctk.CTkLabel(
            left_col,
            text="Tambah Elemen",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(5, 10))
        
        self.add_entry = ctk.CTkEntry(
            left_col,
            placeholder_text="Masukkan nilai..."
        )
        self.add_entry.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(
            left_col,
            text="Tambah di Akhir",
            command=self.add_element,
            fg_color="#2ecc71",
            hover_color="#27ae60"
        ).pack(fill="x", padx=10, pady=5)
        
        # Delete element
        ctk.CTkLabel(
            left_col,
            text="Hapus Elemen",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(20, 10))
        
        self.delete_entry = ctk.CTkEntry(
            left_col,
            placeholder_text="Masukkan indeks..."
        )
        self.delete_entry.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(
            left_col,
            text="Hapus Berdasarkan Indeks",
            command=self.delete_by_index,
            fg_color="#e74c3c",
            hover_color="#c0392b"
        ).pack(fill="x", padx=10, pady=5)
        
        # Right column - Update/Search
        right_col = ctk.CTkFrame(operations_frame)
        right_col.pack(side="right", fill="both", expand=True, padx=(5, 10), pady=10)
        
        # Update element
        ctk.CTkLabel(
            right_col,
            text="Update Elemen",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(5, 10))
        
        self.update_index_entry = ctk.CTkEntry(
            right_col,
            placeholder_text="Indeks..."
        )
        self.update_index_entry.pack(fill="x", padx=10, pady=5)
        
        self.update_value_entry = ctk.CTkEntry(
            right_col,
            placeholder_text="Nilai baru..."
        )
        self.update_value_entry.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(
            right_col,
            text="Update Elemen",
            command=self.update_element,
            fg_color="#f39c12",
            hover_color="#e67e22"
        ).pack(fill="x", padx=10, pady=5)
        
        # Search element
        ctk.CTkLabel(
            right_col,
            text="Cari Elemen",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(20, 10))
        
        self.search_entry = ctk.CTkEntry(
            right_col,
            placeholder_text="Cari nilai..."
        )
        self.search_entry.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(
            right_col,
            text="Cari Elemen",
            command=self.search_element,
            fg_color="#9b59b6",
            hover_color="#8e44ad"
        ).pack(fill="x", padx=10, pady=5)
        
        # Bottom buttons
        bottom_frame = ctk.CTkFrame(main_frame)
        bottom_frame.pack(fill="x", pady=(20, 0))
        
        ctk.CTkButton(
            bottom_frame,
            text="Kosongkan Array",
            command=self.clear_array,
            fg_color="#95a5a6",
            hover_color="#7f8c8d"
        ).pack(side="left", padx=5, pady=10)
        
        ctk.CTkButton(
            bottom_frame,
            text="Isi Array Contoh",
            command=self.fill_sample,
            fg_color="#3498db",
            hover_color="#2980b9"
        ).pack(side="left", padx=5, pady=10)
        
    def update_display(self):
        """Update tampilan array"""
        self.array_display.delete("1.0", "end")
        
        if not self.array:
            self.array_display.insert("1.0", "Array kosong")
        else:
            # Display dengan indeks
            display_text = "Indeks | Nilai\n"
            display_text += "-" * 30 + "\n"
            for i, value in enumerate(self.array):
                display_text += f"  [{i}]  |  {value}\n"
            
            self.array_display.insert("1.0", display_text)
        
        self.info_label.configure(text=f"Jumlah elemen: {len(self.array)}")
        
    def add_element(self):
        """Tambah elemen ke array"""
        value = self.add_entry.get().strip()
        
        if not value:
            messagebox.showwarning("Peringatan", "Masukkan nilai terlebih dahulu!")
            return
        
        try:
            # Coba convert ke number jika memungkinkan
            if '.' in value:
                value = float(value)
            else:
                try:
                    value = int(value)
                except ValueError:
                    pass  # Keep as string
            
            self.array.append(value)
            self.update_display()
            self.add_entry.delete(0, "end")
            messagebox.showinfo("Sukses", f"Elemen '{value}' berhasil ditambahkan!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menambahkan elemen: {str(e)}")
    
    def delete_by_index(self):
        """Hapus elemen berdasarkan indeks"""
        index_str = self.delete_entry.get().strip()
        
        if not index_str:
            messagebox.showwarning("Peringatan", "Masukkan indeks terlebih dahulu!")
            return
        
        try:
            index = int(index_str)
            
            if not self.array:
                messagebox.showwarning("Peringatan", "Array masih kosong!")
                return
            
            if index < 0 or index >= len(self.array):
                messagebox.showerror("Error", f"Indeks tidak valid! Gunakan 0-{len(self.array)-1}")
                return
            
            deleted_value = self.array.pop(index)
            self.update_display()
            self.delete_entry.delete(0, "end")
            messagebox.showinfo("Sukses", f"Elemen '{deleted_value}' di indeks {index} berhasil dihapus!")
            
        except ValueError:
            messagebox.showerror("Error", "Indeks harus berupa angka!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menghapus elemen: {str(e)}")
    
    def update_element(self):
        """Update elemen di indeks tertentu"""
        index_str = self.update_index_entry.get().strip()
        new_value = self.update_value_entry.get().strip()
        
        if not index_str or not new_value:
            messagebox.showwarning("Peringatan", "Masukkan indeks dan nilai baru!")
            return
        
        try:
            index = int(index_str)
            
            if not self.array:
                messagebox.showwarning("Peringatan", "Array masih kosong!")
                return
            
            if index < 0 or index >= len(self.array):
                messagebox.showerror("Error", f"Indeks tidak valid! Gunakan 0-{len(self.array)-1}")
                return
            
            # Coba convert ke number jika memungkinkan
            if '.' in new_value:
                new_value = float(new_value)
            else:
                try:
                    new_value = int(new_value)
                except ValueError:
                    pass  # Keep as string
            
            old_value = self.array[index]
            self.array[index] = new_value
            self.update_display()
            self.update_index_entry.delete(0, "end")
            self.update_value_entry.delete(0, "end")
            messagebox.showinfo("Sukses", f"Elemen di indeks {index} berhasil diubah dari '{old_value}' menjadi '{new_value}'!")
            
        except ValueError:
            messagebox.showerror("Error", "Indeks harus berupa angka!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengupdate elemen: {str(e)}")
    
    def search_element(self):
        """Cari elemen dalam array"""
        search_value = self.search_entry.get().strip()
        
        if not search_value:
            messagebox.showwarning("Peringatan", "Masukkan nilai yang ingin dicari!")
            return
        
        if not self.array:
            messagebox.showwarning("Peringatan", "Array masih kosong!")
            return
        
        # Coba convert ke number untuk pencarian
        try:
            if '.' in search_value:
                search_value = float(search_value)
            else:
                try:
                    search_value = int(search_value)
                except ValueError:
                    pass
        except:
            pass
        
        indices = [i for i, val in enumerate(self.array) if str(val) == str(search_value)]
        
        if indices:
            result = f"Elemen '{search_value}' ditemukan di indeks: {', '.join(map(str, indices))}\n"
            result += f"Total: {len(indices)} kemunculan"
            messagebox.showinfo("Hasil Pencarian", result)
        else:
            messagebox.showinfo("Hasil Pencarian", f"Elemen '{search_value}' tidak ditemukan dalam array!")
    
    def clear_array(self):
        """Kosongkan array"""
        if not self.array:
            messagebox.showinfo("Info", "Array sudah kosong!")
            return
        
        if messagebox.askyesno("Konfirmasi", "Yakin ingin mengosongkan array?"):
            self.array.clear()
            self.update_display()
            messagebox.showinfo("Sukses", "Array berhasil dikosongkan!")
    
    def fill_sample(self):
        """Isi array dengan data contoh"""
        if self.array:
            if not messagebox.askyesno("Konfirmasi", "Array sudah berisi data. Yakin ingin mengisi dengan data contoh?"):
                return
        
        self.array = [10, 25, 30, 45, 50, 15, 20, 35, 40, 55]
        self.update_display()
        messagebox.showinfo("Sukses", "Array berhasil diisi dengan data contoh!")
    
    def run(self):
        """Jalankan aplikasi"""
        self.window.mainloop()

if __name__ == "__main__":
    try:
        app = ArrayProgram()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)