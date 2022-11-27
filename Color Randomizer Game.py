from tkinter import *
import random

root = Tk()
root.title("Encapsulation")
root.geometry("400x300")
root.config(bg = "white")

lbl_color = Label(root, font = ("Comic Sans MS", 20, "bold"), bg = "white")
lbl_color.place(relx = 0.5, rely = 0.4, anchor = CENTER)

class Score():
    
    def __init__(self):
        self.__score = 0
        
    def updateScore(self):
        self.text = ["BLUE", "GREEN", "ORANGE", "PINK", "RED", "YELLOW", "PURPLE", "BROWN", "GREY", "BLACK"]
        self.random_no_text = random.randint(0, 9)
        
        self.color = ["blue", "green", "orange", "pink", "red", "yellow", "purple", "brown", "grey", "black"]
        self.random_no_color = random.randint(0, 9)
        
        lbl_color["text"] = self.text[self.random_no_text]
        lbl_color["fg"] = self.color[self.random_no_color]

obj = Score()
        
btn = Button(root, text = "Start", command = obj.updateScore, relief = FLAT, bg = "dark olive green", fg = "white", padx = 10, pady = 1, font = ("Arial", 15))
btn.place(relx = 0.6, rely = 0.8, anchor = CENTER)

root.mainloop()