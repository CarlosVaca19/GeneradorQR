import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox

def generar_qr():
    url = entrada_url.get()
    if not url.strip():
        messagebox.showerror("Error", "Por favor, ingrese una URL válida.")
        return
    
    try:
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        archivo = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if archivo:
            img.save(archivo)
            messagebox.showinfo("Éxito", f"Código QR guardado en:\n{archivo}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Código QR")
ventana.geometry("400x200")
ventana.resizable(False, False)

# Etiqueta y campo de entrada
tk.Label(ventana, text="Ingrese la URL:", font=("Arial", 12)).pack(pady=10)
entrada_url = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada_url.pack(pady=5)

# Botón para generar el QR
boton_generar = tk.Button(ventana, text="Generar Código QR", font=("Arial", 12), command=generar_qr)
boton_generar.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
