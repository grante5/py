import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    p = 2 * dx - dy
    y = y1
    points = []

    for x in range(x1, x2 + 1):
        if steep:
            points.append((y, x))
        else:
            points.append((x, y))

        if p >= 0:
            y += 1 if y1 < y2 else -1
            p -= 2 * dx

        p += 2 * dy

    return points

def main():
    x1, y1 = map(int, input("Enter starting point (x1, y1): ").split())
    x2, y2 = map(int, input("Enter ending point (x2, y2): ").split())
    points = draw_line(x1, y1, x2, y2)

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.figure(figsize=(8, 6))  
    plt.plot(x_values, y_values, marker='o', color='blue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Bresenham Line Drawing Algorithm')
    plt.grid()
    plt.tight_layout()  
    plt.show()

if __name__ == "__main__":
    main()