from tkinter import *
from tkinter import messagebox
from ApplicationFiles.administrator_home_page import *
from ApplicationFiles.Database_Operations import ask_query


##------------------ function for user access checking -------------------##
def user_access_checking(entered_username,entered_password):

    query = f'''SELECT * FROM Server
                WHERE LoginId = '{entered_username}' and LoginPassword = '{entered_password}';'''

    query_result,is_successfull = ask_query(query)

    if is_successfull == False:
        return(0)
    
    return len(query_result.fetchall())
##------------------ function for user access checking END-------------------##



##------------------function for login-------------------##
def login(screen):

    ##-------------creating canvas--------------##
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    ##-------------creating label 'Administrator Pannel'--------------##
    Label(screen,text="Administrator Login Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=780,y=230)

    ##-------------creating label 'Enter Username'--------------##
    U_N = Label(screen,text="Enter  Username :",bg='lightgray',fg='black',font=('arial',13,'bold')).place(x=700,y=380)


    ##-------------creating label 'Enter Password'--------------##
    P_W = Label(screen,text="Enter  Password :",bg='lightgray',fg='black',font=('arial',13,'bold')).place(x=700,y=460)


    username=StringVar()
    password=StringVar()

    ##-------------creating input box for username--------------##
    U_N_A = Entry(screen,bg='white',textvariable=username,width=20,font=('arial',15)).place(x=900,y=380)

    ##-------------creating input box for password--------------##
    P_W_A = Entry(screen,bg='white',textvariable=password,width=20,font=('arial',15),show="*").place(x=900,y=460)




    ##------------------ function to call user access fuction when login button pressed -------------------##
    def login_button_pressed():
        signal = user_access_checking(username.get(),password.get())
        ##----------- if access approved--------------##
        if signal==1:
            # screen.destroy()
            administrator_home_page(str(username.get()),str(password.get()),screen)
            # login()
        ##----------- if access denied--------------##   
        else:
            messagebox.showerror("Invalid Credentials","Invalid Username or Password")

    ##-------------Button for login--------------##
    login_button = Button(screen,text="Login",fg='green',bg='white',font=('times',14,'bold'),width=14,command=login_button_pressed).place(x=850,y=570)


    Button(screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=screen.destroy).place(x=590,y=650)

    screen.mainloop()

##------------------function for login  END-------------------##
