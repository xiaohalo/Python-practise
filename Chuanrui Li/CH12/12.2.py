#You are given the source to an application which crashes when it is run.
#After running it ten times in a debugger, you find it never crashes in the same place.
#The application is single threaded, and uses only the C standard library. 
#What programming errors could be causing this crash? How would you test each one?

1. Random variable: 
The application uses some random number or variable component which may not be fixed for every execution of the program. Examples include: user input, a random number generated by the program, or the time of day.
2. Memory Leak: 
The program may have run out of memory. Other culprits are totally random for each run since it depends on the number of processes running at that particular time. This also includes heap overflow or corruption of data on the stack.
3, External dependency:
Crash because some other programs get an error

1, track down the problem for doing similar functions and figure out the solutions
Ex: doing the I/O event