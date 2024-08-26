import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import *

customer_name=''
delivery=False
DELIVERY_COST='3.00'
delivery_address=''
pizza_selections=[]
total_cost=0
CHEAP_PIZZA=['Margherita', 'Marinara', 'Prosciutto', 'Hawaiian',
              'Popeye','Pepperoni', 'Meat Lovers']
PREMIUM_PIZZA=['Godfather', 'Parmigiana', 'M.O.B.']
pizza_types=[]
pizza_types.extend(CHEAP_PIZZA)
pizza_types.extend(PREMIUM_PIZZA)
pizza_types.append('None')
root=tk.Tk() #Root widget
root.geometry('520x300')
root.title('Pizza Order')
root.iconbitmap(default='assets/images/pizza_icon.ico')

# Initial order function. It takes the customer's name, checks if they want
# delivery and if they do, uses another function to take their address.
def order():
    # Local function to take the customer's address and open the next 
    # window when done
    def take_address():
        global delivery_address
        global delivery
        delivery_address=address_input.get(1.0, 'end-1c')
        if delivery_address=='':
            delivery=False
        else:
            delivery=True
        address.destroy()
        pizza_order()

    # Local function to open the next window when done
    def no_delivery():
        address.destroy()
        pizza_order()

    global customer_name
    while customer_name == '':
        customer_name=askstring('Name input', 'Customer name\t\t\t\t\t')
        if customer_name == None:
            reset(None)
            return
    
    address=tk.Tk() #Root addressess widget
    address.geometry('520x300')
    address.title('Delivery details')
    address.iconbitmap('assets/images/delivery_icon.ico')
    window=tk.Frame(address)
    window.pack()

    text=Label(window, text='Delivery address:',
                    font=('Open Sans', 25))
    text.pack(side=TOP, pady=10)

    address_input=tk.Text(window, height=1, width=25)
    address_input.pack(side=TOP, pady=10)

    bottomaddressFrame=Frame(window)
    bottomaddressFrame.pack(side=BOTTOM)

    enter_button=tk.Button(bottomaddressFrame, text='Enter',
                           font=('Open Sans', 15), command=take_address)
    enter_button.pack(side=TOP, pady=10, padx=30)
    enter_button.config(height=2, width=25)

    quit_button=Button(bottomaddressFrame, text='No delivery', 
                       font=('Open Sans', 15), command=no_delivery)
    quit_button.pack(side=BOTTOM, pady=10, padx=30)
    quit_button.config(height=2, width=25)


def pizza_order():
    # Local function to save the pizza selections and open the next
    # window when done
    def save_order():
        pizza_selections.append(selection1.get())
        pizza_selections.append(selection2.get())
        pizza_selections.append(selection3.get())
        pizza_selections.append(selection4.get())
        pizza_selections.append(selection5.get())

        pizza_selection.destroy()
        return_order()

    

    pizza_selection=tk.Tk() #Root addressess widget
    pizza_selection.geometry('520x300')
    pizza_selection.title('Pizza details')
    pizza_selection.iconbitmap('assets/images/pizza_icon.ico')
    window=tk.Frame(pizza_selection)
    window.grid()
    selection1=tk.StringVar(pizza_selection)
    selection1.set('None')
    selection2=tk.StringVar(pizza_selection)
    selection2.set('None')
    selection3=tk.StringVar(pizza_selection)
    selection3.set('None')
    selection4=tk.StringVar(pizza_selection)
    selection4.set('None')
    selection5=tk.StringVar(pizza_selection)
    selection5.set('None')

    p1t=Label(pizza_selection, text='Pizza 1 Type',
                    font=('Open Sans', 20))
    p1t.grid(pady=5, padx=15, row=0, column=0)

    p1s=OptionMenu(pizza_selection, selection1, *pizza_types)
    p1s.grid(pady=5, padx=15, row=0, column=1)
    p1s.config(width=20)
    
    p2t=Label(pizza_selection, text='Pizza 2 Type',
                    font=('Open Sans', 20))
    p2t.grid(pady=5, padx=15, row=1, column=0)

    p2s=OptionMenu(pizza_selection, selection2, *pizza_types)
    p2s.grid(pady=5, padx=15, row=1, column=1)
    p2s.config(width=20)
    
    p3t=Label(pizza_selection, text='Pizza 3 Type',
                    font=('Open Sans', 20))
    p3t.grid(pady=5, padx=15, row=2, column=0)

    p3s=OptionMenu(pizza_selection, selection3, *pizza_types)
    p3s.grid(pady=5, padx=15, row=2, column=1)
    p3s.config(width=20)
    
    p4t=Label(pizza_selection, text='Pizza 4 Type',
                    font=('Open Sans', 20))
    p4t.grid(pady=5, padx=15, row=3, column=0)

    p4s=OptionMenu(pizza_selection, selection4, *pizza_types)
    p4s.grid(pady=5, padx=15, row=3, column=1)
    p4s.config(width=20)
    
    p5t=Label(pizza_selection, text='Pizza 5 Type',
                    font=('Open Sans', 20))
    p5t.grid(pady=5, padx=15, row=4, column=0)

    p5s=OptionMenu(pizza_selection, selection5, *pizza_types)
    p5s.grid(pady=5, padx=15, row=4, column=1)
    p5s.config(width=20)

    enter_button=tk.Button(pizza_selection, text='Enter',
                           font=('Open Sans', 15), command=save_order)
    enter_button.grid(row=5, column=0, pady=10, padx=30)
    enter_button.config(height=2, width=25)
    

