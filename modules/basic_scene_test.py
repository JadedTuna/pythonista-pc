from scene import *

class MyScene (Scene):
    def setup(self):
        pass

    def draw(self):
        background(0, 0, 1)
        fill(1, 0, 0)
        for touch in self.touches.values():
            ellipse(touch.location.x - 50, touch.location.y - 50,
                    100, 100)

run(MyScene())
