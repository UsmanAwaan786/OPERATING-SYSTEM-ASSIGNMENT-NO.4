# OPERATING-SYSTEM-ASSIGNMENT-NO.4
Objectives: 
 		
•	Our main objective is to develop a program to create 4 different threads.
•	Apply these four threads on four different functions and get results.
Implementation:

I used the "threading" header file to implement multithreading, using the "threading.thread()" function to create 4 threads equivalent to my 4 desire functions  and execute them and used "threading.thread.join()"which causes the calling thread to block until the specified thread has completed.
Functions

	input_thread()
	Use for taking string input from user

	reverse_thread()
	Use for reversing the input string

	capital_thread()
	Use for capitalizing the input string

	shift_thread()
	Use for shifting each character by two of input string


Functional Commands:

	Threading.thread.join()
	It causes the calling thread to block until the specified thread has completed.

	Thread.start()
	Used to start thread

System Specifications:

•	Compiler (interpreter)

	PyCharm

•	Programming Language

	Python

•	Operating System:

	Windows 8,8.1,10,11 x64 bit
	Ubuntu

•	Hardware required:

	Processor: Core i3 or more with 4 cores 
	Dedicated video memory (at least 1 GB)
	Ram: 4 GB Ram
	Hard Disk: 100GB

Processing of Code:

	This code creates four threads other than main thread: an input thread, a reverse thread, a capital thread, and a shift thread. The input thread takes a string input from the user, and the other three threads operate on this string. The reverse thread reverses the string, the capital thread capitalizes it, the shift thread shifts each character by two.
The threads are designed to run concurrently: the input thread prompts the user for input, and the other three threads wait until the input thread has finished before starting their work. This is done using the threading.thread.join() method, which causes the calling thread to block until the specified thread has completed. 
The code also includes exception handling to catch any errors that may occur in the threads. If an error occurs, a message is printed indicating which thread encountered the error. 
Finally, the code takes care to use memory resources efficiently by only creating the threads when they are needed and releasing them when they are no longer needed.
