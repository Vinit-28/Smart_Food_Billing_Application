from os import stat, statvfs
from tkinter import *
from ApplicationFiles.append_menu_list import * 
import ApplicationFiles.new_orders_pannel
import ApplicationFiles.menu_list_page 



##-----------------Function to remove Menu-----------------##
def remove_menu(tablename, menu_id):

    query = f"DELETE FROM {tablename} WHERE FoodId = {menu_id};"

    ask_query(query)

##-----------------END of this Function-----------------##



##-----------------new orders page-----------------##
def menu_list_pannel(screen,tablename):
    
    ##-----------------Create Window if Not Available-----------------##
    if screen == None:
        screen = Tk()
        screen.geometry('1920x1080')
        screen.title("Smart Food Application")
        Label(screen,text="Digital  Restro",font = ("Comic Sans MS",30,"bold","roman"),fg='purple',width=28,height=2,).place(x=650,y=50)



    ##-----------------Labels and box creations-----------------##

    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)
    
    Label(screen,text="Menu List Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)


    ##-----------------creating scrollbar-----------------##
    vertical_scrollbar = Scrollbar(screen,)
    vertical_scrollbar.pack(side = RIGHT,fill = Y,pady=350,padx=200)

    horizontal_scrollbar = Scrollbar(screen,orient = HORIZONTAL)
    horizontal_scrollbar.pack(side=BOTTOM,fill=X,pady=100,padx=550)

  

    ##-----------------creating Listbox or list of orders-----------------##
    listbox = Listbox(screen,bg='white',fg='black',height=18,width=65,font=('times',11,'bold'),cursor='dot',selectbackground='orange',xscrollcommand=horizontal_scrollbar.set,yscrollcommand=vertical_scrollbar.set)
    listbox.place(x=690,y=290)

    
     ##-----------------Getting menu list from text file-----------------##
    menu_dictionery ,des_list,menu = ApplicationFiles.menu_list_page.get_menu_list(tablename)


    ##-----------------function to call append_or_edit function-----------------##
    def call_and_destroyer(signal):
        
        if signal == 'E' or signal == 'R':
            
            selected_item = listbox.curselection()
            if selected_item[0] %2 !=0:

                index=selected_item[0]//2
                
                if signal == 'E':

                    vertical_scrollbar.destroy()
                    horizontal_scrollbar.destroy()
                    append_or_edit(screen,tablename,'E',menu[index])
                else:

                    listbox.delete(selected_item[0])
                    listbox.delete(selected_item[0]-1)
                    remove_menu(tablename,menu[index][3])
                    messagebox.showinfo("Success","Food Item Deleted Successfully!!!")
                    vertical_scrollbar.destroy()
                    horizontal_scrollbar.destroy()
                    menu_list_pannel(screen,tablename)
                    return

        elif signal == 'A':

            vertical_scrollbar.destroy()
            horizontal_scrollbar.destroy()

            if menu == []:
                append_or_edit(screen,tablename,signal,[],TRUE)
            else:
                append_or_edit(screen,tablename,signal,[],False)
     
        
        menu_list_pannel(None,tablename)



    ##-----------------Button creations-----------------##
    Button(screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=screen.destroy).place(x=590,y=650)

    Button(screen,text='Add More',fg='green',bg='white',width=9,font=('calibri',9,'bold'),command =lambda: call_and_destroyer('A')).place(x=1050,y=600)


    if menu != []:
        Button(screen,text='Edit',fg='green',bg='white',width=7,font=('calibri',9,'bold'),command = lambda: call_and_destroyer('E')).place(x=690,y=600)
    
        Button(screen,text='Remove',fg='green',bg='white',width=7,font=('calibri',9,'bold'),command = lambda:call_and_destroyer('R')).place(x=870,y=600)

    else:

        Button(screen,text='Edit',fg='green',bg='white',width=7,font=('calibri',9,'bold'),state=DISABLED).place(x=690,y=600)
    
        Button(screen,text='Remove',fg='green',bg='white',width=7,font=('calibri',9,'bold'),state=DISABLED).place(x=870,y=600)
    

   

    index=listbox_index=length=0

    for i in menu_dictionery:

        #EXAMPLE  ==  listbox.insert(1,'  1.  Manchurian Rice,  Price = 40\- ( per plate )')

        menu_string = '  ' + str(index+1) + '.  ' + str(i) + ',  Price  =  ' + str(menu_dictionery[i]) + ' \-  ' + des_list[index] + '   '

        if not menu_string == '  ' + str(index+1) + '.  '  + ',  Price  =  0' + ' \-  ()   ' :
            listbox.insert(listbox_index,'')
            listbox.insert(listbox_index+1,menu_string)

        index+=1
        listbox_index+=2

    ##------------END of this section------------##



    ##-----------------connecting scroll bar to the listbox-----------------##
    vertical_scrollbar.config(command=listbox.yview)
    horizontal_scrollbar.config(command=listbox.xview)
    
    screen.mainloop()

##-----------------END of this function-----------------##
