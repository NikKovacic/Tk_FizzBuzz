from Tkinter import *
import tkMessageBox

window = Tk()

#  greeting text
greeting = Label(window, text="Welcome to the FizzBuzz game!\nPlease enter a number between 1 and 100: ")
greeting.pack()

#  entry field
num = Entry(window)
num.pack()


#  check num, kako se da omejiti na range(1, 100)
def check_num():
    if int(num.get()) % 3 == 0 and int(num.get()) % 5 == 0:
        result_text = "FizzBuzz"
    elif int(num.get()) % 3 == 0:
        result_text = "Fizz"
    elif int(num.get()) % 5 == 0:
        result_text = "Buzz"
    else:
        result_text = "Try again :)"

    tkMessageBox.showinfo("Result", result_text)


# submit button
submit = Button(window, text="Submit", command=check_num)
submit.pack()

window.mainloop()
