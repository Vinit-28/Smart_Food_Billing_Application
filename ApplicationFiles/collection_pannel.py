from tkinter import *
import ApplicationFiles.new_order_window
from tkinter import messagebox
from ApplicationFiles.Database_Operations import ask_query



##---------------to remove space from string---------------##  
def space_remover(string):
    string1=''
    for i in string:
        if not i == ' ':
            string1 = string1 + i
    return(string1)
##---------------END of this function---------------##  



##---------------to get month index---------------##  
def get_month_index(string):
    month_lst = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nuv','dec']
    index=0
    while index < 12:
        if month_lst[index] == string:
            return(index)
        index+=1
##---------------END of this function---------------##  




##---------------collection pannel 4---------------##
def collection_pannel_4(collection_screen,tablename , total_colllection , collection_list, username, total_orders, signal1,signal2):


    ##-------------creating canvas--------------##
    Canvas(collection_screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    ##-------------creating label 'Administrator Pannel'--------------##
    Label(collection_screen,text="Revenue Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)
    

    ##---------creating vertical scroll bar---------##
    v_scrollbar = Scrollbar(collection_screen,orient =VERTICAL)
    v_scrollbar.pack(side=RIGHT,padx=350,pady=350,fill =Y)

    ##---------creating listbox---------##
    listbox = Listbox(collection_screen,height=15,width=50,cursor='dot',selectbackground='orange',yscrollcommand = v_scrollbar.set)
    listbox.place(x=700,y=300)

    ##---------Displaying the collection items or orders---------##
    index = 0 
    for item in collection_list:

        listbox.insert(index,'')
        listbox.insert(index+1 , item)
        index+=2
        
    ##---------connecting scroll bar to the listbox---------##
    v_scrollbar.config(command = listbox.yview)


    ##---------Displaying total collection---------##
    Label(collection_screen,text='Total Collection  : ',fg='green',bg='lightgray',font=('arial',14,'bold')).place(x=780,y=600)

    Label(collection_screen,text='Rs ' + str(total_colllection) + '.00',fg='blue',bg='lightgray',font=('arial',14,'bold')).place(x=950,y=600)


    ##---------function to call order window---------##
    def next_window_caller(direction):
        selected_item = listbox.curselection()
        nonlocal collection_screen
        if direction == "ahead" and not (selected_item[0] % 2 == 0) :

            v_scrollbar.destroy()
            ##------------caling next page/window------------##
            ApplicationFiles.new_order_window.see_order_details(collection_screen,total_orders[selected_item[0]//2])
            

            collection_screen = Tk()
            collection_screen.geometry('1920x1080')
            collection_screen.title("Smart Food Application")
            Label(collection_screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)
            collection_pannel_4(collection_screen,tablename,total_colllection,collection_list,username,total_orders,signal1,signal2)
            
        
        elif direction == "back":
            v_scrollbar.destroy()
            collection_screen_pannel_3(collection_screen,tablename,signal1,signal2,username)
    
    ##---------END of this function---------##



    ##---------creating Buttons---------##
    Button(collection_screen,text = 'See Details',fg='green',bg='white',width=10,font=('times',13),command = lambda: next_window_caller("ahead")).place(x=1130,y=660)

    Button(collection_screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=lambda: next_window_caller("back")).place(x=590,y=660)



##---------------END of this function---------------##




##---------------collection pannel 3---------------##
def collection_screen_pannel_3(collection_screen,tablename,signal1,signal2,username):
    
    ##----------box creation-----------##
    Canvas(collection_screen,bg='lightgray',width=700,height=500).place(x=570,y=200)
    
    Label(collection_screen,text="Revenue Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)


    ##---------------if hours collection has to be find---------------##
    if signal1 == 'H':
        Label(collection_screen,text='Enter Year : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=320)

        Label(collection_screen,text='Month Name : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=360)

        Label(collection_screen,text='Enter Date : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=400)

        Label(collection_screen,text='From time : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=440)

        Label(collection_screen,text='To time : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=480)

        year_ans = StringVar()
        month_ans = StringVar()
        date_ans = StringVar()
        f_time_ans = StringVar()
        t_time_ans = StringVar()
        
        ##----------if table wise data has to be find---------##
        if signal2 == 'T':

            table_id = StringVar()
            Label(collection_screen,text='Table Id : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=520)
            ans_6 = Entry(collection_screen,textvariable=table_id,width=15,font=('calibri',12)).place(x=950,y=520)


        ans_1 = Entry(collection_screen,textvariable=year_ans,width=15,font=('calibri',12)).place(x=950,y=320)

        ans_2 = Entry(collection_screen,textvariable=month_ans,width=15,font=('calibri',12)).place(x=950,y=360)

        ans_3 = Entry(collection_screen,textvariable=date_ans,width=15,font=('calibri',12)).place(x=950,y=400)

        ans_4 = Entry(collection_screen,textvariable=f_time_ans,width=15,font=('calibri',12)).place(x=950,y=440)

        ans_5 = Entry(collection_screen,textvariable=t_time_ans,width=15,font=('calibri',12)).place(x=950,y=480)

        Label(collection_screen,text='Note* Time Guide :  20:13:58  /  hr : min : sec',bg='lightgray',font=('times',12,'bold')).place(x=600,y=580)


    ##---------------if date wise collection has to be find---------------##
    elif signal1 == 'D':

        Label(collection_screen,text='Enter Year : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=360)

        Label(collection_screen,text='Month Name : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=410)

        Label(collection_screen,text='From Date : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=460)

        Label(collection_screen,text='To Date : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=510)


        year_ans = StringVar()
        month_ans = StringVar()
        f_date_ans = StringVar()
        t_date_ans = StringVar()

        ##----------if table wise data has to be find---------##
        if signal2 == 'T':

            table_id = StringVar()
            Label(collection_screen,text='Table Id : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=560)
            ans_5 = Entry(collection_screen,textvariable=table_id,width=15,font=('calibri',12)).place(x=950,y=560)

        
        ans_1 = Entry(collection_screen,textvariable=year_ans,width=15,font=('calibri',12)).place(x=950,y=360)

        ans_2 = Entry(collection_screen,textvariable=month_ans,width=15,font=('calibri',12)).place(x=950,y=410)

        ans_3 = Entry(collection_screen,textvariable=f_date_ans,width=15,font=('calibri',12)).place(x=950,y=460)

        ans_4 = Entry(collection_screen,textvariable=t_date_ans,width=15,font=('calibri',12)).place(x=950,y=510)


    ##---------------if monthly collection has to be find---------------##
    elif signal1 == 'M':

        Label(collection_screen,text='Enter Year : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=360)

        Label(collection_screen,text='From Month : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=420)

        Label(collection_screen,text='To Month : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=480)

        

        year_ans = StringVar()
        f_month_ans = StringVar()
        t_month_ans = StringVar()

        ##----------if table wise data has to be find---------##
        if signal2 == 'T':

            table_id = StringVar()
            Label(collection_screen,text='Table Id : ',fg='black',bg='lightgray',font=('calibri',11,'bold')).place(x=720,y=540)
            ans_3 = Entry(collection_screen,textvariable=table_id,width=15,font=('calibri',12)).place(x=950,y=540)

        
        ans_1 = Entry(collection_screen,textvariable=year_ans,width=15,font=('calibri',12)).place(x=950,y=360)

        ans_2 = Entry(collection_screen,textvariable=f_month_ans,width=15,font=('calibri',12)).place(x=950,y=420)

        ans_3 = Entry(collection_screen,textvariable=t_month_ans,width=15,font=('calibri',12)).place(x=950,y=480)

        Label(collection_screen,text='Note* Month Guide :  January / Jan',bg='lightgray',font=('times',12,'bold')).place(x=600,y=600)


    ##---------------if yearly collection has to be find---------------##
    elif signal1 == 'Y':
        f_year_q = Label(collection_screen,text='From Year : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=380)

        t_year_q = Label(collection_screen,text='To Year : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=440)

        

        f_year_ans = StringVar()
        t_year_ans = StringVar()

        ##----------if table wise data has to be find---------##
        if signal2 == 'T':

            table_id = StringVar()
            Label(collection_screen,text='Table Id : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=500)
            ans_3 = Entry(collection_screen,textvariable=table_id,width=15,font=('calibri',12)).place(x=950,y=500)

        
        ans_1 = Entry(collection_screen,textvariable=f_year_ans,width=15,font=('calibri',12)).place(x=950,y=380)

        ans_2 = Entry(collection_screen,textvariable=t_year_ans,width=15,font=('calibri',12)).place(x=950,y=440)




    ##----------------function to check whether an input field is emoty or not----------------##
    def input_fields_checking():
        if signal1 == 'H':
            if year_ans.get() == "" or month_ans.get() == "" or date_ans.get() == "" or f_time_ans.get == "" or t_time_ans.get() == ""  or signal2 == 'T' and table_id.get() == "" :
                return(0)
        elif signal1 == 'D':
            if year_ans.get() == "" or month_ans.get() == "" or f_date_ans.get() == "" or t_date_ans.get() == "" or signal2 == 'T' and table_id.get() == "" :
                return(0)
        elif signal1 == 'M':
            if year_ans.get() == "" or f_month_ans.get() == "" or t_month_ans.get() == "" or signal2 == 'T' and table_id.get() == "" :
                return(0)
        elif signal1 == 'Y':
            if f_year_ans.get() == "" or t_year_ans.get() == "" or signal2 == 'T' and table_id.get() == "" :
                return(0)
        return(1)

    ##----------------END of this function----------------##   


    ##----------------function to find data accroding to user requirements----------------##
    def matching_data():
        if not input_fields_checking():
            messagebox.showerror("Input Field Issue","All Fields are Required to be Filled")
            return

        try:
            total_amount=0
            collection_list = []
            index=0

            query = f"SELECT * FROM {tablename};"

            query_result, is_successfull = ask_query(query)
            
            if is_successfull:
                total_orders = query_result.fetchall()

                for row  in total_orders:
                    previous = total_amount
                    date_time , table_number , order_amount = row[0],row[1],row[3]
                    date_time = date_time.lower()
                    temp=''
                    order_year = space_remover(date_time[-4:])
                    order_month = space_remover(date_time[4:7]) 
                    order_day = space_remover(date_time[:4])
                    order_date = space_remover(date_time[8:10])   
                    order_time = space_remover(date_time[11:-5])  

                    

                    if signal1 == 'H' :
                        month = month_ans.get()
                        month = month[:3].lower()
                        if order_time >= f_time_ans.get() and order_time <= t_time_ans.get() and  order_month == month and order_date == date_ans.get() and order_year == year_ans.get() :
                            if signal2 == 'T' and table_id.get() == table_number:
                                total_amount += order_amount
                                #collection_list.append('Rs ' + str(order_amount) + '.00 , recieved on ' + order_day + ' , ' + str(order_month) + ' ' + str(order_date) + '  ')
                            elif signal2 == 'R':
                                total_amount += order_amount

                    elif signal1 == 'D':
                        month = month_ans.get()
                        month = month[:3].lower()
                        if  order_date >= f_date_ans.get() and order_date <= t_date_ans.get() and  order_month == month and order_year == year_ans.get() :
                            if signal2 == 'T' and table_id.get() == table_number:
                                total_amount += order_amount
                            elif signal2 == 'R':
                                total_amount += order_amount
                            

                    elif signal1 == 'M':
                        
                        string = f_month_ans.get()
                        string = string.lower()
                        f_month_ans_index = get_month_index(string[:3])
                        string = t_month_ans.get()
                        string = string.lower()
                        t_month_ans_index = get_month_index(string[:3])
                        order_month_index = get_month_index(order_month)

                        if    order_month_index >= f_month_ans_index and order_month_index <= t_month_ans_index and order_year == year_ans.get() :
                            if signal2 == 'T' and table_id.get() == table_number:
                                total_amount += order_amount
                            elif signal2 == 'R':
                                total_amount += order_amount
                    
                    elif signal1 == 'Y':
                        if order_year >= f_year_ans.get() and order_year <= t_year_ans.get() :
                            if signal2 == 'T' and table_id.get() == table_number:
                                total_amount += order_amount
                            elif signal2 == 'R':
                                total_amount += order_amount
                    
                    if total_amount > previous :
                        collection_list.append('  Rs ' + str(order_amount) + '.00 , recieved on ' + order_day + ' , ' + str(order_month) + ' ' + str(order_date) + '  ')
                    
                    index+=1

                if total_amount == 0:
                    messagebox.showinfo("Revenue Details","Total Revenue is 0 !!!")
                else:
                    collection_pannel_4(collection_screen,tablename,total_amount,collection_list,username,total_orders,signal1,signal2)
            
            else:
                messagebox.showinfo("Revenue Details","Total Revenue is 0 !!!")
        except:
            messagebox.showerror("Data Issue","No Record Exists")

    ##----------------END of this function----------------##


    Button(collection_screen,text='Submit',fg='green',bg='white',width=12,font=("times",12),command= matching_data).place(x=1130,y=650)

    Button(collection_screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=lambda: collection_screen_pannel_1(collection_screen,username)).place(x=590,y=650)


##-----------------END of this function------------------##



##--------------Function for Restaurant and table option---------------##
def collection_screen_pannel_2(collection_screen,tablename,signal1,username):

    ##--------------Button for Restaurant---------------##
    Button(collection_screen,text='For Restaurant',fg='blue',bg='white',width=12,font=('times',11),command = lambda:collection_screen_pannel_3(collection_screen,tablename,signal1,'R',username)).place(x=1120,y=580)

    ##--------------Button for Table---------------##
    Button(collection_screen,text='For Table',fg='blue',bg='white',width=12,font=('times',11),command = lambda:collection_screen_pannel_3(collection_screen,tablename,signal1,'T',username)).place(x=1120,y=630)


##--------------END of this function---------------##



##---------------collection pannel---------------##
def collection_screen_pannel_1(screen,username):

    global tablename 
    tablename = username + '_permanent_file'

    # global collection_screen
    
    ##---------Screen creation---------##
    if screen == None:
        collection_screen = Tk()
        collection_screen.geometry('1920x1080')
        collection_screen.title("Smart Food Application")
        Label(collection_screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)

    else:
        collection_screen = screen


    ##---------creating labels and box---------##
    Canvas(collection_screen,bg='lightgray',width=700,height=500).place(x=570,y=200)
    
    Label(collection_screen,text="Revenue Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)

    

    ##---------creating options with buttons---------##

    Button(collection_screen,text="Hour - Wise",fg='green',bg='white',width=20,font=('arial',14,'bold'),command = lambda:collection_screen_pannel_2(collection_screen,tablename,'H',username)).place(x=650,y=400)


    Button(collection_screen,text="Date - Wise",fg='green',bg='white',width=20,font=('arial',14,'bold'),command = lambda:collection_screen_pannel_2(collection_screen,tablename,'D',username)).place(x=950,y=400)


    Button(collection_screen,text="Month - Wise",fg='green',bg='white',width=20,font=('arial',14,'bold'),command = lambda:collection_screen_pannel_2(collection_screen,tablename,'M',username)).place(x=650,y=500)


    Button(collection_screen,text="Year - Wise",fg='green',bg='white',width=20,font=('arial',14,'bold'),command = lambda:collection_screen_pannel_2(collection_screen,tablename,'Y',username)).place(x=950,y=500)


    Button(collection_screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=collection_screen.destroy).place(x=590,y=650)



    collection_screen.mainloop()


##---------------END of tis function---------------##
