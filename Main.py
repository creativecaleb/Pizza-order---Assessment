import tkinter as tk
from tkinter.simpledialog import askinteger, askstring
from tkinter import *

customer_name=''
delivery=False
delivery_address=''
pizza_type=[]
total_cost=0
cheap_pizza=['Margherita', 'Marinara', 'Prosciutto', 'Hawaiian',
              'Popeye','Pepperoni', 'Meat Lovers']
premium_pizza=[ 'Godfather', 'Parmigiana', 'M.O.B.']
root=tk.Tk() #Root widget
root.geometry('520x300')
root.title('Pizza Order')
root.iconbitmap('assets/images/pizza_icon.ico')


def order():
    tk


frame=Frame(root)
frame.pack()

bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)

top_text=Label(frame, text="Pizza Order Program", 
               font=("Open Sans", 25))
top_text.pack(side=TOP, pady=30)

quit_button=Button(bottom_frame, text='Quit', font=("Open Sans", 15),
                     command=root.destroy)
quit_button.pack(side=RIGHT, pady=30, padx=30)
quit_button.config( height=2, width=10 )

order_button=tk.Button(bottom_frame, text='New order', 
                       font=("Open Sans", 15), command=order)
order_button.config( height=2, width=10 )
order_button.pack(side=LEFT, pady=30, padx=30)

root.mainloop()


