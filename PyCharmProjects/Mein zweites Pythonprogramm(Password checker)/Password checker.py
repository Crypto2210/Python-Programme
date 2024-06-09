import tkinter as tk

root = tk.Tk()
e = tk.StringVar()
root.geometry("300x190")
root.title("Password checker")


def if_():
    label = tk.Label(root, text="", textvariable=e, font=("Arial", 9))
    label.pack(side="top")
    if password.get() == input2.get():
        e.set("Das Passwort wurde erfolgreich abgespeichert!")

    if password.get() != input2.get():
        e.set("Das Passwort wurde nicht erfolgreich abgespeichert!")


bitte_passwort_eingeben = tk.Label(root, text="Bitte passowort eingenben!:", font=("Arial", 12))
bitte_passwort_eingeben.pack(side="top", fill="x")
password = tk.Entry(root)
password.pack(side="top", fill="x", padx=1, pady=2)
bitte_passwort_eingeben2 = tk.Label(root, text="Bitte passowort zweites mal eingeben!:", font=("Arial", 12))
bitte_passwort_eingeben2.pack(side="top", fill="x")
input2 = tk.Entry(root)
input2.pack(side="top", fill="x", padx=1, pady=2)

enter = tk.Button(root, text="Abschicken", command=if_)
enter.pack(fill="x", pady=10)

quit = tk.Button(root, text="Programm beenden", command=root.destroy)
quit.pack(side="bottom", pady=5)

root.mainloop()
