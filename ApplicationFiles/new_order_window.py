from tkinter import *



##---------------for extracting the data from an single line---------------##
def resolve_data(order):

    food_list = [food for food in order[4].split(' -- ')]
    price_list = [int(price) for price in order[5].split(' ')]
    qty_list = [int(qty) for qty in order[6].split(' ')]

    return(order[0],order[1],order[2],order[3],food_list,price_list,qty_list,len(food_list))

##---------------END of this function---------------##        


##---------------for adding spaces to the strings---------------##   
def space_adder(str1,str2,signal):
    limit=0
    if signal == 'I':
        if len(str1) < 15:
            limit = 15-len(str1)+1
            for i in range (0,limit) : 
                str1=str1+' '
            if str2[0]==' ':
                str2 = str2[1:]
            str1 = str1 + ':  ' + str2
            return(str1)
    elif signal == 'N' and len(str1) < 22:
        limit=22-len(str1)+1
    elif signal == 'Q' and len(str1) < 5:
        limit = 5-len(str1)+1
    elif signal == 'P' and len(str1) < 8:
        limit = 8-len(str1)+1
    if limit == 0:
        return(str1)
    for i in range(0,limit):
        str1 = str1 + ' '
    return(str1)
##---------------END of this function---------------##

        


##---------------To see the details of an order---------------##
def see_order_details(screen,order):
    

    ##----------Labels and Box creation----------##

    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    Label(screen,text="Order Details Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)

    ##----------creating horizontal and vertical scroll bars----------##
    vertical_scrollbar = Scrollbar(screen)
    vertical_scrollbar.pack(side=RIGHT,padx=550,pady=350,fill=Y)


    textbox = Text(screen,bg='lightblue',width=65,height=20,bd=2,fg='black',yscrollcommand=vertical_scrollbar.set,wrap='none')
    textbox.place(x=670,y=290)


    order_time,table_number,customer_name,total_amount,food_list,price_list,qty_list,limit = resolve_data(order)


    ##----------Adding spaces to them----------##
    table_number = space_adder('Table Number',str(table_number)+'\n','I')
    customer_name = space_adder('Customer Name',str(customer_name)+'\n','I')
    date = space_adder('Date',order_time[0:11]+order_time[-5:]+'\n','I')
    time = space_adder('Time',order_time[10:-4]+'\n','I')

    ##----------Entering in the textbox----------##
    textbox.insert(END,'\n'+customer_name)
    textbox.insert(END,table_number)
    textbox.insert(END,date)
    textbox.insert(END,time)

    textbox.insert(END,'\n\n  -----------Order List-----------\n\n')
    textbox.insert(END,' Product Name         Qty    Price    Total\n\n')


    for index in range(0,limit) :
        string = space_adder(' '+ food_list[index],'','N') +  space_adder(str(qty_list[index]),'','Q') + space_adder(str(price_list[index]),'','P') + str(price_list[index]*qty_list[index])
        textbox.insert(END,string+'\n')


    textbox.insert(END,' ------------------------------------------------- \n')
    string = space_adder(' Total','','N') +  space_adder('','','Q') + space_adder('','','P') + 'RS ' + str(total_amount) + '.00'
    textbox.insert(END,string)
    textbox.insert(END,'\n ------------------------------------------------- \n')


    ##----------connecting scrollbars to the textbox----------##
    
    vertical_scrollbar.config(comman = textbox.yview)

    ##----------making textbox disabled----------##
    textbox.config(state=DISABLED)


    ##----------sbutton to back or return to the previous page----------##
    Button(screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=screen.destroy).place(x=590,y=660)

    screen.mainloop()

##---------------END of this function---------------##
