from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.size = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = Label(self, text='Python Pizza calculator', font='arial 16')
        self.lbl_title.grid(row=0, column=0, columnspan=3 ,  sticky = W, pady = 2)

        self.lbl_title = Label(self, text='Select Size:', font='arial 12')
        self.lbl_title.grid(row=1, column=0,  sticky = W, pady = 2)

        self.lbl_title = Label(self, text='Select Toppings:', font='arial 12')
        self.lbl_title.grid(row=3, column=0,  sticky = W, pady = 2)
        self.rad_medium = Radiobutton(self, text='Medium', font='arial 12', variable=self.size, value="Medium")
        self.rad_medium.grid(row=2, column=0)
        self.rad_large = Radiobutton(self, text='Large', font='arial 12', variable=self.size, value="Large")
        self.rad_large.grid(row=2, column=1)
        self.rad_xlarge = Radiobutton(self, text='Extra Large', font='arial 12', variable=self.size, value="xlarge")
        self.rad_xlarge.grid(row=2, column=2)
        self.rad_medium.select()
        fred = Button(self, fg='red', bg='blue')



if __name__ == "__main__":
    window = Tk()
    window.title('Test Application Window')
    window.geometry("500x500")
    app = Application(window)
    app.mainloop()