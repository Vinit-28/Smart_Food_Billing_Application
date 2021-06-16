from tkinter import *
from tkinter import messagebox
from ApplicationFiles.menu_list_page import *
from ApplicationFiles.Database_Operations import ask_query



##------------------function for Username Checking starts-------------------##
def username_checking(username_entered):

    query = f'''SELECT * FROM Server
                WHERE LoginId =  '{username_entered}'; '''
    
    query_rseult,is_successfull = ask_query(query)

    if is_successfull:
        return len(query_rseult.fetchall())

    return (0)
##------------------function for Username Checking starts-------------------##




def customer_home_page(screen=None):

    ##------------------screen creation-------------------##
    if screen == None:
        screen = Tk()
        screen.geometry('1920x1080')
        screen.title("Smart Food Application")
        Label(screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)


    ##-------------creating canvas and Label--------------##
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    Label(screen,text="Customer Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=780,y=230)

    
    ##------------------Asking Questions-------------------##
    Label(screen,text='Enter Hotel Username : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=360)

    Label(screen,text='Enter Table Number : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=420)

    Label(screen,text='Enter Your Name : ',bg='lightgray',font=('arial',12,'bold')).place(x=720,y=480)


    ##------------------Getting Answers-------------------##
    hotel_username = StringVar()
    table_number = StringVar()
    customer_name = StringVar()

    a_1 = Entry(screen,textvariable=hotel_username,width=15,font=('arial',12)).place(x=950,y=360)

    a_2 = Entry(screen,textvariable=table_number,width=15,font=('arial',12,)).place(x=950,y=420)

    a_3 = Entry(screen,textvariable=customer_name,width=15,font=('arial',12,)).place(x=950,y=480)


    ##------------------To call Menu List page-------------------##
    def call_menu_list_page():

        if len(hotel_username.get()) == 0 or len(customer_name.get()) == 0 :
            messagebox.showerror("Input Field Issue","All Fields are Required to be Filled")
        
        else:
            if username_checking(hotel_username.get()) == 0:
                messagebox.showerror("Invalid Input","Invalid Hotel UserName")
            else:
                if(menu_list_page(screen,hotel_username.get(),table_number.get(),customer_name.get())):
                    customer_home_page(screen = None)
                
                
    ##------------------Done button-------------------##

    Done = Button(screen,text='Done',fg='green',bg='white',width=10,command=call_menu_list_page).place(x=860,y=570)

    Button(screen,text="Back",bg='white',fg='red',font=('times',15),width=8,command=screen.destroy).place(x=590,y=650)

    screen.mainloop()
