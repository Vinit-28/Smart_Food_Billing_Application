from tkinter import *
from ApplicationFiles.new_order_window import *
from ApplicationFiles.Database_Operations import ask_query


##-----------------function to see the details of an orders-----------------##
def to_call_see_order_details_function(listbox,tablename,signal,screen,scrollbars,total_orders):
    
    selected_item = listbox.curselection()
    
    if not (selected_item[0] % 2 ==0) :
        index=selected_item[0]//2
        scrollbars[0].destroy()
        scrollbars[1].destroy()

        see_order_details(screen,total_orders[index])

        new_notifications_page(None,tablename,signal)

##-----------------END of this function-----------------##



##-----------------function to remove the orders from order list-----------------##
def remove_orders(listbox,tablename,total_orders,screen,signal,scrollbars):
    selected_item = listbox.curselection()

    if not (selected_item[0] % 2 ==0) :
        index=selected_item[0]//2
        listbox.delete(selected_item[0])
        listbox.delete(selected_item[0]-1)

        order_date = total_orders[index][0]
        tableno = total_orders[index][1]

        query = f"DELETE FROM {tablename} WHERE Date = '{order_date}' and TableNo = {tableno};"

        ask_query(query)

        scrollbars[0].destroy()
        scrollbars[1].destroy()
        listbox.destroy()
        new_notifications_page(screen,tablename,signal)

##-----------------END of this function-----------------##



##-----------------new orders page-----------------##
def new_notifications_page(screen,tablename,signal):
    
    ##-----------------screen creation-----------------##

    if screen == None:
        screen = Tk()
        screen.geometry('1920x1080')
        screen.title("Smart Food Application")
        Label(screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)



    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    
    if signal == 'O': 
        Label(screen,text="New Orders Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=780,y=230)
    elif signal == 'T':
        Label(screen,text="New Transaction Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=780,y=230)


    query = f"SELECT * FROM {tablename};"

    query_result, is_successfull = ask_query(query)


    ##-----------------creating scrollbar-----------------##
    vertical_scrollbar = Scrollbar(screen)
    vertical_scrollbar.pack(side = RIGHT,fill = Y,pady=350,padx=200)


    horizontal_scrollbar = Scrollbar(screen,orient = HORIZONTAL)
    horizontal_scrollbar.pack(side=BOTTOM,fill=X,pady=100,padx=550)
    


    ##-----------------creating Listbox or list of orders-----------------##
    listbox = Listbox(screen,bg='white',fg='black',height=15,width=50,font=('times',13,'bold'),cursor = 'dot',selectbackground='orange',xscrollcommand=horizontal_scrollbar.set,yscrollcommand=vertical_scrollbar.set)
    listbox.place(x=680,y=290)


    ##-----------------Button creations-----------------##
    Button(screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=screen.destroy).place(x=590,y=650)


    if is_successfull:
        index=0
        listbox_index = 1
        
        total_orders = query_result.fetchall()
        for row in total_orders:

            if signal == 'T':
                table_number, customer_name, order_amount = row[1],row[2],row[3]
                listbox.insert(index,'')
                listbox.insert(index+1,'  ' + str(listbox_index) + '.   Rs ' + str(order_amount) + ', recieved from ' + customer_name + ', table ' + str(table_number) + '  ')

            elif signal == 'O':
                table_number, customer_name = row[1],row[2]
                listbox.insert(index,'')
                listbox.insert(index+1,'  ' + str(listbox_index) + '.   '  + customer_name + ',  from table ' + str(table_number) + '  ')
            index+=2
            listbox_index+=1
        
        if index > 0:
            Button(screen,text='Remove',fg='blue',bg='white',width=15,command=lambda:remove_orders(listbox,tablename,total_orders,screen,signal, [vertical_scrollbar,horizontal_scrollbar])).place(x=990,y=600)

            Button(screen,text='See Details',fg='green',bg='white',width=15,command=lambda:to_call_see_order_details_function(listbox,tablename,signal,screen,[vertical_scrollbar,horizontal_scrollbar],total_orders)).place(x=680,y=600)

        else:

            Button(screen,text='See Details',fg='green',bg='white',width=15,state=DISABLED).place(x=680,y=600)

            Button(screen,text='Remove',fg='blue',bg='white',width=15,state=DISABLED).place(x=990,y=600)

    else:

        Button(screen,text='See Details',fg='green',bg='white',width=15,state=DISABLED).place(x=680,y=600)

        Button(screen,text='Remove',fg='blue',bg='white',width=15,state=DISABLED).place(x=990,y=600)




    ##-----------------connecting scroll bar to the listbox-----------------##
    vertical_scrollbar.config(command=listbox.yview)
    horizontal_scrollbar.config(command=listbox.xview)
    
    
    screen.mainloop()

##-----------------END of this function-----------------##
