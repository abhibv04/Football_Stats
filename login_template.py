import streamlit as st
import mysql.connector

# Function to authenticate user from MySQL database
import streamlit as st
import mysql.connector
import pandas as pd
import xml.etree.ElementTree as ET
def login_success(mydb):
    
   

    def reading(table,file):
        xml_tree=ET.parse(file+".xml")
        xml_root=xml_tree.getroot()
        for child_element in xml_root:
            data=()
            for sub_child_element in child_element:
                data+=(sub_child_element.text,)
            inserting(table,str(data))


    cursor = mydb.cursor()
    def inserting(table_name,values):
        insert_query = f"""
        INSERT INTO {table_name}  
        VALUES {values}
        """
        print(insert_query)
        cursor.execute(insert_query)
        mydb.commit()
        


    def update_books(table,book_id, new_quantity):    #update tables
        update_assits = """                              
        UPDATE assists
        SET P_Name = %s
        WHERE SL_No = %s
        """
        update_cleansheets = """                              
        UPDATE clean_sheets
        SET P_Name = %s
        WHERE SL_No = %s
        """
        update_goals = """                              
        UPDATE goals
        SET P_Name = %s
        WHERE SL_No = %s
        """
        update_inter_club_tour_stats = """                              
        UPDATE inter_club_tour_stats
        SET Player = %s
        WHERE SL_No = %s
        """
        update_inter_stats = """                              
        UPDATE inter_stats
        SET P_Name = %s
        WHERE SL_No = %s
        """
        
    

        if table=="assists":

            cursor.execute(update_assits, (new_quantity, book_id))
        if table=="clean_sheets":

            cursor.execute(update_cleansheets, (new_quantity, book_id))
        if table=="goals":

            cursor.execute(update_goals, (new_quantity, book_id))
        
        if table=="inter_club_tour_stats":

            cursor.execute(update_inter_club_tour_stats, (new_quantity, book_id))
        if table=="inter_stats":

            cursor.execute(update_inter_stats, (new_quantity, book_id))
    
        
        
        
        mydb.commit()

    def veiwall(table_name):
        cursor.execute(f"SELECT * FROM {table_name}")
        
        result = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=column_names)
        st.write(df)
        

    def delete_books(book_id,table):
        delete_assists = """
        DELETE FROM assists
        WHERE SL_No = %s
        """
        delete_goals = """
        DELETE FROM goals
        WHERE SL_No = %s
        """
        delete_cleansheets = """
        DELETE FROM clean_sheets
        WHERE SL_No = %s
        """
        delete_inter_club_tour_stats = """
        DELETE FROM inter_club_tour_stats
        WHERE SL_No = %s
        """
        delete_inter_stats = """
        DELETE FROM inter_stats
        WHERE SL_No = %s
        """
        delete_points_table = """
        DELETE FROM points_table
        WHERE SL_No = %s
        """
        if table=="goals":
            cursor.execute(delete_goals, (book_id,))
        if table=="assists":
            cursor.execute(delete_assists, (book_id,))
        if table=="points_table":
            cursor.execute(delete_points_table, (book_id,))
        if table=="clean_sheets":
            cursor.execute(delete_cleansheets, (book_id,))
        if table=="inter_club_tour_stats":
            cursor.execute(delete_inter_club_tour_stats, (book_id,))
        if table=="inter_stats":
            cursor.execute(delete_inter_stats, (book_id,))
        
        mydb.commit()

    def insertstats(pname, position, age, mp, goals, assists, tackles, shots_bl, kp, val, nationality, club):
        inserting_query = """
        INSERT INTO player_stats 
        (P_Name, Position, Age, Matches_Played, Goals, Assists, Tackles_Won, Shots_Blocked, Key_Passes, Value, Nationality, Club_Name) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(inserting_query, (pname, position, age, mp, goals, assists, tackles, shots_bl, kp, val, nationality, club))
        mydb.commit()
        

    def making_text_bar():
        options = ['select...','update', 'insert', 'delete', 'view']
        choice = st.selectbox('Choose an option', options)
        if choice == 'insert':
            
            pname=st.text_input("Enter the player name to update")
            position=st.text_input("Enter Position")
            age=st.text_input("Enter Age")
            mp=st.text_input("Enter MP")
            goals=st.text_input("Enter Goals")
            assists=st.text_input("Enter Assists")
            tackles=st.text_input("Enter Tackles Won")
            shots_bl=st.text_input("Enter Shots blocked")
            kp=st.text_input("Enter Key passes")
            val=st.text_input("Enter Value")
            nationality=st.text_input("Enter Nationality")
            club=st.text_input("Enter Club_Name")
            
            if st.button('Insert table'):
                st.write("Insertion Done") 
                insertstats(pname,position,age,mp,goals,assists,tackles,shots_bl,kp,val,nationality,club)

        
        elif choice == 'view':
            st.write('assists')   
            veiwall(str("assists"))
            st.write('goals')
            veiwall(str("goals"))
            st.write('clean_sheets')
            veiwall(str("clean_sheets"))
            st.write('inter_club_tour_stats')
            veiwall(str(" inter_club_tour_stats"))
            st.write('inter_stats')
            veiwall(str("inter_stats"))
            st.write('manager')
            veiwall(str("manager"))
            st.write('player_stats')
            veiwall(str("player_stats"))
            st.write('points_table')
            veiwall(str("points_table"))

            
        elif choice == 'update':
            table=st.text_input("Enter the table name to update")
            book_id = st.text_input("Enter the ID of the book to update")
            new_price = st.text_input("Enter the P_Name")
            if st.button('Update table'):
                update_books(table,book_id,new_price)
        elif choice == 'delete':
            table=st.text_input("Enter table name")
            book_id = st.text_input("Enter the ID of the cart to delete")
            if st.button('Delete table'):
                delete_books(book_id,table)
        


    st.title('FootStats')

    making_text_bar()

    cursor.close()

    #mydb.close()
def authenticate(username, password):
    try:
        # Establish MySQL connection (replace with your connection details)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abhi@0405",
            database="football_stats1"
            
        )

        cursor = mydb.cursor()

        # Query to check user credentials in the database
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        cursor.close()
        #mydb.close()

        if user:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        st.error(f"Failed to connect to database: {error}")
        return False

def main():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abhi@0405",
            database="football_stats1"
            
        )
    st.title('Login to FootStats')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if authenticate(username, password):
            st.success(f'Logged in as {username}')
            login_success(mydb)
            # Add further functionality after successful login, e.g., redirect to another page
        else:
            st.error('Invalid credentials. Please try again.')

if __name__ == '__main__':
    main()
