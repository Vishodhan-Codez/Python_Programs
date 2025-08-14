# Saved interactive plot script for y = x * n * (1 - n)
# Run with a Python environment that supports matplotlib interactive windows or Jupyter notebooks.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

rng = np.random.default_rng(42)

def make_sample(size=2500):
    return rng.triangular(-1.2, 0.0, 1.5, size=size)

def compute_y(x, n):
    return x * int(round(n)) * (1 - int(round(n)))

x = make_sample()

fig, ax = plt.subplots(figsize=(11,6))
fig.patch.set_facecolor('#0b0b0b')
ax.set_facecolor('#0b0b0b')
plt.subplots_adjust(left=0.08, right=0.98, top=0.88, bottom=0.20)

y = compute_y(x, 99999)
sc = ax.scatter(x, y, s=10, alpha=0.85, c=x, edgecolors='none')
ax.set_xlabel('x (random — triangular, mode=0)')
ax.set_ylabel('y = x * n * (1 - n)')
ax.set_title('Interactive plot — y = x · n · (1 − n)', color='#ffffff', fontsize=14, pad=12)
ax.grid(True, linestyle=':', linewidth=0.6, color='#222222', alpha=0.6)
ax.spines['bottom'].set_color('#555555')
ax.spines['top'].set_color('#555555')
ax.spines['left'].set_color('#555555')
ax.spines['right'].set_color('#555555')
ax.tick_params(colors='#cccccc', which='both')

slider_ax = plt.axes([0.12, 0.09, 0.68, 0.04], facecolor='#111111')
n_slider = Slider(slider_ax, 'n', valmin=0, valmax=200000, valinit=99999, valfmt='%0.0f', valstep=1)

button_ax = plt.axes([0.83, 0.09, 0.10, 0.04], facecolor='#111111')
redraw_button = Button(button_ax, 'New sample', color='#333333', hovercolor='#444444')

def update(val):
    new_y = compute_y(x, n_slider.val)
    sc.set_offsets(np.c_[x, new_y])
    fig.canvas.draw_idle()

n_slider.on_changed(update)

def redraw(event):
    global x
    x = make_sample()
    new_y = compute_y(x, n_slider.val)
    sc.set_offsets(np.c_[x, new_y])
    sc.set_array(x)
    fig.canvas.draw_idle()

redraw_button.on_clicked(redraw)

plt.show()