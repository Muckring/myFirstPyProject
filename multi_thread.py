import threading
import time

def get_up() -> None:
    time.sleep(4)
    print("I got up")

def cook_breakfast() -> None:
    time.sleep(10)
    print("I cooked breakfast")

def go_to_work(attribute: str) -> None:
    time.sleep(7)
    print(f'I going to my {attribute} work')



task1 = threading.Thread(target=get_up)
task1.start()

task2 = threading.Thread(target=cook_breakfast)
task2.start()

task3 = threading.Thread(target=go_to_work, args=("bloody",))
task3. start()

task1.join()
task2.join()
task3.join()

print("And this is gonna last for perpetuity or eternity")