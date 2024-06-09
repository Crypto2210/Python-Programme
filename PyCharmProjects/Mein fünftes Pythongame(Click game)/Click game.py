import random
import time
import keyboard
import sys


def tasten_eingabe():
    key_event = keyboard.read_event()
    if key_event.event_type == keyboard.KEY_DOWN:
        aktuelle_zeit2 = time.time()
        reaktionszeit = aktuelle_zeit2 - aktuelle_zeit1
        if reaktionszeit < 0.1:
            print("\nKeine Taste davor drücken!")
            sys.exit()
        print("\nDeine Reaktionszeit ist: ", reaktionszeit, "sec")
        input("Zum beenden Entertaste drücken!\n")


print("Ich teste deine Reaktionsgeschwindigket, nachdem du etwas eingegeben hast musst du die Leertaste drücken...")
print("Bevor du etwas siehst nichts drücken!!!")
print("Drücke beliebige Taste um zu starten!")
start_event = keyboard.read_event()
if start_event.event_type == keyboard.KEY_DOWN:
    print("\nStart!!")
    randnumb = random.randint(4, 20)
    time.sleep(randnumb)
    aktuelle_zeit1 = time.time()
    print("\nBewegung")
    tasten_eingabe()
