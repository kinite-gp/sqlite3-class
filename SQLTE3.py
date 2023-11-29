import sqlite3

class Connector:
    def __init__(self, database) -> None:
        """
        Constructor for the Connector class.

        Parameters:
        - database (str): The path to the SQLite database file.
        """

        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self) -> bool:
        """
        Connect to the SQLite database.

        Returns:
        - bool: True if the connection is successful, False otherwise.
        """
        
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            return True
        except sqlite3.Error as e:
            # Print the error message if connection fails.
            print(e)
            return False
        
    def disconnect(self) -> bool:
        """
        Disconnect from the SQLite database.

        Returns:
        - bool: True if the disconnection is successful, False otherwise.
        """
        
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None
            return True
        else:
            return False
        
    def select(self,table, items,where=None):
        """
        Execute a SELECT query on the SQLite database.

        Parameters:
        - table (str): The name of the table to select from.
        - items (str): The columns to select.
        - where (str, optional): The WHERE clause of the query.

        Returns:
        - None
        """
        
        if not self.connection:
            return
        
        _sql = f"select {items} from {table}"
        if where is not None:
            _sql += f" WHERE {where}"
        _sql += ";"

        self.cursor.execute(_sql)

    def insert(self,table,items,values):
        """
        Execute an INSERT query on the SQLite database.

        Parameters:
        - table (str): The name of the table to insert into.
        - items (str): The columns to insert data into.
        - values (str): The values to insert into the specified columns.

        Returns:
        - None
        """

        if not self.connection:
            return

        _sql = f"insert into {table} {items} values {values};"
        self.cursor.execute(_sql)
        self.connection.commit()

    def fetch_one(self):
        """
        Fetch a single row from the result of a query.

        Returns:
        - tuple: A tuple containing a boolean indicating success (True/False) and the fetched row.
        """

        try:
            row = self.cursor.fetchone()
            return (True, row)
        except sqlite3.Error as e:
            # Print the error message if connection fails.
            print(e)
            return (False,)
        
    def fetch_all(self):
        """
        Fetch all rows from the result of a query.

        Returns:
        - tuple: A tuple containing a boolean indicating success (True/False) and the fetched rows.
        """
        
        try:
            rows = self.cursor.fetchall()
            return (True, rows)
        except sqlite3.Error as e:
            # Print the error message if connection fails.
            print(e)
            return (False,)
    