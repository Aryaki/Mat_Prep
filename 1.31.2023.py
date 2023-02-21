import tkinter

canvas = tkinter.Canvas(width=600, height=100, bg='black')
canvas.pack()


def animation(): # "While true" can be used instead of the function
    global slogan
    slogan = slogan[1:] + slogan[0]
    canvas.delete("all")
    canvas.create_text(300, 50, text=6 * ' ' + slogan + 6 * ' ', fill='yellow', font=('Jokerman', '30', 'bold'))
    canvas.after(100, animation)


slogan = ''
slogan = " "*4 + slogan + " " * (40 - len(slogan))
animation()

canvas.mainloop()
