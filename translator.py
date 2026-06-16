from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
 text = input_text.get("1.0", END).strip()
 translated = GoogleTranslator(source='en', target='te').translate(text)
 output_text.delete("1.0", END)
 
 output_text.insert(END, translated)
def clear_text():
    input_text.delete("1.0",END)
    output_text.delete("1.0",END)

root = Tk()
root.title("Language Translation Tool")
root.geometry("700x450")
input_text = Text(root, height=5, width=50)
Label(root, text="Enter Text",font=("arial",12,"bold")).pack(pady=5)
input_text.pack()
Button(root, text="Translate", command=translate_text).pack()
Button(root,text="Clear", command=clear_text).pack(pady=5)
Label(root, text="Translated Text",font=("arial", 12,"bold")).pack(pady=5)
output_text = Text(
    root,
    height=5,
    width=50,
    font=("arial",14),
    bg="white",
    fg="green",
    bd=2,
    relief="solid"
)
output_text.pack(pady=10)

root.mainloop() 