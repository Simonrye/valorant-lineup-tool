# Valorant Lineup Script
# Version 1.0
# Author: Simonrye
# GitHub: https://github.com/Simonrye/valorant-lineup-tool/
# License: Creative Commons Zero v1.0 Universal

# Please read the entire README.md file for instructions and usage guidelines.
# Use this script responsibly and only in custom games.
# Respect the game's terms of service and fair play rules.
# Remember that third-party scripts are not officially endorsed by Valorant.

from pynput import keyboard, mouse
from pynput.mouse import Button, Controller
from tkinter import *
from PIL import Image, ImageTk
import pyautogui
import math
import ctypes
import json

def change_speed(speed=10):
    set_mouse_speed = 113
    ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)

settings_file = 'settings.json'
def remove_comments(json_text):
    lines = json_text.split('\n')
    cleaned_lines = [line for line in lines if not line.lstrip().startswith('//')]
    return '\n'.join(cleaned_lines)

change_speed(speed=10)
with open(settings_file, 'r') as file:
    try:
        json_text = remove_comments(file.read())
        data = json.loads(json_text)
        val_sensitivity = data['valorant_sensitivity']
        player_x, player_y = data['player_coords']
        
        personal_multi = data['map_distance_multiplier']
        
        ascent_multi = data['ascent_multiplier']
        bind_multi = data['bind_multiplier']
        breeze_multi = data['breeze_multiplier']
        fracture_multi = data['fracture_multiplier']
        haven_multi = data['haven_multiplier']
        icebox_multi = data['icebox_multiplier']
        lotus_multi = data['lotus_multiplier']
        pearl_multi = data['pearl_multiplier']
        split_multi = data['split_multiplier']
        sunset_multi = data['sunset_multiplier']
        
        
        unplanted_rgb = data['unplanted_spike_rgb']
        planted_rgb = data['planted_spike_rgb']
        tolerance = data['tolerance']
        XFILE = data['x_file']
        DOTFILE = data['dot_file']
    
    except Exception as e:
        val_sensitivity = 0.4
        player_x, player_y = 206, 227
        personal_multi = 1

        ascent_multi = 1.07
        bind_multi = 1.27
        breeze_multi = 1.03
        fracture_multi = 0.96
        haven_multi = 1
        icebox_multi = 1.03
        lotus_multi = 1.035
        pearl_multi = 0.96
        split_multi = 0.958
        sunset_multi = 0.964
        
        unplanted_rgb = [219, 230, 3]
        planted_rgb = [248, 188, 0]
        tolerance = 12
        XFILE = 'overlays/violet_x.png'
        DOTFILE = 'overlays/red_dot.png'
        
        print(f'WARNING! Unable to load {settings_file}!\nUsing default values that may be inaccurate.')
        print(f'Error message:\n{e}\n')

print('''Valorant Lineup Script
Version 1.0
Author: Simonrye
GitHub: https://github.com/Simonrye/valorant-lineup-tool/
License: Creative Commons Zero v1.0 Universal

Please read the entire README.md file for instructions and usage guidelines.
Use this script responsibly and only in custom games.
Respect the game's terms of service and fair play rules.
Remember that third-party scripts are not officially endorsed by Valorant.
''')


while True:
    choice = input('''Select agent:
1. Brimstone
2. Viper
3. KAY/O
''').strip()
    if choice in ('1', '2', '3'):
        agent = {
            '1': 'Brimstone',
            '2': 'Viper',
            '3': 'KAY/O',
        }[choice]
        break

while True:
    choice = input('''
Select map:
1. Ascent
2. Bind
3. Breeze
4. Fracture
5. Haven
6. Icebox
7. Lotus
8. Pearl
9. Split
10. Sunset
''').strip()
    if choice in (str(x) for x in range(1,11)):
        map_multi = {
            '1': ascent_multi,
            '2': bind_multi,
            '3': breeze_multi,
            '4': fracture_multi,
            '5': haven_multi,
            '6': icebox_multi,
            '7': lotus_multi,
            '8': pearl_multi,
            '9': split_multi,
            '10': sunset_multi
        }[choice] * personal_multi
        break

while True:
    choice = input('''
Select mode:
1. Unplanted spike
2. Planted spike
''').strip()
    if choice in ('1', '2'):
        target_color = {
            '1': unplanted_rgb,
            '2': planted_rgb
        }[choice]
        break

print('\nSELECTED AGENT:', agent)

SENSE_MULTI = val_sensitivity/.4 #Do not change. Edit sensitivity in settings.json file.

print('Script initiated.')
def find_all_pixels_with_tolerance(target_color, tolerance, region_top_left, region_bottom_right):
    screen = pyautogui.screenshot(region=(region_top_left[0], region_top_left[1], region_bottom_right[0] - region_top_left[0], region_bottom_right[1] - region_top_left[1]))    
    matches = []
    for x in range(screen.width):
        for y in range(screen.height):
            pixel_color = screen.getpixel((x, y))
            if all(abs(pixel_color[i] - target_color[i]) <= tolerance for i in range(3)):
                matches.append((x + region_top_left[0], y + region_top_left[1]))
    return matches


