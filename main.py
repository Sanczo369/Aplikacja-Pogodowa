from tkinter import *
import json
def main():
    root=Tk()
    root.title("Aplikacja Pogodowa")
    root.geometry("300x80")

    # Elements
    zipcode_label=Label(root, text="Podaj kod pocztowy")
    zipcode_btn = Button(root, text="ID", width=34)
    zipcode_entry = Entry(root)
    status_label=Label(root,text="test")

    # Position
    zipcode_label.grid(row=0, column=0)
    zipcode_entry.grid(row=0, column=1)
    zipcode_btn.grid(row=1, columnspan=2)
    status_label.grid(row=2, columnspan=2)

    root.mainloop()
if __name__ == '__main__':
    main()