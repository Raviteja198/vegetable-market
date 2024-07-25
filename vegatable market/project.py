import mysql.connector as db

con=db.connect(user='root',password='Mysql@021',host='localhost',database='market')
cur=con.cursor()
cur.execute('select * from market.vegetables')
data=cur.fetchall()
amt=0
total_amt=0
profit=0
total_profit=0
while True:
    
    print('1.owner')
    print('2.customer')
    ch=int(input('choose one option :'))
    if ch==1:
        print('1.Add Items')
        print('2.show updated vegetables table')
        print('3.profit')
        print('4.customer Details')
        print('5.close the shop')
        op=int(input('choose one option  :'))
        if op==1:
            V_name=input("Enter the vegetable name you want to add in the table :")
            V_price=(input("Enter the price of the item :"))
            V_quantity=input("Enter the quantity u have :")
            V_purchased_price=int(V_price)-10
            
            adding_items='''insert into Vegetables (veg_Name,Price,quantity,purchased_price) values (%s,%s,%s,%s)'''
            
            try:
                cur.execute(adding_items,(V_name,V_price,V_quantity,V_purchased_price))
                con.commit()
                print("Item  details have been saved successfully.")
            except db.Error as err:
                print(f"Error: {err}")
                con.rollback()
        elif op==2:
            cur1=con.cursor()
            cur1.execute('select * from market.vegetables')
            updated_data=cur1.fetchall()
            print('\n\t','*'*10,'Updated Vegetables Table','*'*10)
            print()
            print("*"*50)
            headers = ["Vegetables", "price", "Quantity"]
            widths = [max(len(v[0]) for v in data) + 2, 7, 10]
            # print('\t','Vegetables \t','price \t\t',"Quantity \t")
            print(f"{headers[0]:<{widths[0]}}\t{headers[1]:<{widths[1]}}\t\t{headers[2]:<{widths[2]}} ")
            print("*"*50)
            for rows in updated_data:
                # print('\t',rows[0],'            ',rows[1],'          ',rows[2])
                print(f"{rows[0]:<{widths[0]}}\t{rows[1]:<{widths[1]}}\t\t{rows[2]:<{widths[2]}}Kgs")
            print("*" * 50)
            cur1.close()
        elif op==3:
            print()
            print("*"*10,'profit',"*"*10)
            print()
            print("*" * 25)
            print('The profit you Earned is ',total_profit,'Rs')
            print("*" * 25)
        elif op==4:
            cur2=con.cursor()
            cur2.execute('select * from market.Customer_Details')
            data2=cur2.fetchall()
            headers = ["Name", "Phne Number", "Location"]
            widths = [max(len(v[0]) for v in data2) + 2, 7, 10]
            print("*" * 50)
            print(f"{headers[0]:<{widths[0]}}\t{headers[1]:<{widths[1]}}\t\t{headers[2]:<{widths[2]}} ")
            print("*" * 50)
            for row in data2:
                 print(f"{row[0]:<{widths[0]}}\t{row[1]:<{widths[1]}}\t\t{row[2]:<{widths[2]}}")
            print("*" * 50)
            cur2.close()
        elif op==5:
            print('The shop is closing')
            break
    elif ch==2:
        
    # conn2=db.connect(user='root',password='Mysql@021',host='localhost'database='customer details')
        C_name=input("Enter your name  please :")
        C_phn_nbr=(input("Enter the phne nbr :"))
        C_location=input("Enter the location :")
        if int(len(C_phn_nbr))==10:
            store_details='''insert into Customer_Details (Name,phn_nbr,Location) values (%s,%s,%s)'''
            try:
                cur.execute(store_details,(C_name,C_phn_nbr,C_location))
                con.commit()
                print("Customer details have been saved successfully.")
            except db.Error as err:
                print(f"Error: {err}")
                con.rollback()
        else:
            print("Enter a valid phone nbr")
            break
        # cur=con.cursor()
        # cur.execute('select * from market.vegetables')

        # cur2=con.cursor()
        # cur2.execute('select * from market.Customer_Details')
        # data=cur.fetchall()
        vegetable_quantities = {rows[0]: rows[2] for rows in data}

        print('\t','*'*10,'The Items avaliable in the Shop are','*'*10)
        # print('*'*50)
        headers = ["Vegetables", "price", "Quantity"]
        widths = [max(len(v[0]) for v in data) + 2, 7, 10]
        # print('vegtables \t \t','price \t\t','quantity','Kgs')
        print("*" * 50)
        print(f"{headers[0]:<{widths[0]}}\t{headers[1]:<{widths[1]}}\t\t{headers[2]:<{widths[2]}} ")
        print("*" * 50)
        # print('*'*50)
        # amt=0
        # total_amt=0
        # profit=0
        # total_profit=0
        for rows in data:
            # print(rows[0],'     ',rows[1],'     ',rows[2],'Kgs')
            print(f"{rows[0]:<{widths[0]}}\t{rows[1]:<{widths[1]}}\t\t{rows[2]:<{widths[2]}}Kgs")
        print("*" * 50)

        query='SElECT item_check(%s)'
        while True:
            veg_name=input("Enter the Vegetable you want :")
            cur.execute(query,(veg_name,))
            result=cur.fetchone()
            # print(result)
            if result:
                output = result[0]
                # print(output)
            else:
                print('Item_not_avaliable')
                continue

            if output=='True':
                qty=float(input("Enter how much quantity you want :"))
                query1='SElECT Quantity(%s,%s)'
                item=veg_name
                cur.execute(query1,(item,qty,))
                res=cur.fetchone()
                if res:
                    output1 = res[0]
                else:
                    print('Enterd_quantity_is_not_avaliable')
                    continue
            
                
                if output1=='True':
                    for i in data:
                        if i[0]==veg_name:
                            amt=i[1]*qty
                            profit=(i[1]-i[3])*qty
                            total_amt+=amt
                            total_profit+=profit
                            # t_profit=total_profit
                        
                        
                            new_quantity = i[2] - qty
                            update_query = 'UPDATE Vegetables SET quantity = %s WHERE veg_name = %s'
                            cur.execute(update_query, (new_quantity, veg_name))
                            con.commit()
                            print(f"Updated quantity of {veg_name} to {new_quantity} kg")
                else:
                    print('Entered quantity is not available')
            else:
                print('Item is not avaliable')
                
            ch=input("Do you want more items yes/no :")
            if ch=='no':
                print('\n\t\t ----Your Bill----')
                print('*'*50)
                print('please pay the total amount of :',total_amt,'Rs')
                print('*'*50)
                amount_paid = float(input("\nEnter amount paid by the customer : Rs "))
                if amount_paid >= total_amt:
                    change = amount_paid - total_amt
                    print()
                    print(f"Change: ",change)
                    print("Thank you for shopping with us!")
                    print("Have A NICE DAY")
                    break
                else:
                    print("You paid less amont please pay the total amount ")
                    break
        
        for veg_name, new_quantity in vegetable_quantities.items():
            update_query = 'UPDATE Vegetables SET quantity = %s WHERE veg_name = %s'
            cur.execute(update_query, (new_quantity, veg_name))
            con.commit()
                        
                    
                
                
        # print(total_amt)
            # c=input('Do you want close the shop(yes/no):')
            # if c!='yes' and c!='no':
            #     print("Enter the correct option")
            # if c=='yes':
            #     print('closing the shop')
            #     print('\t\t','*'*10,'Report','*'*10)
            #     # print('*'*50)
            #     # print('vegtables \t', 'quantity \t','kgs \t')
            #     # print('*'*50)
            
            #     # break
            #     cur.execute('select * from market.vegetables')
            #     updated_data=cur.fetchall()
            #     print('\n\t','*'*10,'Updated Vegetables Table','*'*10)
            #     print()
            #     print("*"*50)
            #     headers = ["Vegetables", "price", "Quantity"]
            #     widths = [max(len(v[0]) for v in data) + 2, 7, 10]
            #     # print('\t','Vegetables \t','price \t\t',"Quantity \t")
            #     print(f"{headers[0]:<{widths[0]}}\t{headers[1]:<{widths[1]}}\t\t{headers[2]:<{widths[2]}} ")
            #     print("*"*50)
            #     for rows in updated_data:
            #         # print('\t',rows[0],'            ',rows[1],'          ',rows[2])
            #         print(f"{rows[0]:<{widths[0]}}\t{rows[1]:<{widths[1]}}\t\t{rows[2]:<{widths[2]}}Kgs")
            #     print("*" * 50)
                    
                
            #     print()
            #     print("*"*10,'profit',"*"*10)
            #     print()
            #     print("*" * 25)
            #     print('The profit you Earned is ',total_profit,'Rs')
            #     print("*" * 25)
            #     break  
                
                
        # for veg_name, new_quantity in vegetable_quantities.items():
        #     update_query = 'UPDATE Vegetables SET quantity = %s WHERE veg_name = %s'
        #     cur.execute(update_query, (new_quantity, veg_name))
        #     con.commit()
        #     break

        cur.close()
        con.close()
    else:
        print("Enter the correct option , please")























    # query2 = "SELECT get_Price(%s)"
    # item=veg_name
    # print(item)
    # cur.execute(query2, (item,))
    # result=cur.fetchone()
    # print(result)
    # if result:
    #     price = result[0]
    # else:
    #     # price = None
    #     pass

