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
    n = 300 # Giảm số lượng điểm để tăng tốc độ vẽ
    d = 20  # Số chiều
    T = 5.
    times = np.linspace(0., T, n)
    dt = times[1] - times[0]
    dB = np.sqrt(dt) * np.random.normal(size=(n - 1, d))  # Tạo n - 1 điểm ngẫu nhiên theo phân phối chuẩn
    B0 = np.zeros(shape=(1, d))
    B = np.concatenate((B0, np.cumsum(dB, axis=0)), axis=0) #Vị trí hiện tại của B(t) = B(0) + tổng của các dB
    S0 = 25 #Giá trị ban đầu của cổ phiếu
    muy = 0.05 #Lợi nhuận trung bình hàng năm
    sigma = 0.4 #Độ biến động hàng năm
    St = S0 * np.exp((muy - (sigma**2)/2)*T + sigma * B) #Giá trị cổ phiếu tại thời điểm t
    fig, ax = plt.subplots() #Tạo hình vẽ
    lines = [ax.plot([], [])[0] for _ in range(d)] #Tạo dòng cho mỗi chiều
    line_y0, = ax.plot([], [], color='blue', label='y = 0') #Tạo dòng y = 0

    def update(frame):
        ax.clear()
        ax.title.set_text('Stock Price Simulation')
        ax.set_xlabel('t', fontsize=16)
        ax.set_ylabel('S(t)', fontsize=16)
        ax.set_xlim(0, T)
        ax.set_ylim(-100, 100)
        for i, line in enumerate(lines): #Vẽ dòng cho mỗi chiều
            line.set_data(times[:frame], St[:frame, i]) #Vẽ dòng
            ax.plot(times[:frame], St[:frame, i]) #Vẽ dòng
        y = np.zeros(20) #Tạo mảng y = 0
        t = np.linspace(0, T, 20) #Tạo mảng t
        line_y0.set_data(t, y)
        ax.plot(t, y, color='blue', label='y = 0')
        return lines + [line_y0]

    ani = FuncAnimation(fig, update, frames= n, interval=20) #Tạo animation
    #ani.save('stock_price.gif') #Lưu file gif
    # Thêm nút bấm Pause/Resume
    pause_ax = plt.axes([0.775, 0.085, 0.2, 0.075])
    pause_button = Button(pause_ax, 'Pause/Resume')
    animation_control = AnimationControl(ani)
    pause_button.on_clicked(animation_control.pause)

    plt.tight_layout()  # Tự động điều chỉnh các thông số của hình vẽ
    plt.show()


if __name__ == '__main__':
    main()