def return_order():
    # Local function to save order to text file open the next window when done
    def save_and_reset():
        f = open('order_receipts.txt', 'a') 
        f.write(f'Customer Name: {customer_name}\n')
        f.write(f'\n')
        reset(order_details)


    order_details=tk.Tk() #Root addressess widget
    order_details.geometry('600x700')
    order_details.title('Order details')
    order_details.iconbitmap('assets/images/pizza_icon.ico')
    window=tk.Frame(order_details)
    window.grid()

    text=Label(window, text='Customer Name:',
                    font=('Open Sans', 25))
    text.grid(pady=5, padx=15, row=0, column=0)

    text=Label(window, text=customer_name,
                    font=('Open Sans', 25))
    text.grid(pady=5, padx=15, row=0, column=1)
    
    if delivery==True:
        text=Label(window, text='Delivery Cost:',
                        font=('Open Sans', 25))
        text.grid(pady=5, padx=15, row=1, column=0)

        text=Label(window, text=f'${DELIVERY_COST}',
                        font=('Open Sans', 25))
        text.grid(pady=5, padx=15, row=1, column=1)
    
        text=Label(window, text='Delivery Address:',
                        font=('Open Sans', 25))
        text.grid(pady=5, padx=15, row=2, column=0)

        text=Label(window, text=delivery_address,
                        font=('Open Sans', 25))
        text.grid(pady=5, padx=15, row=2, column=1)
    else:
        text=Label(window, text='Pickup in store',
                        font=('Open Sans', 25))
        text.grid(pady=5, padx=15, row=1, column=0)
    
    text=Label(window, text='Pizzas Ordered:',
                    font=('Open Sans', 25))
    text.grid(pady=5, padx=15, row=3, column=0)

    text=Label(window, text='Cost:',
                    font=('Open Sans', 25))
    text.grid(pady=5, padx=15, row=3, column=1)

    for pizza in range(0,5):
        global total_cost
        if pizza_selections[pizza] != 'None':
            text=Label(window, font=('Open Sans', 25),
                        text=
                        f'Pizza {pizza+1} {pizza_selections[pizza]}:')
            text.grid(pady=5, padx=15, row=4+pizza, column=0)

            text=Label(window, font=('Open Sans', 25),
                        text=f'${pizza_cost(pizza_selections[pizza])}')
            text.grid(pady=5, padx=15, row=4+pizza, column=1)
            try:
                print(pizza_cost(pizza_selections[pizza]))
                total_cost+=pizza_cost(pizza_selections[pizza])
            except:
                print('No pizza selected')

    if delivery == True:
        total_cost+=3

    text=Label(window, text='Total Cost:',
                    font=('Open Sans', 25))
    text.grid(pady=5, padx=15, row=9, column=0)

    text=Label(window, text=f'${total_cost}',
                    font=('Open Sans', 25))
    text.grid(pady=5, padx=15, row=9, column=1)
    
    save_exit_button=Button(order_details, text='Close order',
                           font=('Open Sans', 15),
                           command=save_and_reset)
    save_exit_button.grid(row=10, column=0, pady=10, padx=30)
    save_exit_button.config(height=2, width=25)

    cancel_exit_button=tk.Button(order_details, text='Cancel order',
                           font=('Open Sans', 15),
                           # Has to be a lambda function to work
                           command=lambda: reset(order_details)) 
    cancel_exit_button.grid(row=10, column=0, pady=10, padx=30)
    cancel_exit_button.config(height=2, width=25)

# Function to check which list a pizza is in and return a cost
def pizza_cost(var):
    if var in CHEAP_PIZZA:
        return 10.50
    elif var in PREMIUM_PIZZA:
        return 15.50
    else:
        return 'Error, redo order'

def reset(var):
        global customer_name
        global delivery
        global delivery_address
        global pizza_selections
        global total_cost
        customer_name=''
        delivery=False
        delivery_address=''
        pizza_selections=[]
        total_cost=0

        if var != None:
            var.destroy()


frame=Frame(root)
frame.pack()

bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)

text=Label(frame, text='Pizza Order Program', 
               font=('Open Sans', 25))
text.pack(side=TOP, pady=30)

quit_button=Button(bottom_frame, text='Quit', font=('Open Sans', 15),
                     command=root.destroy)
quit_button.pack(side=RIGHT, pady=30, padx=30)
quit_button.config(height=2, width=10)

order_button=tk.Button(bottom_frame, text='New order', 
                       font=('Open Sans', 15), command=order)
order_button.config( height=2, width=10 )
order_button.pack(side=LEFT, pady=30, padx=30)

root.mainloop()
