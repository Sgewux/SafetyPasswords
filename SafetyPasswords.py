#imports
from tkinter import *
from tkinter import messagebox
import random
#letters
letters = [
	 "a",
	 "b",
	 "c",
	 "d",
	 "e",
	 "f",
	 "g",
	 "h",
	 "i",
	 "j",
	 "k",
	 "l",
	 "m",
	 "n",
	 "o",
	 "p",
	 "q",
	 "r",
	 "s",
	 "t",
	 "u",
	 "v",
	 "w",
	 "x",
	 "y",
	 "z"
]
#symbols
symbols = [
	 "#",
	 "!",
	 "$",
	 "%",
	 "&",
     "?"
]
#numbers
numbers = [
	 "0",
	 "1",
	 "2",
	 "3",
	 "4",
	 "5",
	 "6",
	 "7",
	 "8",
	 "9"

]
#functions
def generate():

	x = []	
	for i in range(4):

		if i % 2 == 0:
			x.append(random.choice(symbols))
			x.append(random.choice(numbers))
			x.append(random.choice(letters).upper())

		else:
			x.append(random.choice(symbols))
			x.append(random.choice(numbers))
			x.append(random.choice(letters))
	random.shuffle(x)

	return ''.join(x)



def password(lenght):
	global password_label
	
	if lenght < 8:
		question = messagebox.askyesno("Small Password", f"Your password lenght it's very short, we suggest to set a longer than 8 password\n Are you sure to use a {lenght} characters password?")
		if question == 1:
			contra = generate()
			password_label = Entry(root, borderwidth=0, width= 50, bg="#f1f1f1")
			password_label.insert(0, f"Your password is: {contra[:lenght]}")
			password_label.grid(column=1, row=2)
		else:
			messagebox.showinfo("Info", "Ok, lets try again")
	elif lenght >= 8:
		contra = generate()
		password_label = Entry(root, borderwidth=0, width= 50,   bg="#f1f1f1")
		password_label.insert(0, f"Your password is: {contra[:lenght]}")
		password_label.grid(column=1, row=2)
	#except:
	#	messagebox.showerror("Error","Something happened, please try again")

#graphics
root = Tk()
root.title("SafetyPasswords")
root.geometry("800x500")

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



