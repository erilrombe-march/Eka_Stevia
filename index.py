import turtle
import math
import time
import pygame
import os

folder = os.path.dirname(os.path.abspath(__file__))
lokasi_lagu = os.path.join(folder, "1010.MP3")

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.load(lokasi_lagu)

lyrics_list = [
    (0, "🎵 I Love You"),
    (1, "Ingin Rasanya Hatiku"),
    (4, "Memeluk dan Menciummu"),
    (7, "Dan Ingin Kukatakan Cinta Kamu"),
    (12, "Ingin Hati Ini Lebih Dekat Lagi Denganmu"),
    (18, "Dan Kukatakan"),
    (22, "I Will Say I Love You"),
    (28, ""),
    (34, "Di Hari Berikutnya (our next day)"),
    (39, "Kujumpa Lagi Denganmu"),
    (42, "When I Saw You (Kau Semakin Mempesona)"),
    (48, "Senyuman di Bibirmu Membuatku Tergila-gila"),
    (58, "Khayalku Membayangkan Kapankah Kau Jadi Milikku"),
    (68, "Khayalku Kau Tercipta Hanyalah Untuk"),
    (77, "Hanya Untukku (Hanya Untukku)"),
    (81, ""),
]

screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("black")
screen.title("LOVE JAMILAH ❤️")
screen.tracer(0)

pygame.mixer.music.play()
start_time = time.time()

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.color("#ffb6c1")

for scale in range(11, 17):
    for i in range(120):
        angle = i * 2 * math.pi / 120
        x = 16 * (math.sin(angle) ** 3) * scale
        y = (13 * math.cos(angle) -
            5 * math.cos(2 * angle) - 
            2 * math.cos(3 * angle) -
            math.cos(4 * angle)) * scale

        t.goto(x + 100, y)
        t.write("I LOVE YOU", align = "center",
                font = ("Times New Roman", 8, "bold"))

t.goto(100, -20)
t.color("#ff1493")
t.write("EKA STEVIA", align = "center",
        font = ("Times New Roman", 20, "bold"))

lyric_turtle = turtle.Turtle()
lyric_turtle.hideturtle()
lyric_turtle.penup()
lyric_turtle.color("#ffb6c1")

def update_lyrics():
    elapsed = time.time() - start_time
    current_lyric = ""

    for timestamp, lyric in lyrics_list:
        if elapsed >= timestamp:
            current_lyric = lyric
        else:
            break

    lyric_turtle.clear()
    lyric_turtle.goto(-470, 250)
    lyric_turtle.write(current_lyric, align = "left",
                       font = ("Times New Roman", 12, "bold"))

    if pygame.mixer.music.get_busy():
        screen.ontimer(update_lyrics, 250)
    else:
        lyric_turtle.clear()
        lyric_turtle.goto(-470, 250)
        lyric_turtle.write("❤️❤️❤️", align = "left",
                           font = ("Times New Roman", 12, "bold"))

update_lyrics()
screen.update()

try:
    turtle.done()
finally:
    pygame.mixer.music.stop()
    pygame.mixer.quit()
