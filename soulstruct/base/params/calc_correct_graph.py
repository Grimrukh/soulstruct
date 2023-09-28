import numpy as np


THRESHOLD_POINTS = [1, 18, 60, 80, 150]
THRESHOLD_COEFFICIENTS = [0, 25, 75, 90, 142.5]
GAMMA_FACTORS = [1.2, -1.2, 1, 1, 1]


def linearize_segment(line_x, line_y, next_x):
    width = line_x[1] - line_x[0]
    height = line_y[1] - line_y[0]
    slope = height / width
    next_width = next_x - line_x[1]
    return line_y[1] + next_width * slope


def main():
    import matplotlib.pyplot as plt
    _, ax = plt.subplots()
    for i in range(len(THRESHOLD_POINTS) - 1):
        x0, x1 = THRESHOLD_POINTS[i:i + 2]
        y0, y1 = THRESHOLD_COEFFICIENTS[i:i + 2]
        gamma = GAMMA_FACTORS[i]
        if gamma < 0:
            gamma = 1 / -gamma
        # gamma = 1

        width = (x1 - x0)
        height = (y1 - y0)
        slope = height / width
        print(f"Plotting line segment: [{x0}, {x1}], [{y0}, {y1}], slope {slope}, gamma {gamma}")

        x = np.linspace(0, 1, 100)
        y = x ** gamma
        x = x * width + x0
        y = y * height + y0
        ax.plot(x, y)
        ax.scatter([x0, x1], [y0, y1])

    ax.set_xlabel("Level")
    ax.set_ylabel("Value")
    plt.show()


if __name__ == '__main__':
    # main()
    new_y = linearize_segment([40, 60], [30, 40], 99)
    print(f"Next Y: {new_y}")
