import numpy as np
import matplotlib.pyplot as plt
import math

h0 = 15  
g = 9.8  
v0 = 0   


t = math.sqrt(2 * h0 / g)
print("Waktu jatuh = ", t, " s")


v = g * t
print("Kecepatan Akhir = ", v, " m/s")

h_akhir = h0 - 0.5 * g * t**2
print("Posisi Akhir = ", h_akhir, " m")


t_akhir = np.linspace(0, t, num=100)


v_akhir = g * t_akhir


posisi = h0 - 0.5 * g * t_akhir**2


fig, ax1 = plt.subplots()
ax1.plot(t_akhir, v_akhir, label="Kecepatan")
ax1.set(xlabel='Waktu (s)', ylabel='Kecepatan (m/s)', 
        title='Grafik kecepatan benda sebagai fungsi waktu selama benda jatuh')
ax1.grid()

fig, ax2 = plt.subplots()
ax2.plot(t_akhir, posisi, label="Posisi", color='orange')
ax2.set(xlabel='Waktu (s)', ylabel='Posisi (m)', 
        title='Grafik posisi benda sebagai fungsi waktu selama benda jatuh')
ax2.grid()


plt.show()



