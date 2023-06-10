import cv2

class Button:
    def __init__(self, pos, width, height, no):
        self.pos = pos
        self.width = width
        self.height = height
        self.no = no

    def draw(self, frame):
        cv2.rectangle(frame, self.pos, (
            self.pos[0] + self.width, self.pos[1] + self.height), (255, 255, 255), cv2.FILLED)
        cv2.rectangle(frame, self.pos, (
            self.pos[0] + self.width, self.pos[1] + self.height), (0, 0, 0), 3)
        cv2.putText(frame, self.no, (self.pos[0] + 20, self.pos[1] + 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 1)
        

    def checkClick(self, frame, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(frame, self.pos, (
                self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225), cv2.FILLED)
            cv2.rectangle(frame, self.pos, (
                self.pos[0] + self.width, self.pos[1] + self.height), (0, 0, 0), 3)
            cv2.putText(
                frame, self.no, (self.pos[0] + 20, self.pos[1] + 50), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 0), 2)
            
            return True
        else:
            return False