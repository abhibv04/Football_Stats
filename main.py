import pandas as pd
import mysql.connector

# Define your database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Abhi@0405",
    "database": "Football_Stats1"
}

# Read the CSV file for points_table and transform the data
df_points = pd.read_csv("DB-Proj/csv_to_database/csv_to_database/filtered_points_table.csv"
    , encoding='utf-8')
df_points.fillna(0, inplace=True)
df_points = df_points.rename(
    columns={'Squad': 'Club_Name', 'Notes': 'Status'})

# Add an SL No column to the DataFrame
df_points['SL_No'] = range(1, len(df_points) + 1)

# Reorder columns to have 'SL_No' as the first column
columns_to_insert = ['SL_No', 'Club_Name', 'MP', 'W', 'D', 'L', 'GF',
                     'GA', 'GD', 'Pts', 'Top Team Scorer', 'Goalkeeper', 'Status']
df_points = df_points[columns_to_insert]

# Read the CSV file for player_stats and transform the data
# df_players = pd.read_csv('/Users/prathamshetty/Desktop/Sem 5/DBMS/Football Stats Project/csv_to_database/filtered_player_stats.csv',
#                          encoding='ISO-8859-1')

df_players = pd.read_csv("DB-Proj/csv_to_database/csv_to_database/filtered_player_stats_2.csv",
                         encoding='utf-8')
df_players.fillna(0, inplace=True)

# Rename the 'Team' column to 'Club_Name'
df_players.rename(columns={'Team': 'Club_Name'}, inplace=True)

# Select the columns you want from the CSV file and reorder them
selected_columns = [
    'Player_Name', 'Position_y', 'Age', 'Matches Played', 'Goals',
    'Assists', 'Tackles Won', 'Shots Blocked', 'Key Passes', 'Value', 'Nationality', 'Club_Name'
]

df_players = df_players[selected_columns]

df_assists=pd.read_csv("DB-Proj/csv_to_database/csv_to_database/Assists.csv",encoding='utf-8',delimiter=';')
df_assists.fillna(0, inplace=True)

# Add an SL No column to the DataFrame
df_assists['SL_No'] = range(1, len(df_assists) + 1)

# Define the list of columns to select from the df_assists DataFrame
selected_columns_1 = ['SL_No','Rank', 'P_Name', 'Assists']

# Filter the df_assists DataFrame to select the specified columns
df_assists = df_assists[selected_columns_1]

# Read the CSV file for Goals and Clean_Sheets
df_goals = pd.read_csv("DB-Proj/csv_to_database/csv_to_database/Goals.csv", encoding='utf-8', delimiter=';')
df_goals.fillna(0, inplace=True)
df_clean_sheets = pd.read_csv("DB-Proj/csv_to_database/csv_to_database/Clean_Sheets.csv", encoding='utf-8', delimiter=';')
df_clean_sheets.fillna(0, inplace=True)

# Add an SL No column to the DataFrames
df_goals['SL_No'] = range(1, len(df_goals) + 1)
df_clean_sheets['SL_No'] = range(1, len(df_clean_sheets) + 1)

# Define the list of columns to select from the Goals and Clean_Sheets DataFrames
selected_columns_goals = ['SL_No', 'Rank', 'P_Name', 'Goals']
selected_columns_clean_sheets = ['SL_No', 'Rank', 'P_Name', 'Clean_Sheets']

# Filter the DataFrames to select the specified columns
df_goals = df_goals[selected_columns_goals]
df_clean_sheets = df_clean_sheets[selected_columns_clean_sheets]

# Read the CSV file for manager_final and transform the data
df_managers = pd.read_csv("DB-Proj/csv_to_database/csv_to_database/updated_manager.csv",encoding='utf-8')
df_managers.fillna(0, inplace=True)

# Read the CSV file for Inter_Stats and transform the data
df_inter_stats = pd.read_csv("DB-Proj/csv_to_database/csv_to_database/Inter_Stats.csv", encoding='utf-8', delimiter=',')
df_inter_stats.fillna(0, inplace=True)

