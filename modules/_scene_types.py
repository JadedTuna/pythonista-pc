class Vector3(object):
    def __eq__(self, other):
        return (isinstance(other, Vector3) and
                ((self.x == other.x) and (self.y == other.y)) and
                (self.z == other.z)
                )

    def __getitem__(self, index):
        return self.as_tuple()[index]

    def __getstate__(self):
        return self.as_tuple()

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        for i in self.as_tuple():
            yield i

    def __len__(self):
        return 3

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return "Vector3(x=%s, y=%s, z=%s)" % self.as_tuple()

    def __setitem__(self, index, value):
        setattr(self, {0: "x", 1: "y", 2: "z"}[index], value)

    def __setstate__(self, state):
        x, y, z = state
        self.x = x
        self.y = y
        self.z = z

    def as_tuple(self):
        return (self.x, self.y, self.z)

    def todict(self):
        return {'x': self.x, 'y': self.y, 'z': self.z}

class Rect(object):
    def __contains__(self, item):
        tx, ty = item
        if self.x <= tx <= self.x + self.w:
            if self.y <= ty <= self.y + self.h:
                return True
        return False

    def __eq__(self, other):
        return (isinstance(other, Rect) and
                ((self.h == other.h) and (self.w == other.w)) and
                ((self.x == other.x) and (self.y == other.y))
                )

    def __getitem__(self, index):
        return self.as_tuple()[index]

    def __getstate__(self):
        return self.as_tuple()

    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __iter__(self):
        for i in self.as_tuple():
            yield i

    def __len__(self):
        return 4

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return "Rect(x=%s, y=%s, w=%s, h=%s)" % self.as_tuple()

    def __setitem__(self, index, value):
        setattr(self, {0: "x", 1: "y", 2: "w", 3: "h"}[index], value)

    def __setstate__(self, state):
        x, y, w, h = state
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def as_tuple(self):
        return (self.x, self.y, self.w, self.h)

    def todict(self):
        return {'x': self.x, 'y': self.y, 'w': self.w, 'h': self.h}

    def center(self):
        return Point(self.w/2., self.h/2.)

class Touch(object):
    def __init__(self, x, y, prev_x, prev_y, touch_id):
        self.location = Point(x, y)
        self.prev_location = Point(prev_x, prev_y)
        self.touch_id = touch_id
        self.layer    = None

    def __eq__(self, other):
        return (isinstance(other, Touch) and
                (self.touch_id == other.touch_id)
                )

class Size(object):

    def __eq__(self, other):
        return (isinstance(other, Size) and
                ((self.w == other.w) and (self.h == other.h))
                )

    def __getitem__(self, index):
        return self.as_tuple()[index]

    def __getstate__(self):
        return self.as_tuple()

    def __init__(self, w=0.0, h=0.0):
        self.w = w
        self.h = h

    def __iter__(self):
        for i in self.as_tuple():
            yield i

    def __len__(self):
        return 2

    def __ne__(self, item):
        return not (self == item)

    def __repr__(self):
        return "Size(w=%s, h=%s)" % (self.w, self.h)

    def __setitem__(self, index, item):
        setattr(self, {0: 'w', 1: 'h'}[index], item)

    def __setstate__(self, state):
        w, h = state
        self.w = w
        self.h = h

    def as_tuple(self):
        return (self.w, self.h)

    def todict(self):
        return {'w': self.w, 'h': self.h}

class Point(object):

    def __eq__(self, other):
        return (isinstance(other, Point) and
                ((self.x == other.x) and (self.y == other.y))
                )

    def __getitem__(self, index):
        return self.as_tuple()[index]

    def __getstate__(self):
        return self.as_tuple()

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __iter__(self):
        for i in self.as_tuple():
            yield i

    def __len__(self):
        return 2

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return "Point(x=%s, y=%s)" % self.as_tuple()

    def __setitem__(self, index, value):
        setattr(self, {0: 'x', 1: 'y'}, value)

    def __setstate__(self, state):
        x, y = state
        self.x = x
        self.y = y

    def as_tuple(self):
        return (self.x, self.y)

    def todict(self):
        return {'x': self.x, 'y': self.y}

class Color(object):
    def __eq__(self, other):
        return (isinstance(other, Color) and
                ((self.r == other.r) and (self.g == other.g)) and
                ((self.b == other.b) and (self.a == other.a))
                )

    def __getitem__(self, index):
        return self.as_tuple()[index]

    def __getstate__(self):
        return self.as_tuple()

    def __init__(self, r=1.0, g=1.0, b=1.0, a=1.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __iter__(self):
        for i in self.as_tuple():
            yield i

    def __len__(self):
        return 4

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return "Color(r=%s, g=%s, b=%s, a=%s)" % self.as_tuple()

    def __setitem__(self, index, value):
        setattr(self, {0: "r", 1: "g", 2: "b", 3: "a"}[index], value)

    def __setstate__(self, state):
        r, g, b, a = state
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def as_tuple(self):
        return (self.r, self.g, self.b, self.a)

    def todict(self):
        return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}
