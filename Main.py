import tkinter as tk
from tkinter.simpledialog import askinteger, askstring
from tkinter import *

customer_name=''
delivery=False
delivery_address=''
pizza_type=[]
total_cost=0
cheap_pizza=['Margherita', 'Marinara', 'Prosciutto', 'Hawaiian',
              'Popeye','Pepperoni', 'Meat Lovers', 'None']
premium_pizza=[ 'Godfather', 'Parmigiana', 'M.O.B.']
root=tk.Tk() #Root widget
root.geometry('520x300')
root.title('Pizza Order')
root.iconbitmap(default='assets/images/pizza_icon.ico')


def order():
    def take_address():
        global delivery_address
        delivery_address=address_input.get(1.0, 'end-1c')
        address.destroy()
        pizza_order()

    global customer_name
    customer_name=askstring('Name input', 'Customer name\t\t\t\t\t')
    
    address=tk.Tk() #Root addressess widget
    address.geometry('520x300')
    address.title('Delivery details')
    address.iconbitmap('assets/images/delivery_icon.ico')
    window=tk.Frame(address)
    window.pack()

    topText=Label(window, text='Delivery address:',
                    font=('Open Sans', 25))
    topText.pack(side=TOP, pady=10)

    address_input=tk.Text(window, height=1, width=25)
    address_input.pack(side=TOP, pady=10)

    bottomaddressFrame=Frame(address)
    bottomaddressFrame.pack(side=BOTTOM)

    enter_button=tk.Button(bottomaddressFrame, text='Enter',
                           font=('Open Sans', 15), command=take_address)
    enter_button.pack(side=TOP, pady=10, padx=30)
    enter_button.config(height=2, width=25)

    quit_button=Button(bottomaddressFrame, text='No delivery', 
                       font=('Open Sans', 15), command=address.destroy)
    quit_button.pack(side=BOTTOM, pady=10, padx=30)
    quit_button.config(height=2, width=25)


def pizza_order():
    pizza_selection=tk.Tk() #Root addressess widget
    pizza_selection.geometry('520x300')
    pizza_selection.title('Pizza details')
    pizza_selection.iconbitmap('assets/images/pizza_icon.ico')
    window=tk.Frame(pizza_selection)
    window.grid()
    selection=tk.StringVar()
    selection.set('None')

    p1t=Label(pizza_selection, text='Pizza 1 Type',
                    font=('Open Sans', 20))
    p1t.grid(pady=5, padx=15, row=0, column=0)

    p1s=OptionMenu(pizza_selection, selection, *cheap_pizza)
    p1s.grid(pady=5, padx=15, row=0, column=1)
    p1s.config(width=20)
    
    p2t=Label(pizza_selection, text='Pizza 2 Type',
                    font=('Open Sans', 20))
    p2t.grid(pady=5, padx=15, row=1, column=0)

    p2s=OptionMenu(pizza_selection, selection, *cheap_pizza)
    p2s.grid(pady=5, padx=15, row=1, column=1)
    p2s.config(width=20)
    
    p3t=Label(pizza_selection, text='Pizza 3 Type',
                    font=('Open Sans', 20))
    p3t.grid(pady=5, padx=15, row=2, column=0)

    p3s=OptionMenu(pizza_selection, selection, *cheap_pizza)
    p3s.grid(pady=5, padx=15, row=2, column=1)
    p3s.config(width=20)
    
    p4t=Label(pizza_selection, text='Pizza 4 Type',
                    font=('Open Sans', 20))
    p4t.grid(pady=5, padx=15, row=3, column=0)

    p4s=OptionMenu(pizza_selection, selection, *cheap_pizza)
    p4s.grid(pady=5, padx=15, row=3, column=1)
    p4s.config(width=20)
    
    p5t=Label(pizza_selection, text='Pizza 5 Type',
                    font=('Open Sans', 20))
    p5t.grid(pady=5, padx=15, row=4, column=0)

    p5s=OptionMenu(pizza_selection, selection, *cheap_pizza)
    p5s.grid(pady=5, padx=15, row=4, column=1)
    p5s.config(width=20)
    


frame=Frame(root)
frame.pack()

bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)

top_text=Label(frame, text='Pizza Order Program', 
               font=('Open Sans', 25))
top_text.pack(side=TOP, pady=30)

quit_button=Button(bottom_frame, text='Quit', font=('Open Sans', 15),
                     command=root.destroy)
quit_button.pack(side=RIGHT, pady=30, padx=30)
quit_button.config(height=2, width=10)

order_button=tk.Button(bottom_frame, text='New order', 
                       font=('Open Sans', 15), command=order)
order_button.config( height=2, width=10 )
order_button.pack(side=LEFT, pady=30, padx=30)

root.mainloop()