# print(price)
# print(type(price))
# print(amt)

# cur.close()
# con.close()

# import mysql.connector

# def call_item_check(veg_name):
#     try:
#         # Establish a c-onnection to the MySQL database
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Mysql@021",
#             database="market"
#         )
#         cursor = conn.cursor()

#         # Prepare the SQL query to call the item_check function
#         query = "SELECT item_check(%s)"
#         cursor.execute(query, (veg_name,))

#         # Fetch the result
#         result = cursor.fetchone()

#         # Check if result is not None
#         if result:
#             output = result[0]
#         else:
#             output = None

#         # Close the cursor and connection
#         cursor.close()
#         conn.close()

#         return output

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return None

# def call_quantity_check(veg_name, num):
#     try:
#         # Establish a connection to the MySQL database
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Mysql@021",
#             database="market"
#         )
#         cursor = conn.cursor()

#         # Prepare the SQL query to call the Quantity function
#         query = "SELECT Quantity(%s, %s)"
#         cursor.execute(query, (veg_name, num))

#         # Fetch the result
#         result = cursor.fetchone()

#         # Check if result is not None
#         if result:
#             output = result[0]
#         else:
#             output = None

#         # Close the cursor and connection
#         cursor.close()
#         conn.close()

#         return output

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return None

# # Example usage
# veg_name = 'tomato'
# quantity = 12

# # Call item_check function
# item_check_output = call_item_check(veg_name)
# print(f"Item check for '{veg_name}': {item_check_output}")

# # Call Quantity function
# quantity_check_output = call_quantity_check(veg_name, quantity)
# print(f"Quantity check for '{veg_name}' with quantity {quantity}: {quantity_check_output}")

