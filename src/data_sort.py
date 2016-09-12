import pylab
import numpy as np

xy_file = open("../data/xy.dat", "r")

# Initialise an empty list to store the data
x = []
y = []

while True:
    try:
        # Read the next line.
        line = xy_file.readline()

        # Split this line into words.
        words = line.split()

        if len(words) !=2:
            break
    except:
        break

    # Convert each line of data into a float
    xdata = float(words[0])
    ydata = float(words[1])

    x.append(xdata)
    y.append(ydata)


x = np.array(x)
y = np.array(y)

ymax = np.amax(y)
ymin = np.amin(y)


print "The maximum value is", ymax
print "The minimum value it", ymin

pylab.plot(x, y)
pylab.xlabel("x data")
pylab.ylabel("y data")
pylab.show()

