import tkinter as tk
import main
from tkinter import messagebox
  
root=tk.Tk()
root.title("Miller Indices Representer")
 
# setting the windows size
root.geometry("400x400")
 

def pos_plot():

    try:

        x=int(x_txt.get("1.0","end"))
        y=int(y_txt.get("1.0","end"))
        z=int(z_txt.get("1.0","end"))

        main.clear()
        main.cube()
    
        main.Positive_Axis()
        main.Positive_Plot(x, y ,z)
        main.my_pen.hideturtle()
    except:
        messagebox.showerror("Error", "Please provide valid input")


def neg_plot():

    try:

        x=int(x_txt.get("1.0","end"))
        y=int(y_txt.get("1.0","end"))
        z=int(z_txt.get("1.0","end"))

        main.clear()
        main.cube()
    
        main.Negative_Axis()
        main.Negative_Plot(x, y, z)
        main.my_pen.hideturtle()
    except:
        messagebox.showerror("Error", "Please provide valid input")

     
     

x_label = tk.Label(root, text = 'Provide the x intercept', padx=5, pady=5, font=('calibre',10, 'bold'))
x_txt = tk.Text(root, height=1, width=20)
  

y_label = tk.Label(root, text = 'Provide the y intercept', padx=5, pady=5, font = ('calibre',10,'bold'))
y_txt = tk.Text(root, height=1, width=20)


z_label = tk.Label(root, text = 'Provide the z intercept', padx=5, pady=5, font = ('calibre',10,'bold'))
z_txt = tk.Text(root, height=1, width=20)

  

pos_btn=tk.Button(root,text = 'Positive Plot', padx=10, pady=10, command = pos_plot)
neg_btn=tk.Button(root,text = 'Negative Plot', padx=10, pady=10, command = neg_plot)
  

x_label.grid(row=0,column=0)
x_txt.grid(row=0,column=1)
y_label.grid(row=1,column=0)
y_txt.grid(row=1,column=1)
z_label.grid(row=2,column=0)
z_txt.grid(row=2,column=1)
pos_btn.grid(row=6,column=0)
neg_btn.grid(row=6,column=1)


root.mainloop()