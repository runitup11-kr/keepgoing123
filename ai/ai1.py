
import matplotlib.pyplot as plt


# 데이터 준비
x = range(-10,11)
y1 = [2*val for val in x]
y2 = [4*val for val in x]
y3 = [8*val for val in x]

# 그래프 선택 후 드로잉
plt.plot(x, y1, label = "2x", color = "red")
plt.plot(x, y2, label = "4x", marker = "o")
plt.plot(x, y3, label = "8x", marker = "x")

plt.legend()
plt.title("autumn")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)

plt.show()