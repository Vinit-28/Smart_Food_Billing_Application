from tkinter import *
from tkinter import messagebox
from ApplicationFiles.administrator_login_page import *
from ApplicationFiles.Database_Operations import ask_query



##------------------function for Username Checking starts-------------------##(checks whether a username already exits or not while signup)
def username_checking(username_entered):
    
    query = f'''SELECT * FROM Server
                WHERE LoginId =  '{username_entered}'; '''
    
    query_rseult,is_successfull = ask_query(query)

    if is_successfull and len(query_rseult.fetchall()) == 0:
        return(1)

    return (0)
##------------------function for Username Checking starts-------------------##





##------------------function for Password validity-------------------##
def password_validity(password):
    len=0
    validity=""
    for i in password:
        if i == '&' or i == '@' or i == '#' or i == '$' or i == '*' :
            validity = validity + 'S'
        if i >='A' and i <= 'Z':
            validity = validity + 'U'
        if i >='a' and i <= 'z':
            validity = validity + 'L'
        len+=1
    for i in range(0,9):
        if str(i) in password:
            validity = validity + 'N'
    if ('S' in validity ) and ('N' in validity ) and  ('U' in validity )  and ('L' in validity )  and len >=8 :
        return(1)
    else:
        return(0)
##------------------function for Password validity END-------------------##



##------------------function for signup-------------------##
def signup(screen):
    
    ##-------------creating canvas--------------##
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    ##-------------creating label 'Administrator Pannel'--------------##
    Label(screen,text="Administrator SignUp Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=780,y=230)
    

    ####---------------------Asking Questions to user---------------------------####

    ##-------------creating label 'Enter Username'--------------##
    U_N = Label(screen,text="Enter  Username :",bg='lightgray',fg='black',font=('arial',12,'bold')).place(x=700,y=290)


    ##-------------creating label 'Enter Password'--------------##
    P_W = Label(screen,text="Enter  Password :",bg='lightgray',fg='black',font=('arial',12,'bold')).place(x=700,y=340)


    # ##-------------creating label 'Confirm Password'--------------##
    C_P_W = Label(screen,text="Confirm  Password :",bg='lightgray',fg='black',font=('arial',12,'bold')).place(x=700,y=390)


    ##-------------creating label 'email'--------------##
    E_M = Label(screen,text="Enter  E-mail :",bg='lightgray',fg='black',font=('arial',12,'bold')).place(x=700,y=440)


    ##-------------creating label 'phone number'--------------##
    P_N = Label(screen,text="Phone  Number :",bg='lightgray',fg='black',font=('arial',12,'bold')).place(x=700,y=490)


    ##-------------creating label 'restaurant name'--------------##
    R_N = Label(screen,text="Restaurant  Name :",bg='lightgray',fg='black',font=('arial',12,'bold')).place(x=700,y=540)


    ##----------------variables for answers-----------------##

    username=StringVar()
    password=StringVar()
    confirm_password=StringVar()
    email=StringVar()
    restaurant_name=StringVar()
    phone_number=StringVar()


    ####--------------------------Answer Boxes------------------------------####


    ##-------------creating input box for username--------------##
    U_N_A = Entry(screen,bg='white',textvariable=username,fg='black',width=17,font=('arial',12)).place(x=1000,y=290)

    ##-------------creating input box for password--------------##
    P_W_A = Entry(screen,bg='white',textvariable=password,fg='black',width=17,font=('arial',12),show="*").place(x=1000,y=340)


    ##-------------creating input box for confirm password--------------##
    C_P_W_A = Entry(screen,bg='white',textvariable=confirm_password,fg='black',width=17,font=('arial',12),show="*").place(x=1000,y=390)

    ##-------------creating input box for email--------------##
    E_M_A = Entry(screen,bg='white',textvariable=email,fg='black',width=17,font=('arial',12)).place(x=1000,y=440)

    ##-------------creating input box for phone number--------------##
    P_N_A = Entry(screen,bg='white',textvariable=phone_number,fg='black',width=17,font=('arial',12)).place(x=1000,y=490)

    ##-------------creating input box for hotel name--------------##
    R_N_A = Entry(screen,bg='white',textvariable=restaurant_name,fg='black',width=17,font=('arial',12)).place(x=1000,y=540)



    ##------------------function for saving the details of the user into a text file-------------------##
    def file_handling():

        password_signal=password_validity(password.get())
        signal=username_checking(username.get())
        
        ##-------------if username already exists---------------##
        if signal==0:
            messagebox.showerror("Username Issue","Username Already Exists")

        ##-------------if Password is invalid according to password guidelines---------------##
        elif password_signal == 0:
             
            messagebox.showerror("Password Standard Issue","Password should contain atleast 8 characters and one symbol (@,#,*..), a number (0-9), an uppercase letter and an lowercase letter")
            
        ##-------------if password and confirm password are not same---------------##
        elif password.get() != confirm_password.get():
            
            messagebox.showerror("Password Issue","Password Should be Same")
            

        ##-------------if anyone field is not filed---------------##
        elif  username.get()=="" or password.get()=="" or email.get()=="" or restaurant_name.get()=="" or phone_number.get()=="" :
            
            messagebox.showerror("Field Empty Issue","All Fields are Required to be Filled")

        ##-------------if signup successfull---------------##
        else :
            
            query = f'''INSERT INTO Server (LoginId, LoginPassword, EMail, RestroName, Contact)
                        VALUES ( '{username.get()}', '{password.get()}', '{email.get()}', '{restaurant_name.get()}', '{phone_number.get()}' ); '''
            
            ask_query(query)
            
            messagebox.showinfo("Registration Successfull","Your Account has Created ... Now Login") 

            login(screen) 


    ##------------------function for saving the details of the user into a text file END-------------------##


    ##-------------Button for signup--------------##
    Button(screen,text="Sign up",fg='green',width=14,bg='white',font=('times',14,'bold'),command=file_handling).place(x=850,y=610)
    
    Button(screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=screen.destroy).place(x=590,y=660)


    screen.mainloop()

##------------------function for signup  END-------------------##
