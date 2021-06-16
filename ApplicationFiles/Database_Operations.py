import sqlite3


def ask_query(sql_query):

    try:
        database_connection_object = sqlite3.connect("ApplicationFiles/Application_DataBase.db")
        query_result = database_connection_object.execute(sql_query)
        database_connection_object.commit()
    except:
        return (),False

    
    return query_result,True




def create_necessary_tables(hotel_username):
    
    query = f"CREATE TABLE {hotel_username}_menu_list ( FoodName text, FoodPrice int, FoodDescription text, FoodId INTEGER PRIMARY KEY AUTOINCREMENT )"
    ask_query(query)
    
    query = f"CREATE TABLE {hotel_username}_new_orders ( Date text, TableNo int, CustomerName text, TotalAmount int, OrderList text, PriceList text, QtyList text )"
    ask_query(query)

    query = f"CREATE TABLE {hotel_username}_new_transactions ( Date text, TableNo int, CustomerName text, TotalAmount int, OrderList text, PriceList text, QtyList text )"
    ask_query(query)

    query = f"CREATE TABLE {hotel_username}_permanent_file ( Date text, TableNo int, CustomerName text, TotalAmount int, OrderList text, PriceList text, QtyList text )"
    ask_query(query)

    return 