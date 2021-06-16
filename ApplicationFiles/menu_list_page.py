from tkinter import *
from tkinter import messagebox
from ApplicationFiles.order_list_page import *
from ApplicationFiles.Database_Operations import create_necessary_tables,ask_query



##-------------------getting menu list from-------------------##
def get_menu_list(tablename):
    menu_dictionery = {}
    des_list = []
    menu = []
    
    query = f"SELECT * FROM {tablename};"

    query_result,is_successfull = ask_query(query)
    
    if is_successfull:
        
        menu = query_result.fetchall()

        for m in menu:
            menu_dictionery[m[0]] = m[1]
            des_list.append(m[2])

    return(menu_dictionery,des_list,menu)
##-------------------End of this function-------------------##



##-------------------adding space to product name and price-------------------##
def space_adding(string):
    string = '    ' + string
    print(string)
    while( not len(string)==73) :
        string = string + ' '
    return(string)
##-------------------End of this function-------------------##


##------------menu list page function------------##

def menu_list_page(screen,hotel_username, table_number, customer_name):

    restore_previous_screen = True

    create_necessary_tables(hotel_username)
    
    ##------------screen creation------------##
    if screen == None:
        screen = Tk()
        screen.geometry('1920x1080')
        screen.title("Smart Food Application")
        Label(screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)


    ##-------------creating canvas and Label--------------##
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)

    Label(screen,text="Customer Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)


    #------------Making scroll bars to scroll listboxor menu list vertically and horizontally ------------##

    vertical_scrollbar = Scrollbar(screen,)
    vertical_scrollbar.pack(side = RIGHT,fill = Y,pady=350,padx=200)

    horizontal_scrollbar = Scrollbar(screen,orient = HORIZONTAL)
    horizontal_scrollbar.pack(side=BOTTOM,fill=X,pady=100,padx=550)



    ##------------Making Listbox and adding items in it------------##

    listbox = Listbox(screen,bg='lightblue',fg='black',width = 55,height = 18,font=('times',12,'bold'),bd=0,cursor='dot',selectbackground='orange',selectmode = MULTIPLE,yscrollcommand = vertical_scrollbar.set,xscrollcommand = horizontal_scrollbar.set )
    listbox.place(x=700,y=290)

    menu_dictionery ,des_list, menu = get_menu_list(hotel_username+'_menu_list')

    index=listbox_index=length=0

    for i in menu_dictionery:

        #EXAMPLE  ==  listbox.insert(1,'  1.  Manchurian Rice,  Price = 40\- ( per plate )')

        menu_string = '  ' + str(index+1) + '.  ' + str(i) + ',  Price  =  ' + str(menu_dictionery[i]) + ' \-  ' + des_list[index] 
        
        if length < len(menu_string) :
            length = len(menu_string)
            menu_string = menu_string + '     '

        if not menu_string == '  ' + str(index+1) + '.  '  + ',  Price  =  0' + ' \-  ()' :
            listbox.insert(listbox_index,'')
            listbox.insert(listbox_index+1,menu_string)

        index+=1
        listbox_index+=2



    ##------------connecting scroll vars to the menu list/listbox------------##

    vertical_scrollbar.config(command=listbox.yview)
    horizontal_scrollbar.config(command=listbox.xview)


    ##------------to go to next page that is order list page------------##
    def go_to_order_list_page():
        ordered_indexes = listbox.curselection()
        ordered_list = {}
        for index in ordered_indexes:
            if index %2==0:
                continue
            signal=0
            food_name = middle =''
            for character in listbox.get(index):

                if character >= 'A' and character <= 'Z' or character >= 'a' and character <= 'z' :
                    if signal == 2:
                        food_name = food_name + middle
                        middle = ''
                    food_name = food_name + character
                    signal=1
                    
                elif not food_name == '' and character==' ':
                    signal=2
                    middle = middle + character

                elif signal == 1:
                    break

            ordered_list[food_name] = menu_dictionery[food_name]
        
        if ordered_list != {}:
            
            vertical_scrollbar.destroy()
            horizontal_scrollbar.destroy()
            if(order_list_page(screen,hotel_username, table_number, customer_name, ordered_list,reset=True)):
                menu_list_page(None,hotel_username,table_number,customer_name)
            else:
                nonlocal restore_previous_screen
                restore_previous_screen = False
   
    ##------------END of this Function------------##



    ##------------Exit and goto order list buttons------------##

    Button(screen,text="Go to Order List",fg="green",bg="white",font=("times",15),command = go_to_order_list_page).place(x=1080,y=650)

    Button(screen,text="Back",bg='white',fg='red',font=('times',15),width=8,command=screen.destroy).place(x=590,y=650)

    
    ##------------Guidance to the customers------------##
    
    messagebox.showinfo("Guide to Customer","Just Click on the Food Items that you Wish to Order!!!")


    screen.mainloop()

    return restore_previous_screen

##------------END of this Function------------##
