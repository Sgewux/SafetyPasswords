#imports
from tkinter import *
from tkinter import messagebox
from random import randint
#letters
letters = {
	1: "a",
	2: "b",
	3: "c",
	4: "d",
	5: "e",
	6: "f",
	7: "g",
	8: "h",
	9: "i",
	10: "j",
	11: "k",
	12: "l",
	13: "m",
	14: "n",
	15: "o",
	16: "p",
	17: "q",
	18: "r",
	19: "s",
	20: "t",
	21: "u",
	22: "v",
	23: "w",
	24: "x",
	25: "y",
	26: "z"
}
#symbols
symbols = {
	1: "#",
	2: "!",
	3: "$",
	4: "%",
	5: "&",
	6: "?"
}
#numbers
numbers = {
	0: "0",
	1: "1",
	2: "2",
	3: "3",
	4: "4",
	5: "5",
	6: "6",
	7: "7",
	8: "8",
	9: "9"

}
#functions
def randomL():
	random_leter = randint(1, 26)
	return random_leter


def randomS():
	random_symbol = randint(1, 6)
	return random_symbol


def randomN():
	random_number = randint(0, 9)
	return random_number


def password(len):
	global password_label
	
	if len < 8:
		question = messagebox.askyesno("Small Password", f"Your password lenght it's very short, we suggest to set a longer than 8 password\n Are you sure to use a {len} characters password?")
		if question == 1:
			contra = letters[randomL()] + symbols[randomS()] + letters[randomL()].upper() + numbers[randomN()] + symbols[randomS()] + letters[randomL()].upper() + numbers[randomN()] +letters[randomL()] + symbols[randomS()] + letters[randomL()].upper() + numbers[randomN()] +  symbols[randomS()]
			password_label = Entry(root, borderwidth=0, width= 50, bg="#f1f1f1")
			password_label.insert(0, f"Your password is: {contra[0:len]}")
			password_label.grid(column=1, row=2)
		else:
			messagebox.showinfo("Info", "Ok, lets try again")
	elif len >= 8:
		contra = letters[randomL()] + symbols[randomS()] + letters[randomL()].upper() + numbers[randomN()] + symbols[randomS()] + letters[randomL()].upper() + numbers[randomN()] +letters[randomL()] + symbols[randomS()] + letters[randomL()].upper() + numbers[randomN()] +  symbols[randomS()]
		password_label = Entry(root, borderwidth=0, width= 50,   bg="#f1f1f1")
		password_label.insert(0, f"Your password is: {contra[0:len]}")
		password_label.grid(column=1, row=2)
	#except:
	#	messagebox.showerror("Error","Something happened, please try again")

#graphics
root = Tk()
root.title("SafetyPasswords")
root.geometry("800x500")
#root.iconbitmap("C:/Users/SEBAS/Desktop/Python/SafetyPasswords/icon.ico")
class Window():
	"""Gui's window class"""
	def __init__(self, root):
		self.root = root
		self.label1 = Label(self.root, text="Generate a unhackeable password (ok, not at all :D)", font=('Helvetica', 14), fg="blue")
		self.label1.grid(column=0, row=0)
		self.label2 = Label(self.root, text="Set the password lenght: ", font=('Helvetica', 10))
		self.label2.grid(column=0, row=1)
		self.user_len = Scale(self.root, from_= 1, to = 12, orient=HORIZONTAL)
		self.user_len.grid(column=1, row=1)
		self.mainbutton = Button(self.root, text="Generate password" , command= lambda: password(self.user_len.get()))
		self.mainbutton.grid(column=0, row=2)
		self.password_label = Entry(self.root, borderwidth=0, width= 50,   bg="#f1f1f1")
		self.password_label.grid(column=1, row=2)
		

if __name__ == '__main__':
	Window(root)

root.mainloop()



