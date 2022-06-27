from tkinter import *

window = Tk()
window.title('Miles to Km to Converter')
window.config(padx=60, pady=60)


#Label
is_equal = Label(text='is equal to', font=('Arial', 12, 'bold'))
is_equal.grid(column=0, row=1)
miles = Label(text='Miles', font=('Arial', 12, 'bold'))
miles.grid(column=2, row=0)
Km = Label(text='Km', font=('Arial', 12, 'bold'))
Km.grid(column=2, row=1)
answer = Label(text="0")
answer.grid(column=1, row=1)


#Entry
entry = Entry(width=10)
entry.insert(END, string="0")
print(entry.get())
entry.grid(column=1, row=0)


#Button
def calculate():
    value = int(entry.get()) * 1.60934
    answer.config(text=value)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()