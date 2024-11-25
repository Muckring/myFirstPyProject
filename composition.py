# This is a lesson in composition


class Hand():
    def __init__(self, quality: str, finger_size: int):
        self.quality = quality
        self.fingers = [Finger(finger_size) for finger in range(5)]

    def display_hand(self):
        return f'{self.quality} {self.fingers[0].length}cm hand'


class Finger():
    
    def __init__(self, length: int):
        self.length = length
        
   

hand = Hand('rugged', 23)

print(hand.display_hand())