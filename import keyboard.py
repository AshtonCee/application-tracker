from pynput import keyboard
import sys
import pickle

count = 0

def on_press(key):
    global count
    if key == keyboard.Key.page_up:
        count += 1
        print("PgUp pressed! Total number of internships applied to:", count)
        save_file()
    if key == keyboard.Key.page_down:
        print('Program terminating...')
        save_file()
        sys.exit(0)

pressed_keys = set()

def on_key_press(key):
    if key not in pressed_keys:
        pressed_keys.add(key)
        on_press(key)

def on_key_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

def save_file():
    with open(r'C:\Users\ashto\Downloads\python personal projects\internship application counter\count.pkl', 'wb') as f:
        pickle.dump(count, f)

def open_file():
    global count
    with open(r'C:\Users\ashto\Downloads\python personal projects\internship application counter\count.pkl', 'rb') as f:
        count = pickle.load(f)
    return count

save_file()
count = open_file()

print('Current count: ', count)

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
