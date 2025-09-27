# (Check out "python unit testing.py" first + see also Adv Python in Programming.xlsx)

class MockDB:  # A fake database class used for testing
    def __init__(self):  # Initialize the mock database
        self.connection = Connection()  # Create a new connection object

    def connect(self, connection_string):  # Simulate a connection method
        return self.connection  # Always return the same connection


class Connection:  # A fake connection class
    def __init__(self):  # Initialize the connection
        self.cur = Cursor()  # Create a new cursor object

    def cursor(self):  # Simulate cursor creation
        return self.cur  # Return the cursor object

    def close(self):  # Simulate closing the connection
        pass  # Do nothing


class Cursor:  # A fake cursor class
    def execute(self, query):  # Simulate running a query
        if query == "select id from employee_db where name=Tom":  # If query matches Tom
            return 123  # Return mock id
        elif query == "select id from employee_db where name=Dick":  # If query matches Dick
            return 456  # Return mock id
        elif query == "select id from employee_db where name=Harry":  # If query matches Harry
            return 789  # Return mock id
        else:  # For all other queries
            return -1  # Return -1 as "not found"

    def close(self):  # Simulate closing the cursor
        pass  # Do nothing


"""
This code creates a mock database system with three classes:
- MockDB gives a fake database object.
- Connection represents a fake database connection that can return a cursor.
- Cursor simulates query execution, returning hardcoded results for John or Tom, and -1 otherwise.
It is useful for testing without needing a real database.
"""