def calculate_average_coordinates(matches):
    if not matches:
        return None, None
    avg_x = sum(x for x, y in matches) // len(matches)
    avg_y = sum(y for x, y in matches) // len(matches)
    return avg_x, avg_y


def calculation(target_x, target_y):
    delta_x = target_x - player_x
    delta_y = target_y - player_y
    turn_angle = math.degrees(math.atan2(delta_y, delta_x))
    distance_m = math.sqrt(delta_x ** 2 + delta_y ** 2)
    return distance_m, turn_angle


def find_spike():
    global target_color, tolerance

    region_top_left = (20, 30)
    region_bottom_right = (400, 230)
    matches = find_all_pixels_with_tolerance(target_color, tolerance, region_top_left, region_bottom_right)
    if matches:
        avg_x, avg_y = calculate_average_coordinates(matches)
        distance_m, turn_angle = calculation(avg_x, avg_y)
        return distance_m * 0.351 * map_multi, turn_angle + 90
    else:
        print(f'Spike not found! No pixels with color {target_color} found in the specified region')
        return None, None


START_X = 960
START_Y = -1650

win = Tk()
win.wm_attributes('-transparentcolor', win['bg'])
win.geometry('1920x1000')

canvas = Canvas(win, width=1920, height=1080)
canvas.pack()

image = ImageTk.PhotoImage(Image.open(XFILE))
image2 = ImageTk.PhotoImage(Image.open(DOTFILE))
img = canvas.create_image(START_X, START_Y, anchor='center', image=image, state='hidden')
img2 = canvas.create_image(START_X, START_Y, anchor='center', image=image2, state='hidden')

label = Label()
label.master.overrideredirect(True)
label.master.lift()
label.master.wm_attributes('-topmost', True)

online = False
dropable = False
lastx, lasty = 960, 540
mouse_moved = False

def on_move(x, y):
    global listener, lastx, lasty, mouse_moved, dropable
    if not mouse_moved:
        mouse_moved = True
        canvas.itemconfig(img, state='normal')
        if dropable:
            canvas.itemconfig(img2, state='normal')
    canvas.move(img, (lastx - x) * 2.5 * SENSE_MULTI, (lasty - y) * 6 * SENSE_MULTI)
    canvas.move(img2, (lastx - x) * 2.5 * SENSE_MULTI, (lasty - y) * 6 * SENSE_MULTI)
    lastx, lasty = x, y
#canvas.move(img, (lastx - x)*2.5 * SENSE_MULTI, -(y - lasty )*12/2 * SENSE_MULTI)

def ExitESC(key):
    global listener, listenerExit, online, win
    stop_keys = [keyboard.Key.left, keyboard.Key.esc, keyboard.Key.caps_lock]
    if key in stop_keys and online:
        listener.stop()
        listenerExit.stop()
        canvas.itemconfig(img, state='hidden')
        canvas.itemconfig(img2, state='hidden')
        change_speed(speed=10)
        online = False

def BeginMouse():
    global listenerExit, lastx, lasty, mouse_moved
    lastx, lasty = 960, 1080
    Controller().position = (1920//2 , 1080)
    mouse_moved = False
    global listener
    listener = mouse.Listener(on_move=on_move)
    listener.start()
    listenerExit = keyboard.Listener(on_press=ExitESC)
    listenerExit.start()


def on_press1(key): 
    global listener, online, win
    try:
        if key == keyboard.Key.right and not online:
            distance_m, turn_angle = find_spike()
            if distance_m is None or turn_angle is None:
                return
            canvas.coords(img, START_X, START_Y)
            canvas.coords(img2, START_X, START_Y)
            canvas.move(img, turn_angle * 5.6, 0)
            canvas.move(img2, turn_angle * 5.6, 0)

            if agent == 'Brimstone':
                change_main, change_drop = calculate_change_brim(distance_m)
            elif agent == 'Viper':
                change_main, change_drop = calculate_change_viper(distance_m)
            elif agent == 'KAY/O':
                change_main, change_drop = calculate_change_kayo(distance_m)
            else:
                print('Agent selection error.')
                return
            print('Distance:', distance_m)
            
            canvas.move(img, 0, change_main)
            if change_drop is not None:
                canvas.move(img2, 0, change_drop)            
            BeginMouse()
            change_speed(speed=2)
            online = True            
    except Exception as e:
        print(e)


def calculate_change_brim(M_bounce):
    global dropable
    change_main = M_bounce * 5.7 - 240
    if M_bounce <= 16:
        dropable = False
        return change_main, None
    dropable = True
    change_drop = M_bounce * 6.6 - 240
    return change_main, change_drop


def calculate_change_viper(M_bounce):
    global dropable
    dropable = False
    if M_bounce <= 44:
        change_main = M_bounce * 6.1 - 230
    elif M_bounce <= 46:
        change_main = M_bounce * 8 - 300
    else:
        change_main = M_bounce * 10 - 410
    return change_main, None


def calculate_change_kayo(M_bounce):
    global dropable
    dropable = False
    if M_bounce <= 26:
        change_main = M_bounce * 10 - 220
    elif M_bounce <= 37:
        change_main = M_bounce * 20 - 540
    else:
        change_main = M_bounce * 100 - 3900   
    return change_main, None


listener1 = keyboard.Listener(
        on_press=on_press1)
listener1.start()
win.mainloop()
