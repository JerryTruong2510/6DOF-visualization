import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import numpy as np
from Denavit_Hartenberg_Matrices_Generator import trans_mat_update as DHMG

DH_par_lists = [[0, 90, 10, 0],
                [10, 0, 0, 0],
                [10, 0, 0, 0],
                [5, 0, 0, 0]]
dhmg = DHMG(4, DH_par_lists)
dhmg.generate_matrices()
dhmg.update_pos_txt()

def setup_and_plot_ax():
    ax.clear()

    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    ax.set_zlim(0, 60)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    x = [0]
    y = [0]
    z = [0]

    f = open("Pos.txt", "r")
    for line in f:
        pos_val = line.strip().split(" ")
        x.append(float(pos_val[0]))
        y.append(float(pos_val[1]))
        z.append(float(pos_val[2]))

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)

    ax.scatter(x, y, z)
    ax.plot(x, y, z)
def update_par(val):
    DH_par_lists[0][-1] = Servo_1_slider.val
    DH_par_lists[1][-1] = Servo_2_slider.val
    DH_par_lists[2][-1] = Servo_3_slider.val
    DH_par_lists[3][-1] = Servo_4_slider.val
    dhmg.DH_par_update(DH_par_lists)
    dhmg.generate_matrices()
    dhmg.update_pos_txt()

    setup_and_plot_ax()

ax = plt.figure().add_subplot(projection='3d')
plt.subplots_adjust(bottom=0.3) # add more space

for i in range(4):
    exec(f"Servo_{i+1}_placeholder = plt.axes([0.2, {0.2 - i*0.05}, 0.72, 0.015])")
    exec(f"Servo_{i+1}_slider = Slider(Servo_{i+1}_placeholder, 'Servo {i+1}', valmin = -180, valmax = 180, valinit = 0)")
    print(i)

Update_button_placeholder = plt.axes([0.05, 0.8, 0.2, 0.1])
Update_button = Button(Update_button_placeholder, label="Update", color="white", hovercolor="grey")
Update_button.on_clicked(update_par)


setup_and_plot_ax()
plt.show()