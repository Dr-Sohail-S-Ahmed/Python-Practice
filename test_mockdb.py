# (Check out "python unit testing.py" first + see also Adv Python in Programming.xlsx)

from mockdb import MockDB  # Import the fake database class from fixtures
import pytest  # Import pytest for testing

# WITHOUT FIXTURE (code repetition) + (select lines 5-30 > Ctrl+/)
# def test_toms_id():  # Test case for Tom's ID
#     db = MockDB()  # Create a mock database instance
#     conn = db.connect("server")  # Connect to the mock database
#     cur = conn.cursor()  # Get a cursor object
#     id = cur.execute("select id from employee_db where name=Tom")  # Run query
#     cur.close()  # Close cursor after test
#     conn.close()  # Close connection after test
#     assert id == 123  # Verify Tom's ID is 123
#
# def test_dicks_id():  # Test case for Dick's ID
#     db = MockDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#     id = cur.execute("select id from employee_db where name=Dick")
#     cur.close()
#     conn.close()
#     assert id == 456  # Verify Dick's ID is 456
#
# def test_harrys_id():  # Test case for Harry's ID
#     db = MockDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#     id = cur.execute("select id from employee_db where name=Harry")
#     cur.close()
#     conn.close()
#     assert id == 789  # Verify Harry's ID is 789


# WITH FIXTURE
@pytest.fixture(scope="module")  # Define a fixture that runs once per module
def cur():  # Fixture function to provide a database cursor
    print("setting up")  # Print message when starting setup
    db = MockDB()  # Create a mock database instance
    conn = db.connect("server")  # Connect to the mock database
    curs = conn.cursor()  # Get a cursor object from the connection
    yield curs  # Provide the cursor to the test functions
    curs.close()  # Close the cursor after tests finish
    conn.close()  # Close the connection after tests finish
    print("closing DB")  # Print message when tearing down


def test_toms_id(cur):  # Test case for Tom's ID
    id = cur.execute("select id from employee_db where name=Tom")  # Run query
    assert id == 123  # Verify Tom's ID is 123


def test_dicks_id(cur):  # Test case for Dick's ID
    id = cur.execute("select id from employee_db where name=Dick")  # Run query
    assert id == 456  # Verify Dick's ID is 456


def test_harrys_id(cur):  # Test case for Harry's ID
    id = cur.execute("select id from employee_db where name=Harry")  # Run query
    assert id == 789  # Verify Harry's ID is 789


"""
This code uses pytest with a fixture to test database queries against a mock database.
- The fixture 'cur' sets up a mock database connection and cursor before tests, 
  and closes them afterward.
- Three tests check that the IDs returned for Tom, Dick, and Harry match expected values.
"""