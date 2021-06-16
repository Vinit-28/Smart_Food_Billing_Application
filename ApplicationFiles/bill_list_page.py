from tkinter import *
import time
from tkinter import messagebox
from ApplicationFiles.Database_Operations import ask_query, create_necessary_tables


##------------Function to Format String------------##
def get_input(string, signal):
    total_char=0
    if signal=='n':
        string1='  '
    else:
        string1='    '
    for i in string:
        if total_char<=23:
            string1 = string1 + i
            total_char+=1
        else:
            break
    if total_char<23:
        for i in range(total_char+1,23):
            string1 = string1 + ' '

    return string1
##------------End of this Function------------##


##------------Getting Order Details------------##
def get_order_deatils(ordered_list,order_quantity):

    Qty = ""
    Products = ""
    Price = ""

    for key in ordered_list:
        Products += str(key) + " -- "
        Price += str(ordered_list[key]) + " "
    
    for i in order_quantity:
        Qty += str(i) + " "
    
    return Products[:-4], Price[:-1], Qty[:-1]

##------------End of this Function------------##



##------------writting orders in a text file so that administrator can read it------------##
def file_handling(hotel_username, table_number, customer_name, total_amount, ordered_list, order_quantity):
    
    create_necessary_tables(hotel_username)

    Products,Prices,Qty = get_order_deatils(ordered_list,order_quantity)


    query = f'''INSERT INTO {hotel_username}_new_orders ( Date, TableNo, CustomerName, TotalAmount, OrderList, PriceList, QtyList )
                VALUES ( '{str(time.ctime())}', {table_number}, '{customer_name}', {total_amount}, '{Products}', '{Prices}', '{Qty}' ) ;'''
    
    ask_query(query)

    query = f'''INSERT INTO {hotel_username}_new_transactions ( Date, TableNo, CustomerName, TotalAmount, OrderList, PriceList, QtyList )
                VALUES ( '{str(time.ctime())}', {table_number}, '{customer_name}', {total_amount}, '{Products}', '{Prices}', '{Qty}' ) ;'''
    
    ask_query(query)

    query = f'''INSERT INTO {hotel_username}_permanent_file ( Date, TableNo, CustomerName, TotalAmount, OrderList, PriceList, QtyList )
                VALUES ( '{str(time.ctime())}', {table_number}, '{customer_name}', {total_amount}, '{Products}', '{Prices}', '{Qty}' ) ;'''

    ask_query(query)


##------------End of this Function------------##






def bill_list_page(screen,hotel_username, table_number, customer_name, ordered_list, final_order_quantity, limit):

    restore_previous_screen = True
    ##------------screen creation------------##
    if screen == None:
        screen = Tk()
        screen.geometry('1920x1080')
        screen.title("Smart Food Application")
        Label(screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)


    ##-------------creating canvas and Label--------------##
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    Label(screen,text="Bill List Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)


    ##------------bill List Labels------------##
    Label(screen,text="Name",bg="lightgray",font=("arial",14,"bold")).place(x=640,y=290)

    Label(screen,text="Description",bg="lightgray",font=("arial",14,"bold")).place(x=850,y=290)

    Label(screen,text="Cost",bg="lightgray",font=("arial",14,"bold")).place(x=1060,y=290)


    ##------------scroll bar------------##
    scroll_bar = Scrollbar(screen)
    scroll_bar.pack(side=RIGHT,fill=Y,padx=400,pady=350)


    ##------------bill writing in textbox starts------------##

    textbox=Text(screen,bg="gray",width=70,height=17,fg="white",bd=0,yscrollcommand=scroll_bar.set)
    textbox.place(x=620,y=330)    


    total_sum=index=0
    for i in ordered_list:
        name=i
        des='( ' + str(final_order_quantity[index]) + 'x' + str(ordered_list[i]) + ' )'
        cost= 'Rs ' + str(final_order_quantity[index]*ordered_list[i]) + '.00'

        name=get_input(name,'n')
        des=get_input(des,'d')
        cost=get_input(cost,'c')

        whole_string= name + des + cost + '\n'

        textbox.insert(END,whole_string)
        total_sum = total_sum + (final_order_quantity[index]*ordered_list[i])
        index+=1

    name=get_input("Total",'n')
    des=get_input("",'d')
    cost=get_input('Rs '+str(total_sum)+'.00\-','c')
    whole_string= '\n'+name + des + cost 

    textbox.insert(END,whole_string)
    scroll_bar.config(command=textbox.yview)
    textbox.config(state="disabled")

    ##------------writing bill in textbox ended successfully------------##


    def success():
        nonlocal restore_previous_screen

        restore_previous_screen = False
        file_handling(hotel_username,table_number,customer_name,total_sum,ordered_list,final_order_quantity)

        messagebox.showinfo("Success","Your Order has Placed Successfully!!!\nPlease Wait 5 minutes...!!!")
        
        screen.destroy()

    ##------------pay button------------##
    Button(screen,text="Pay  "+'Rs '+str(total_sum),fg="green",bg="white",width=10,font=("times",15,),command=success).place(x=1090,y=650)


    ##------------go to order list button------------##
    Button(screen,text="Back",bg='white',fg='red',font=('times',15),width=8,command=screen.destroy).place(x=590,y=650)

    screen.mainloop()

    return restore_previous_screen

##------------End of this Function------------##
