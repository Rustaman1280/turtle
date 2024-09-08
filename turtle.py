import turtle
import colorsys

# Pengaturan layar
screen = turtle.Screen()
screen.bgcolor("black")

# Pengaturan turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.colormode(1)

# Menggambar pola spiral
n = 36  # Jumlah iterasi
h = 0   # Variabel untuk hue (warna)

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)  # Konversi dari HSV ke RGB
    t.pencolor(c)
    t.forward(i * 3 / n + i)  # Memperpanjang garis secara bertahap
    t.left(59)  # Mengatur sudut belokan
    h += 1/n    # Meningkatkan hue untuk perubahan warna

# Selesai
turtle.done()
