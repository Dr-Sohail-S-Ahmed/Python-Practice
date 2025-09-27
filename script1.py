def greet_person(name):
    print(f"Hello, {name}!")        # This doesn't print anything as a part of the string isn't defined inside the
                                    # curly brackets '{}' & also that it's part of a code block of which the defined
                                    # function isn't called upon yet

if __name__ == "__main__":
    print("Running the script directly.")
    greet_person("Sohail")      # Here 'print' can also be used but the result will also display 'None' denoting
                                # that 'greet_person' doesn't have 'return' statement
# When this file is run directly, '__name__' is defined as '__main__' by default therefore 'if' code block is executed
# but when this file is imported as a module from another file/script, 'else' block is executed
else:
    print("Module imported successfully.")