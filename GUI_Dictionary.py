import tkinter as tk
import tkinter.messagebox
from difflib import get_close_matches
import sys



import json
data = json.load(open("dictionary_data.json"))    # This statement create a python dictionary which contains dictionary data


def yes_func(key):
    count = 1
    for widget in frame2.winfo_children():
        widget.destroy()

    tk.Label(frame2, text = "Here are some definitions : ").grid(row=0, padx=15, pady=15,sticky=tk.W)
    for item in data[key]:
        var_meaning = item
        meaning = tk.Label(frame2, textvariable=var_meaning, text = var_meaning, borderwidth=3)
        meaning.grid(row=count, padx=5, pady=5,sticky=tk.W)
        # var_meaning.set(item)
        count += 1


def no_func():
    for widget in frame2.winfo_children():
        widget.destroy()

    tk.Label(frame2, text = "Sorry, This word is not in our database. We will Fix this after some time.").grid(row=0, padx=15, pady=15,sticky=tk.W)
    tk.Label(frame2, text = "OR You can double check it whether you have entered the correct word or not?").grid(row=1, padx=15, pady=15,sticky=tk.W)


def translate():
    count=1
    key=var_entry.get().lower()

    for widget in frame2.winfo_children():
        widget.destroy()

    if key in data or key.title() in data or key.upper() in data:
        if key.title() in data:
            key = key.title()

        if key.upper() in data:
            key = key.upper()

        tk.Label(frame2, text = "Here are some definitions : ").grid(row=0, padx=15, pady=15,sticky=tk.W)
        for item in data[key]:
            var_meaning = item
            meaning = tk.Label(frame2, textvariable=var_meaning, text = var_meaning, borderwidth=3)
            meaning.grid(row=count, padx=5, pady=5,sticky=tk.W)
            # var_meaning.set(item)
            count += 1

    elif len(get_close_matches(key, data.keys())) > 0:
        key = get_close_matches(key, data.keys())[0]
        choice = "Did you mean %s instead?" % key

        tk.Label(frame2, text = choice).grid(row=0, padx=15, pady=15,sticky=tk.W)

        yes = tk.Button(frame2, text = "Yes", command = lambda : yes_func(key), bg = "silver",
                                fg = "black", font = ("Arial Bold", 8), borderwidth=3,
                                relief=tk.RAISED
                                )
        yes.grid(row = 0, column = 1, padx=15, pady=15)


        no = tk.Button(frame2, text = "No", command = no_func, bg = "silver",
                                fg = "black", font = ("Arial Bold", 8), borderwidth=3,
                                relief=tk.RAISED
                                )
        no.grid(row = 0, column = 2, padx=15, pady=15)

    else:
        tk.Label(frame2, text = "Sorry, This word is not in our database. We will Fix this after some time.").grid(row=0, padx=15, pady=15,sticky=tk.W)
        tk.Label(frame2, text = "OR You can double check it whether you have entered the correct word or not?").grid(row=1, padx=15, pady=15,sticky=tk.W)





# This method runs when you click on EXIT
def custom_quit():
    answer = tk.messagebox.askokcancel("Are yor sure?",     # This method shows a messagebox of ok or cancel
    "Are you sure you want to EXIT this Dictionary?"
    )
    if(answer):
        # quit()
        sys.exit()


root = tk.Tk()     # creating a GUI window



frame = tk.Frame(root, relief=tk.RIDGE, borderwidth=20, bg="gray")
frame.pack(fill=tk.BOTH, expand=1)

root.minsize(width=700, height=500)
root.geometry("900x700")


root.title("Dictionary")
heading = tk.Label(frame, text = "Dictionary", bg = "blue", bd=3, fg = "black", font = ("Arial Bold", 25))
# heading.config(highlightbackground="black")
heading.pack()



frame1 = tk.Frame(frame, relief=tk.SOLID, borderwidth=2, bg="gray")
frame1.pack(fill=tk.BOTH, expand=1)



label = tk.Label(frame1, text = "Enter a Word : ", borderwidth=3)
label.grid(row=0, column=0, padx=15, pady=15)



var_entry = tk.StringVar()
word = tk.Entry(frame1, textvariable=var_entry, borderwidth=3, width=50)
word.focus_set()
word.grid(row=0, column=1, padx=15, pady=15)



submit = tk.Button(frame1, text = "Click here to get meaning", command = translate, bg = "silver",
                        fg = "black", font = ("Arial Bold", 8), borderwidth=3,
                        relief=tk.RAISED
                        )
submit.grid(row = 2, column = 0, padx=15, pady=15)


frame2 = tk.Frame(frame1, relief=tk.SOLID, borderwidth=2, bg="gray")
frame2.grid(columnspan=4, sticky = tk.W)


# var_meaning = tk.StringVar()
# meaning = tk.Label(frame2, textvariable=var_meaning, text = var_meaning, borderwidth=3)
# meaning.grid(row=0, column=0, padx=15, pady=15)



exit1 = tk.Button(frame, text = "Exit", command = custom_quit, bg = "silver",
                        fg = "black", font = ("Arial Bold", 8), borderwidth=3,
                        relief=tk.RAISED
                        )
exit1.pack(anchor=tk.E, side=tk.BOTTOM, padx=5, pady=5, fill=tk.BOTH)
#
# reset = tk.Button(frame, text = "One More Word", command = custom_quit, bg = "silver",
#                         fg = "black", font = ("Arial Bold", 8), borderwidth=3,
#                         relief=tk.RAISED
#                         )
# reset.pack(anchor=tk.E, side=tk.BOTTOM, padx=5, pady=5, fill=tk.BOTH)

root.mainloop()
