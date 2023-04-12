from tkinter import *
import requests
import json
def airinfo():
    try:
        api_request= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode_entry.get()+"&distance=25&API_KEY=F6BC1C54-908B-4435-B30F-ACFAB5AFB1C4")
        print("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode_entry.get()+"&distance=25&API_KEY=F6BC1C54-908B-4435-B30F-ACFAB5AFB1C4")
        api=json.loads(api_request.content)
        city= api[0]['ReportingArea']
        quality = api[0]['StateCode']
        category = api[0]['Category']["Name"]
        status_label = Label(root, text="City:"+city+"("+quality+") ->"+category)
        status_label.grid(row=2, columnspan=2)
    except Exception as e:
        api="Error..."
def main():
    global root
    global zipcode_entry
    root=Tk()
    root.title("Aplikacja Pogodowa")
    root.geometry("300x80")

    # Elements
    zipcode_label=Label(root, text="Podaj kod pocztowy")
    zipcode_btn = Button(root, text="ID", width=34, command=airinfo)
    zipcode_entry = Entry(root)

    # Position
    zipcode_label.grid(row=0, column=0)
    zipcode_entry.grid(row=0, column=1)
    zipcode_btn.grid(row=1, columnspan=2)

    root.mainloop()
if __name__ == '__main__':
    main()