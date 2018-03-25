# Plotting
# Kobe Arthur Scofield
# 2018-03-24
# Build 32
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.4

# Because some steps seem slow, so you'll see many printing in this script.

# Loading libraries. matplotlib seems so long.
print("Loading numpy...")
import numpy as np
print("Loading matplotlib...")
import matplotlib.pyplot as plt
print("Library loaded.\n")

# This function tries to process multiple input and split the input string.
def grp_input(inputcount):
    tmp = input()
    return tuple(tmp.split(" ", maxsplit= inputcount))  # Then pack it as a tuple and return.
# End of grp_input

# This function calculate single dot of sine function
def sinedw(x, amp, omega, phi):
    rz = amp * np.sin(omega * x +phi)   # numpy goes faster
    return rz
# End of sinedw

# Initializing elements used in this script
linedx = []
inputstr = []
sinegpdw = np.frompyfunc(sinedw, 4, 1)  # Turn the sinedw function that can calculate arrays

print("Syntax: y = A sin(ωθ + φ)")
print("Input line numbers to draw:")
linedraw = int(input())                                     # How many lines to draw
print("Input function range (min value and max value) and sample dots number: Seperated with space.")
min, max, sample = grp_input(3)                             # Getting data for plotting x range and samples
min = float(min); max = float(max); sample = int(sample);   # Turn str to numbers
x = np.linspace(min, max, sample)                           # Initializing x array
for loop in range(0, linedraw ):
    print("Please input A, ω and φ value to line", loop + 1, "in", linedraw, "with space seperated")
    amp, omega, phi = grp_input(3)                              # Getting data for plotting a function graph
    amp = float(amp); omega = float(omega); phi = float(phi);   # Turn str to numbers
    inputstr.append((amp, omega, phi))                          # Temp store for tags (tuples in a list)
    linedx.append(np.array(sinegpdw(x, amp, omega, phi)))       # Calcutate and store it to a list
#
# Plotting part below. Line color auto defined.
print("Initializing plot canvas...")
plt.figure(figsize=(8,4))
print("Plotting lines...")
for loop in range(0, linedraw):
    amp, omega, phi = inputstr[loop]        # Extract label value from the tuple in the list
    plt.plot(x, linedx[loop], label = ("$" + str(amp) + "sin(" + str(omega) + "θ +" + str(phi) + ")$")) # Plot
    print("Line", loop + 1, "in", linedraw, "completed")
linedx.clear()
inputstr.clear()    # Ram clear
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Graph of $y = A sin(ωθ + φ)$")
plt.legend()
print("Plotting completed.")
plt.show()
