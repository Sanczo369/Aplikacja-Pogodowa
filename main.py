from tkinter import *
import requests
import json
def main():
    root=Tk()
    root.title("Aplikacja Pogodowa")
    root.geometry("300x80")

    # Elements
    zipcode_label=Label(root, text="Podaj kod pocztowy")
    zipcode_btn = Button(root, text="ID", width=34)
    zipcode_entry = Entry(root)

    # Position
    zipcode_label.grid(row=0, column=0)
    zipcode_entry.grid(row=0, column=1)
    zipcode_btn.grid(row=1, columnspan=2)

    try:
        api_request= requests.get("")
        api=json.loads(api_request.content)
        status_label = Label(root, text=api)
        status_label.grid(row=2, columnspan=2)
    except Exception as e:
        api="Error..."



    root.mainloop()
if __name__ == '__main__':
    main()