from tkinter import *
from tkinter import messagebox
from tkinter import filedialog #Dosyalama işlemi için gerekli kütüphane

# GUI(Grafik kullanıcı arayüzü),grafik programları oluşturmak için çeşitli modüller sunar
# (*) kullanarak kütüphaneyi tamamen içinde ki herşeyle birlikte import etmiş oluruz

#Basit XOR şifreleme fonksiyonu
def xor_encrypt_decrypt(data, key):
    # Gelen data'nın tipine göre işlem yap (str veya bytes)
    if isinstance(data, str):
        data = data.encode('utf-8')
    key = key.encode('utf-8')
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def Save_Encrypt():
    title = first_entry.get()
    secret = my_textbox.get("1.0",END).strip()
    master_key = second_entry.get()

    if not (title and secret and master_key):
        messagebox.showerror("Hata", "Tüm alanları doldurun!")
        return

    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files","*.txt")]
        )
        if not file_path:
            return

        encrypted_data = xor_encrypt_decrypt(secret, master_key)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        messagebox.showinfo("Başarılı", "Dosya şifrelenerek kaydedildi!")
    except Exception as e:
        messagebox.showerror("Hata", str(e))



def Decrypt():
    master_key = second_entry.get()
    if not master_key:
        messagebox.showerror("Hata", "Master Key girin!")
        return

    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if not file_path:# Dosya seçilmezse işlemi iptal et
            return

        with open(file_path, 'rb') as f:
            encrypted_data = f.read()# Doğrudan bytes olarak oku
        # encrypted_data zaten bytes, decode'e gerek yok
        decrypted_data = xor_encrypt_decrypt(encrypted_data, master_key).decode('utf-8')
        my_textbox.delete("1.0", END)
        my_textbox.insert("1.0", decrypted_data)
    except UnicodeDecodeError:
        messagebox.showerror("Hata", "Geçersiz Master Key!")
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmeyen Hata: {str(e)}")


window = Tk()
window.title("Secret Notes")
window.minsize(width=200, height=200)
window.config(pady=20)

scrollbar = Scrollbar(window)
scrollbar.grid()

#Image
image = PhotoImage(file="top-secret.png").subsample(6,7)  # Resmi yeniden boyutlandırdık,subsample ile boyutunu küçülttük
image_label = Label(window, image=image)
image_label.grid(row=0, column=0, pady=10)


# label 1
first_label = Label(window, text="Enter your title")  # Label sınıfından bir nesne(widget) oluşturduk
first_label.grid(row=1, column=0) #1.satır 1.sütun

# entry 1
first_entry = Entry(window, width=30)
first_entry.focus()  # Program ilk çalıştırıldığında imleç önce burada gözüksün
first_entry.grid(row=2, column=0)

# label 2
second_label = Label(window, text="Enter your secret")
second_label.grid(row=3, column=0, pady=10)

# Textbox
my_textbox = Text(window, width=30, height=15)
my_textbox.get("1.0",END)
my_textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=my_textbox.yview)
my_textbox.grid(row=4, column=0)

# label 3
third_label = Label(window, text="Enter master key")
third_label.grid(row=5, column=0, pady=10)

# entry 2
second_entry = Entry(window, width=30)
second_entry.grid(row=6, column=0)

# button 1
first_button = Button(window, text="Save & Encrypt", bg="white",command=Save_Encrypt)#buttonu doğrudan çalıştırmayıp referans verdik
first_button.grid(row=7, column=0, pady=10)

# button 2
second_button = Button(window, text="Decrypt", bg="white",command=Decrypt)
second_button.grid(row=8, column=0, pady=10)

window.mainloop()
#Pencereyi açık tutar, program kapanana kadar
