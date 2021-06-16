from tkinter import *
from ApplicationFiles.administrator_login_page import *
from ApplicationFiles.administrator_signup_page import *
from ApplicationFiles.customer_home_page import *
from ApplicationFiles.Database_Operations import ask_query


##-------------to provide signup and login choice and call them--------------##
def signup_login_choice(sign):

    if sign == 'C':
        customer_home_page(screen)

    else:
        def function_call_and_screen_destroyer(signal):
            if signal == 'L':
                login(screen)
            elif signal == 'S':
                signup(screen)

        ##-------------Button for login--------------##
        Button(screen,text="Login",fg='blue',bg='white',command=lambda:function_call_and_screen_destroyer('L')).place(x=1050,y=300)

        ##-------------Button for signup--------------##
        Button(screen,text="signup",fg='green',bg='white',command=lambda:function_call_and_screen_destroyer('S')).place(x=1050,y=350)

    screen.mainloop()
    home_page()



def initialize_database():
    ##-------------Initializing Database--------------##
    query = "CREATE TABLE Server ( LoginId text PRIMARY KEY, LoginPassword  text NOT NULL, EMail text, RestroName text, Contact text) ;"
    ask_query(query)



def home_page():

    initialize_database() 
    
    ##-------------creating window--------------##
    global screen
    screen = Tk()
    screen.title("Smart Food Application")
    screen.geometry('1920x1080')

    ##-------------creating label 'home page'--------------##
    Label(screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)

    ##-------------creating canvas--------------##
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)


    ##-------------creating button for Administrator pannel--------------##
    Button(screen,text="Administrator  Pannel",bg='white',fg='green',font=('times',18,'bold'),height=2,command=lambda:signup_login_choice('A')).place(x=750,y=300)

    ##-------------creating button for Customer pannel--------------##
    Button(screen,text="Customer  Pannel",bg='white',fg='blue',font=('times',18,'bold'),height=2,width=20,command=lambda:signup_login_choice('C')).place(x=780,y=450)

    ##-------------creating button for Exit--------------##
    Button(screen,text="Exit",bg='white',fg='red',font=('times',15),width=8,command=screen.destroy).place(x=590,y=650)

    screen.mainloop()
##-------------END of this function--------------##