# Add an SL No column to the DataFrame
df_inter_stats['SL_No'] = range(1, len(df_inter_stats) + 1)

# Define the list of columns to select from the df_inter_stats DataFrame
selected_columns_inter_stats = ['SL_No', 'Rank', 'P_Name', 'TEAM', 'Played', 'Stats']

# Filter the df_inter_stats DataFrame to select the specified columns
df_inter_stats = df_inter_stats[selected_columns_inter_stats]

# Read the CSV file for Inter_Club_Tour_Stats and transform the data
df_inter_club_tour_stats = pd.read_csv("DB-Proj/csv_to_database/csv_to_database/Inter_Club_Tour.csv", encoding='utf-8', delimiter=',')
df_inter_club_tour_stats.fillna(0, inplace=True)

# Add an SL No column to the DataFrame
df_inter_club_tour_stats['SL_No'] = range(1, len(df_inter_club_tour_stats) + 1)

# Define the list of columns to select from the df_inter_club_tour_stats DataFrame
selected_columns_inter_club_tour_stats = ['SL_No', 'Rank', 'Player', 'Country', 'Club_Name', 'Goals']

# Filter the df_inter_club_tour_stats DataFrame to select the specified columns
df_inter_club_tour_stats = df_inter_club_tour_stats[selected_columns_inter_club_tour_stats]

