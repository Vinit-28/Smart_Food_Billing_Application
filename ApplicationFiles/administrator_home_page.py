from tkinter import *
from tkinter import messagebox
import ApplicationFiles.collection_pannel
from ApplicationFiles.new_orders_pannel import *
from ApplicationFiles.menu_list_pannel import *
from ApplicationFiles.Database_Operations import create_necessary_tables




def checking_file(tablename):

    query = f"SELECT * FROM {tablename} ;"

    query_result, is_successfull = ask_query(query)

    if is_successfull:
        return len(query_result.fetchall())
    
    return 0


##------------------Admi=80nistrator home page-------------------##
def administrator_home_page(username,password,screen=None):

    create_necessary_tables(username)
    
    if screen == None:
        screen = Tk()
        screen.geometry('1920x1080')
        screen.title("Smart Food Application")
        Label(screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)

    

    ##-------------creating label 'Administrator Pannel'--------------##
    
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)
    
    Label(screen,text="Administrator Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=780,y=230)

    
    hi_label = Label(screen,text='hi  ' + username + ' ....',bg='lightgray',font=('times',15,'bold italic')).place(x=850,y=300)



    ##------------------option creation-------------------##

    ##---------if there are no new notifications or transactions---------##
    def warning_labels(signal):
        if signal == 'N':
            messagebox.showinfo("Orders Info","No New Orders !!")
        
        elif signal == 'T':
            messagebox.showinfo("Transaction Info","No New Transactions !!")


    ##-------------to call next page and destroy its own screen-------------##
    def next_pge_caller_and_destroyer(signal,toatl_orders=0,total_transactions=0):

        if signal == 'O':

            if total_orders == 0:
                warning_labels('N')
                return
            else:   
                new_notifications_page(screen,tablename = username+'_new_orders',signal='O')
        
        elif signal == 'T':
            
            if total_transactions == 0:
                warning_labels('T')
                return
            else:
                new_notifications_page(screen,tablename= username+'_new_transactions',signal='T')
        
        elif signal == 'M':
            menu_list_pannel(screen,tablename = username+'_menu_list')
        
        elif signal == 'C':
            ApplicationFiles.collection_pannel.collection_screen_pannel_1(screen,username)
        
        administrator_home_page(username,password)

    ##-------------END of this function-------------##
    


    ##---------checking notification file exists or not---------##

    total_orders = checking_file(tablename = username + '_new_orders')
    total_transactions = checking_file(tablename = username + '_new_transactions')

    
    if total_orders == 0:
        total_orders_str = ""
    else:
        total_orders_str = f"  ( {total_orders} )"
    
    if total_transactions == 0:
        total_transactions_str = ""
    else:
        total_transactions_str = f"  ( {total_transactions} )"

   
    
    ##---------New Orders---------##
    Button(screen,text=f'New Orders'+total_orders_str,fg='green',bg='white',width=20,font=('arial',14,'bold'),command = lambda: next_pge_caller_and_destroyer(signal='O',toatl_orders=total_orders)).place(x=650,y=400)


    ##---------New Transactions---------##
    Button(screen,text=f'Transactions'+total_transactions_str,fg='green',bg='white',width=20,font=('arial',14,'bold'),command = lambda: next_pge_caller_and_destroyer(signal='T',total_transactions=total_transactions)).place(x=950,y=400)


    ##---------Revenue---------##
    Button(screen,text='Revenue',fg='green',bg='white',width=20,font=('arial',14,'bold'),command = lambda: next_pge_caller_and_destroyer(signal='C')).place(x=650,y=500)


    ##---------Menu List---------##
    Button(screen,text='Menu List',fg='green',bg='white',width=20,font=('arial',14,'bold'),command = lambda: next_pge_caller_and_destroyer(signal='M')).place(x=950,y=500)


    ##---------Log Out---------##
    Button(screen,text="Log  Out",bg='white',fg='red',font=('times',13),width=8,command=screen.destroy).place(x=590,y=650)

   
    screen.mainloop()

##------------------END of this function-------------------##
