# Muhammad Usman  Reg# 200901104  Assign_04 OS   BS-CS-01-A
import threading  # thread lib to use threads

# Global variable to store the input string
input_string = ""


def input_thread():  # input thread function
    global input_string
    try:  # Handle any exceptions that occur while getting input
        # Get input from the user
        input_string = input("Enter a string: ")
    except Exception as e:

        print("an error occurred in input thread:", e)


def reverse_thread():  # reverse thread function
    global input_string
    # Reverse the input string
    reversed_string = input_string[::-1]
    print("Reversed string:", reversed_string)


def capital_thread():  # capital thread function
    global input_string
    # Capitalize the input string
    capitalized_string = input_string.upper()
    print("Capitalized string:", capitalized_string)


def shift_thread():  # shift thread function
    global input_string
    # Shift each character in the input string by two
    shifted_string = ""
    for ch in input_string:
        shifted_ch = chr((ord(ch) - ord('a') + 2) % 26 + ord('a'))
        shifted_string += shifted_ch
    print("Shifted string:", shifted_string)


if __name__ == "__main__":  # main body
    # Create the four threads
    input_t = threading.Thread(target=input_thread)
    reverse_t = threading.Thread(target=reverse_thread)
    capital_t = threading.Thread(target=capital_thread)
    shift_t = threading.Thread(target=shift_thread)

    # Start the input thread
    input_t.start()

    # Wait for the input thread to finish
    input_t.join()
    print("\nInput thread finished!")
    print("\nnow remaining threads will execute!\n")
    # Start the other threads
    reverse_t.start()
    capital_t.start()
    shift_t.start()

    # Wait for the other threads to finish
    reverse_t.join()
    capital_t.join()
    shift_t.join()

    print("\nall threads are executed")
