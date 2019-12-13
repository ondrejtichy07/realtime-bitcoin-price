from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['y_value']

    plt.cla()
    plt.plot(x, y1, 'y')
    plt.title("Bitcoin price (USD)")
    plt.xticks(rotation=270, fontsize=10)
    plt.yticks(fontsize=15)
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.tight_layout()
plt.show()