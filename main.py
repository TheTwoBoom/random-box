import random
from tkinter import *
from PIL import Image, ImageTk
import os
root = Tk()
root.geometry("600x100")
var = StringVar()

items = {
    "diamond_block": 625,
#    "coal_block": 125,
    "iron_block": 280,
    "gold_block": 350,
    "redstone_block": 30,
    "emerald_block": 400,
    "diamond_ore": 625,
    "coal_ore": 30,
    "iron_ore": 80,
    "gold_ore": 65,
    "redstone_ore": 30,
}
final_items = []
items_list = list(items.keys())

box = 30000
box_buy = {key: 0 for key in items}

def get_image_path(item):
    """Generates the full file path to an item's image."""
    base_path = r"C:\Users\Berni\PycharmProjects\random-box"  # Replace with the path to the directory containing the images
    file_name = f"{item}.png"
    return os.path.join(base_path, file_name)

def value():
    global box
    global box_buy
    global var
    global final_items
    wert = random.randint(35000,55000)
    print(wert)
    for i in range(3):
        final_items.append(random.choice(list(items_list)))
    while box <= wert:
        item = random.choice(final_items)
        box_buy[item] += 1
        box += items[item]
    box_buy = {key:value for (key, value) in box_buy.items() if value is not 0}
    var.set(str(box_buy))
    box = 30000
    box_buy = {key: 0 for key in items}
    final_items = []
    return box_buy, wert

root.attributes('-topmost', True)
refresh = Button(root, text="Refresh", command=value)
refresh.pack()
l = Label(root, textvariable = var, font=("Ubuntu Mono", 12))
l.pack()
root.mainloop()