try:
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Define the CREATE TABLE query for points_table (if it doesn't exist)
    create_points_table_query = """
    CREATE TABLE IF NOT EXISTS points_table (
        SL_No INT PRIMARY KEY,
        Club_Name VARCHAR(255) UNIQUE,
        MP INT,
        W INT,
        D INT,
        L INT,
        GF INT,
        GA INT,
        GD INT,
        Pts INT,
        `Top Team Scorer` VARCHAR(255),
        Goalkeeper VARCHAR(255),
        `Status` VARCHAR(255)
    );
    """

    # Execute the CREATE TABLE query for points_table
    cursor.execute(create_points_table_query)

    # Define the CREATE TABLE query for player_stats (if it doesn't exist)
    create_player_stats_query = """
    CREATE TABLE IF NOT EXISTS player_stats (
        P_Name VARCHAR(255) PRIMARY KEY,
        Position VARCHAR(255),
        Age INT,
        Matches_Played INT,
        Goals INT,
        Assists INT,
        GA INT,
        Tackles_Won INT,
        Shots_Blocked INT,
        Key_Passes INT,
        Value VARCHAR(255),
        Nationality VARCHAR(255),
        Club_Name VARCHAR(255)
    );
    """

    # Execute the CREATE TABLE query for player_stats
    cursor.execute(create_player_stats_query)

    create_table_assists_query = """
        CREATE TABLE IF NOT EXISTS Assists (
            SL_No INT AUTO_INCREMENT PRIMARY KEY,
            `Rank` INT,
            P_Name VARCHAR(255),
            Assists INT
        )
        """
    cursor.execute(create_table_assists_query)

        # Define the CREATE TABLE query for Goals (if it doesn't exist)
    create_table_goals_query = """
    CREATE TABLE IF NOT EXISTS Goals (
        SL_No INT AUTO_INCREMENT PRIMARY KEY,
        `Rank` INT,
        P_Name VARCHAR(255),
        Goals INT
    );
    """
    
    # Execute the CREATE TABLE query for Goals
    cursor.execute(create_table_goals_query)

    # Define the CREATE TABLE query for Clean_Sheets (if it doesn't exist)
    create_table_clean_sheets_query = """
    CREATE TABLE IF NOT EXISTS Clean_Sheets (
        SL_No INT AUTO_INCREMENT PRIMARY KEY,
        `Rank` INT,
        P_Name VARCHAR(255),
        Clean_Sheets INT
    );
    """
    
    # Execute the CREATE TABLE query for Clean_Sheets
    cursor.execute(create_table_clean_sheets_query)

    create_manager_final_query = """
    CREATE TABLE IF NOT EXISTS manager (
        Club_Name VARCHAR(255) PRIMARY KEY,
        MANAGER VARCHAR(255),
        NATIONALITY VARCHAR(255)
    );
    """

    # Execute the CREATE TABLE query for manager_final
    cursor.execute(create_manager_final_query)

        # Define the CREATE TABLE query for Inter_Stats (if it doesn't exist)
    create_inter_stats_query = """
    CREATE TABLE IF NOT EXISTS Inter_Stats (
        SL_No INT AUTO_INCREMENT PRIMARY KEY,
        `Rank` INT,
        P_Name VARCHAR(255),
        TEAM VARCHAR(255),
        Played INT,
        Stats INT
    );
    """

    # Execute the CREATE TABLE query for Inter_Stats
    cursor.execute(create_inter_stats_query)


    # Define the CREATE TABLE query for Inter_Club_Tour_Stats (if it doesn't exist)
    create_inter_club_tour_stats_query = """
    CREATE TABLE IF NOT EXISTS Inter_Club_Tour_Stats (
        SL_No INT PRIMARY KEY,
        `Rank` INT,
        Player VARCHAR(255),
        Country VARCHAR(255),
        Club_Name VARCHAR(255),
        Goals INT
    );
    """

    # Execute the CREATE TABLE query for Inter_Club_Tour_Stats
    cursor.execute(create_inter_club_tour_stats_query)

    # Commit the changes for both tables' creation
    conn.commit()

    # Define the INSERT INTO query for points_table
    insert_points_query = "INSERT INTO points_table (SL_No, Club_Name, MP, W, D, L, GF, GA, GD, Pts, `Top Team Scorer`, Goalkeeper, `Status`) " \
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Iterate through the DataFrame and insert rows into points_table
    for _, row in df_points.iterrows():
        cursor.execute(insert_points_query, tuple(row))

    # Define the SQL trigger to calculate "G/A" when inserting or updating a row in player_stats
    trigger_query = """
    CREATE TRIGGER CalculateGA
    BEFORE INSERT ON player_stats
    FOR EACH ROW
    BEGIN
        SET NEW.GA = NEW.Goals + NEW.Assists;
    END;
    """

    cursor.execute(trigger_query)

    # Commit the trigger to the database
    conn.commit()

# Define the INSERT INTO query for player_stats
    insert_player_stats_query = "INSERT INTO player_stats (P_Name, Position, Age, Matches_Played, Goals, Assists, Tackles_Won, Shots_Blocked, Key_Passes, Value, Nationality, Club_Name) " \
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Position = VALUES(Position), Age = VALUES(Age), Matches_Played = VALUES(Matches_Played), Goals = VALUES(Goals), Assists = VALUES(Assists), Tackles_Won = VALUES(Tackles_Won), Shots_Blocked = VALUES(Shots_Blocked), Key_Passes = VALUES(Key_Passes), Value = VALUES(Value), Nationality = VALUES(Nationality), Club_Name = VALUES(Club_Name)"

    # Iterate through the DataFrame and insert or update rows into player_stats
    for _, row in df_players.iterrows():
        cursor.execute(insert_player_stats_query, tuple(row))

    insert_assists_query = "INSERT INTO Assists (SL_No, `Rank`, P_Name, Assists) " \
    "VALUES (%s, %s, %s, %s)"

    # Iterate through the DataFrame and insert rows into Assists table
    for _, row in df_assists.iterrows():
        cursor.execute(insert_assists_query, tuple(row))

    # Define the INSERT INTO query for Goals
    insert_goals_query = "INSERT INTO Goals (SL_No, `Rank`, P_Name, Goals) " \
        "VALUES (%s, %s, %s, %s)"
    
    # Iterate through the DataFrame and insert rows into the Goals table
    for _, row in df_goals.iterrows():
        cursor.execute(insert_goals_query, tuple(row))

    # Define the INSERT INTO query for Clean_Sheets
    insert_clean_sheets_query = "INSERT INTO Clean_Sheets (SL_No, `Rank`, P_Name, Clean_Sheets) " \
        "VALUES (%s, %s, %s, %s)"
    
    # Iterate through the DataFrame and insert rows into the Clean_Sheets table
    for _, row in df_clean_sheets.iterrows():
        cursor.execute(insert_clean_sheets_query, tuple(row))

        # Define the INSERT INTO query for manager_final
    insert_manager_final_query = "INSERT INTO manager (Club_Name, MANAGER, NATIONALITY) " \
        "VALUES (%s, %s, %s)"

    # Iterate through the DataFrame and insert rows into manager_final
    for _, row in df_managers.iterrows():
        cursor.execute(insert_manager_final_query, (row['Club_Name'], row['MANAGER'], row['NATIONALITY']))

    
    # Define the INSERT INTO query for Inter_Stats
    insert_inter_stats_query = "INSERT INTO Inter_Stats (SL_No, `Rank`, P_Name, TEAM, Played, Stats) " \
        "VALUES (%s, %s, %s, %s, %s, %s)"

    # Iterate through the DataFrame and insert rows into Inter_Stats
    for _, row in df_inter_stats.iterrows():
        cursor.execute(insert_inter_stats_query, tuple(row))

    # Define the INSERT INTO query for Inter_Club_Tour_Stats
    insert_inter_club_tour_stats_query = "INSERT INTO Inter_Club_Tour_Stats (SL_No, `Rank`, Player, Country, Club_Name, Goals) " \
        "VALUES (%s, %s, %s, %s, %s, %s)"

    # Iterate through the DataFrame and insert rows into Inter_Club_Tour_Stats
    for _, row in df_inter_club_tour_stats.iterrows():
        cursor.execute(insert_inter_club_tour_stats_query, tuple(row))

    # Commit the changes for both tables' data insertion
    conn.commit()

    # Define the ALTER TABLE query to add the foreign key reference to player_stats
    alter_player_stats_query = """
    ALTER TABLE player_stats
    ADD FOREIGN KEY (Club_Name) REFERENCES points_table(Club_Name);
    """

    # Execute the ALTER TABLE query to add the foreign key reference
    cursor.execute(alter_player_stats_query)

    alter_assists_query = """
    ALTER TABLE Assists
    #ADD FOREIGN KEY (P_Name) REFERENCES player_stats(P_Name);
    """

    # Execute the ALTER TABLE query to add the foreign key reference
    cursor.execute(alter_assists_query)

    
    # Define the ALTER TABLE query to add the foreign key reference to Clean_Sheets
    alter_clean_sheets_query = """
    ALTER TABLE Clean_Sheets
    ADD FOREIGN KEY (P_Name) REFERENCES player_stats(P_Name);
    """
    
    # Execute the ALTER TABLE query to add the foreign key reference for Clean_Sheets
    cursor.execute(alter_clean_sheets_query)

    # Define the ALTER TABLE query to add the foreign key reference to points_table
    alter_manager_final_query = """
    ALTER TABLE manager
    ADD FOREIGN KEY (Club_Name) REFERENCES points_table(Club_Name);
    """

    # Execute the ALTER TABLE query to add the foreign key reference
    cursor.execute(alter_manager_final_query)

    # Define the ALTER TABLE query to add the foreign key reference to player_stats
    alter_inter_stats_query = """
    ALTER TABLE Inter_Stats
    ADD FOREIGN KEY (P_Name) REFERENCES player_stats(P_Name);
    """

    # Execute the ALTER TABLE query to add the foreign key reference
    cursor.execute(alter_inter_stats_query)

    # Define the ALTER TABLE query to add the foreign key reference to player_stats
    alter_inter_club_tour_stats_query = """
    ALTER TABLE Inter_Club_Tour_Stats
    ADD FOREIGN KEY (Player) REFERENCES player_stats(P_Name);
    """

    # Execute the ALTER TABLE query to add the foreign key reference
    cursor.execute(alter_inter_club_tour_stats_query)

    alter_inter_club_tour_stats_query="""
    ALTER TABLE Inter_Club_Tour_Stats
    ADD FOREIGN KEY (Club_Name) REFERENCES points_table(Club_Name);
    """

    # Execute the ALTER TABLE query to add the foreign key reference
    
    
    # Commit the changes for adding the foreign key reference
    conn.commit()

except mysql.connector.Error as err:
    print("MySQL Error: {}".format(err))

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()