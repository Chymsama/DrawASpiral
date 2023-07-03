#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import math

# Khởi tạo cửa sổ đồ họa và con rùa
window = turtle.Screen()
t = turtle.Turtle()

# Khởi tạo giá trị ban đầu và nhập giá trị thoát
d = 1
exit_distance = float(input("Nhập khoảng cách thoát khỏi vòng lặp: "))
num_circles = int(input("Nhập số lượng hình tròn xoắn ốc: "))
angle = 360 / num_circles  # Góc xoắn giữa các hình tròn xoắn ốc

for _ in range(num_circles):
    while True:
        t.forward(d)
        t.left(angle)

        d += math.pi * d / 180  # Tăng độ lớn theo đường cong hình tròn

        # Tính khoảng cách từ điểm hiện tại đến điểm ban đầu
        distance = t.distance(0, 0)

        if distance > exit_distance:
            break

# Đóng cửa sổ đồ họa khi thoát khỏi vòng lặp
window.bye()


# In[ ]:




