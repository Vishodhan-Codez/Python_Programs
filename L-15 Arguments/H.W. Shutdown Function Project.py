def shutdown(input_value):
    if input_value == "Yes":
        return "Shutting down..."
    elif input_value == "No":
        return "Abort shutdown."
    else:
        return "Please enter a valid value. "
user_input = input("Enter Yes to shut down, No to abort: ")
print(shutdown(user_input))
