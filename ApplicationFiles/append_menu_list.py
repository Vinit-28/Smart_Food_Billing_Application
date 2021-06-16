from tkinter import * 
from tkinter import messagebox
import os
from ApplicationFiles.Database_Operations import ask_query


##-----------------checking whether the entered food name exists or not-----------------##
def is_food_name_exists(tablename,food_name):
    
    query = f"SELECT * FROM {tablename} WHERE FoodName = '{food_name}';"

    query_result, is_successfull = ask_query(query)

    if is_successfull:
        return len(query_result.fetchall())

    return 0

##-----------------END of this function-----------------##



##-----------------new orders page-----------------##
def append_or_edit(screen,tablename,signal,menu,is_this_fisrt_menu=False):


    ##-----------------Labels and box creations-----------------##
    Canvas(screen,bg='lightgray',width=700,height=500).place(x=570,y=200)
    
    Label(screen,text="Add Item Pannel",bg='lightgray',fg='blue',font=("arial",15,"bold")).place(x=820,y=230)

    
    ##-----------------asking questions-----------------##

    Label(screen,text='Enter Food Name : ',bg='lightgray',font=('arial',14,'bold')).place(x=670,y=360)

    Label(screen,text='Enter Price : ',bg='lightgray',font=('arial',14,'bold')).place(x=670,y=430)

    Label(screen,text='Enter Description : ',bg='lightgray',font=('arial',14,'bold')).place(x=670,y=500)


    ##-----------------answering variables-----------------##
    food_name=StringVar()
    price = StringVar()
    description = StringVar()

    ##-----------------checking if aim is to edit current detaila-----------------##
    if signal == 'E':
        food_name_edit,price_edit,description_edit = menu[0],str(menu[1]),menu[2]
    
            

    ##-----------------answering boxes-----------------##
    ans_1 = Entry(screen,textvariable = food_name,width=18,font=('roman',12,))
    ans_1.place(x=950,y=360)

    ans_2 = Entry(screen,textvariable = price,width=18,font=('roman',12,))
    ans_2.place(x=950,y=430)

    ans_3 = Entry(screen,textvariable = description,width=18,font=('roman',12,))
    ans_3.place(x=950,y=500)


    ##-----------------displaying details if aim is to edit current details-----------------##
    if signal == 'E':
        ans_1.insert(END,food_name_edit)
        ans_2.insert(END,price_edit)
        ans_3.insert(END,description_edit)



    ##-----------------if "done" button pressed-----------------##
    def success():
        if food_name.get() == "" or price.get() == "" or description.get() == "" :
            messagebox.showerror("Input Issue","All Fields are Required to be Filled")

        elif signal != "E" and  is_food_name_exists(tablename,food_name.get()):
            messagebox.showerror("Food Item Issue","Food Item Already Exists")

        else:
            # string = food_name.get() + '\t' + price.get() + '\t' + description.get() + '\n'
            
            if signal == 'E':

                query = f"UPDATE {tablename} SET FoodName = '{food_name.get()}', FoodPrice = {int(price.get())}, FoodDescription = '{description.get()}' WHERE FoodId = {menu[3]}; "
                
                ask_query(query)

                messagebox.showinfo("Success","Food item Edited successfully")

            else: 
                
                if is_this_fisrt_menu:

                    query = f"INSERT INTO {tablename} (FoodName, FoodPrice, FoodDescription, FoodId) VALUES ( '{food_name.get()}', {int(price.get())}, '{description.get()}', 101 ) ;"

                else:
                    query = f"INSERT INTO {tablename} (FoodName, FoodPrice, FoodDescription) VALUES ( '{food_name.get()}', {int(price.get())}, '{description.get()}') ;"

                ask_query(query)

            
                messagebox.showinfo("Success","Food item saved successfully")

            screen.destroy()

    ##-----------------END of this function-----------------##


    ##-----------------creating buttons-----------------##
    Button(screen,text='Save',fg='green',bg='white',width=12,font=('times',12,'bold'),command = success).place(x=850,y=580)

    Button(screen,text="Back",bg='white',fg='red',font=('times',13),width=8,command=screen.destroy).place(x=590,y=650)


    screen.mainloop()

##-----------------END of this function-----------------##
