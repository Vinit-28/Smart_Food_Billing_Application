from tkinter import *
from ApplicationFiles.bill_list_page import *

quantity=0
limit=0
final_order_quantity=[]


def order_list_page(screen,hotel_username, table_number, customer_name, ordered_list, reset = False):

    restore_previous_screen = True
    global limit
    
    if reset:

        global quantity,limit,final_order_quantity
        quantity =0
        limit =0
        final_order_quantity = []

    ##------------counting number of orders------------##
    key_list=[]
    for i in ordered_list:
        key_list.append(i)
        final_order_quantity.append(1)
        limit+=1


    
    ##------------screen creation------------##
    if screen == None:
        screen = Tk()
        screen.geometry('1920x1080')
        screen.title("Smart Food Application")
        Label(screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)


    ##-------------creating canvas and Label--------------##
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    Label(screen,text="Order List Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)


    ##------------individual's bill description------------##
    
    Label(screen,text="Product Name      :-",fg="black",bg="lightgray",font=("arial",13,"bold")).place(x=650,y=330)

    Label(screen,text="Quantity                :-",fg="black",bg="lightgray",font=("arial",13,"bold")).place(x=650,y=380)

    Label(screen,text="Price (per-head)   :-",fg="black",bg="lightgray",font=("arial",13,"bold")).place(x=650,y=430)

    Label(screen,text="Total Cost             :-",fg="black",bg="lightgray",font=("arial",13,"bold")).place(x=650,y=480)


    ##------------Printing one by one each order's detail------------##
    
    def next_prev_changer(symbol_changer,index):

        global quantity
        
        if symbol_changer=='-' and index>0:
            index-=1
        elif symbol_changer=='+' and index<limit-1:
            index+=1

        quantity=final_order_quantity[index]-1

        def qty_changer(symbol):
            global quantity
            if symbol=='-' and quantity>1:
                quantity-=1
            elif symbol=='+' and quantity<5:
                quantity+=1
            
            Label(screen,text=str(quantity),fg="black",bg="lightgray",font=("arial",13,"bold")).place(x=1090,y=380)
            Label(screen,text="Rs "+str(quantity*ordered_list[key_list[index]])+'.00',fg="green",bg="lightgray",width=8,font=("arial",13,"bold")).place(x=1050,y=480)


        
        qty_changer('+')      

        Label(screen,text=key_list[index],fg="black",bg="lightgray",width=14,font=("arial",12,"bold")).place(x=1050,y=330)

        Button(screen,text="--",fg="red",bg="white",font=("times",7,"bold"),command=lambda:qty_changer('-')).place(x=1110,y=380)
        
        Button(screen,text="+",fg="green",bg="white",height=0,font=("times",7,"bold"),command=lambda:qty_changer('+')).place(x=1050,y=380)

        Label(screen,text="Rs "+str(ordered_list[key_list[index]])+'.00 /-',fg="green",bg="lightgray",width=8,font=("arial",13,"bold")).place(x=1050,y=430)



        def final_list_recorder(symbol_changer):

            nonlocal restore_previous_screen

            final_order_quantity[index]=quantity
            
            if symbol_changer=='c':

                if(bill_list_page(screen,hotel_username, table_number, customer_name, ordered_list, final_order_quantity, limit)):
                    print("\nGot True\n")
                    order_list_page(None,hotel_username,table_number,customer_name,ordered_list,reset=False)
                else:
                    restore_previous_screen = False
            else:
                next_prev_changer(symbol_changer,index)
            
        

        ##------------for next button------------##

        if index==limit-1:
            Button(screen,text="Next",fg="blue",bg="white",width=10,font=("times",12,),state=DISABLED).place(x=1050,y=550)
        else:
            Button(screen,text="Next",fg="blue",bg="white",width=10,font=("times",12,),command=lambda:final_list_recorder('+')).place(x=1050,y=550)


        ##------------for previous button------------##         
        if index==0:
            Button(screen,text="Previous",bg="white",fg="blue",width=10,font=("times",12,),state=DISABLED).place(x=650,y=550)

        else:
            Button(screen,text="Previous",bg="white",fg="blue",width=10,font=("times",12,),command=lambda:final_list_recorder('-')).place(x=650,y=550)



        ##------------go to menu list button------------##
        Button(screen,text="Back",bg='white',fg='red',font=('times',15),width=8,command=screen.destroy).place(x=590,y=650)

        ##------------go to bill list button------------##
        Button(screen,text="Done",bg="white",fg="green",width=8,font=("times",15,),command=lambda:final_list_recorder('c')).place(x=1130,y=650)


        
        def remove_item():
            global limit
            if limit==1:
                screen.destroy()
            else:
                limit-=1
                ordered_list.pop(key_list[index])
                key_list.pop(index)
                final_order_quantity.pop(index)
                next_prev_changer(symbol_changer='+',index=index-1)
            
        
        Button(screen,text="Remove",bg="white",fg="red",font=("times",12),command=remove_item).place(x=1050,y=290)

        screen.mainloop()
        
        
    next_prev_changer('+',-1)

    return restore_previous_screen

##------------END of this Function------------##
