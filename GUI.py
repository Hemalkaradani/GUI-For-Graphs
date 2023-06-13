import tkinter as tk
import pygame

def change_graph_color():
    selected_color = color_var.get()
    graph.config(bg=selected_color)
    if selected_color == "red":
        pygame.mixer.music.play()

def select_screen():
    # Logic for selecting the screen goes here
    pass

root = tk.Tk()
root.title("Graph Color Buzzer")

# Screen Selector Button
screen_button = tk.Button(root, text="Select Screen", command=select_screen)
screen_button.pack()

# Color Selector Button
color_var = tk.StringVar(root)
color_var.set("blue")  # Default color
color_button = tk.OptionMenu(root, color_var, "blue", "red", "green", "yellow")
color_button.pack()

# Graph
graph = tk.Label(root, text="Graph Area", width=20, height=10, bg=color_var.get())
graph.pack()

# Buzzer Log
log_label = tk.Label(root, text="Number of Buzzer Logs: 0")
log_label.pack()

# Initialize Pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("beep.wav")  # Replace "beep.wav" with your sound file

root.mainloop()
