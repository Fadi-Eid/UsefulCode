import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM7'
ser.open()

fig, ax = plt.subplots()

ydata = []

# Set initial y-axis limits
ax.set_ylim(10, 200)
def update_data(i):
    global ydata  # Declare ydata as a global variable
    newpoint = int(ser.readline())
    print(newpoint)
    ydata.append(newpoint)
    
    # Keep only the last 50 values
    ydata = ydata[-40:]
    
    ax.clear()
    ax.plot(ydata)
    
    # Set y-axis limits
    ax.set_ylim(10, 200)
    # ax.yaxis.set_ticks(range(10, 201, 20))
    # # Add grid
    # ax.grid(True)

ani = animation.FuncAnimation(fig, update_data, interval=60)
plt.show()
