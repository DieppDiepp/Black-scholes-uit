import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button


def quadratic_variation(B):
    return np.cumsum(np.power(np.diff(B, axis=0, prepend=0.), 2), axis=0) #Co xu hướng bằng T


class AnimationControl:
    def __init__(self, ani):
        self.ani = ani
        self.paused = False

    def pause(self, event):
        if self.paused:
            self.ani.event_source.start()
        else:
            self.ani.event_source.stop()
        self.paused = not self.paused


def main():
    n = 250 # Giảm số lượng điểm để tăng tốc độ vẽ
    d = 20  # Số chiều
    T = 1.
    times = np.linspace(0., T, n)
    dt = times[1] - times[0]
    dB = np.sqrt(dt) * np.random.normal(size=(n - 1, d))  # Tạo n - 1 điểm ngẫu nhiên theo phân phối chuẩn
    B0 = np.zeros(shape=(1, d))
    B = np.concatenate((B0, np.cumsum(dB, axis=0)), axis=0) #Vị trí hiện tại của B(t) = B(0) + tổng của các dB
    fig, ax = plt.subplots()
    lines = [ax.plot([], [])[0] for _ in range(d)]
    line_quad_var, = ax.plot([], [], color='red', label='Quadratic Variation')
    line_parabola, = ax.plot([], [], color='blue', label='y = x^2')


    def update(frame):
        ax.clear()
        ax.title.set_text('Brownian Motion and Quadratic Variation Simulation')
        ax.set_xlabel('t', fontsize=16)
        ax.set_ylabel('B(t)', fontsize=16)
        ax.set_xlim(0, T) #Đặt giới hạn trục x
        ax.set_ylim(-3, 3) #Đặt giới hạn trục y
        for i, line in enumerate(lines):
            line.set_data(times[:frame], B[:frame, i])
            ax.plot(times[:frame], B[:frame, i])
        line_quad_var.set_data(times[:frame], quadratic_variation(B)[:frame])
        ax.plot(times[:frame], quadratic_variation(B)[:frame], color='red', label='Quadratic Variation')
        y = np.linspace(-1, 1, 400)
        t = y**2
        line_parabola.set_data(t, y)
        ax.plot(t, y, color='blue', label='y = x^2')
        return lines + [line_quad_var, line_parabola]
    ani = FuncAnimation(fig, update, frames=n, interval=20)
    ani.save('Brownian_motion.gif', fps = 30) #Lưu video
    # Thêm nút bấm Pause/Resume
    pause_ax = plt.axes([0.775, 0.08, 0.2, 0.075])
    pause_button = Button(pause_ax, 'Pause/Resume')
    animation_control = AnimationControl(ani)
    pause_button.on_clicked(animation_control.pause)

    plt.tight_layout()  # Tự động điều chỉnh các thông số của hình vẽ
    plt.show()


if __name__ == '__main__':
    main()