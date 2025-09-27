# (For basic concepts, see Adv Python in Programming.xlsx)

# "test_" prefix is used before the file name which is used for testing the Python program
# Similarly, "test_" prefix is also used before function names which are to be tested
# (see files: mathlib.py & test_mathlib.py
# To test: A. Cmd > pytest -m pytest {OR} py.test
              # (both these checks for all files with prefix "test_" & tests all functions with the same prefix)
         # B. Cmd > (go to folder containing "test_" prefix file) > py.test -v
              # "v" stands for verbose which mentions individual file names alongwith whether they passed or failed
# To skip testing a specific funtion, place "@pytest.mark.skip" above it > Run test file thru cmd
    # "pytest -v -rxs" gives
# To skip when certain condition is met: @pytest.mark.skipif(sys.version_info > 3,5)
    # Here condition is taken to be Python version > 3.5 but the condition can be something else also
# To run tests with specific word in their names, run in cmd > pytest -k multiply {OR} pytest -k multiply -v
    # Here "multiply" is the word that's searched before running the test
# To tag tests: @pytest.mark.windows (where "windows" is the custom user defined name)
# To run tests while avoiding the ones with specific word in their names: run in cmd > pytest -m "not windows" -v
    # Here "windows" is in double quotes with "not" where "not" in compulsory while next word may be user defined


# (see files: mockdb.py & 