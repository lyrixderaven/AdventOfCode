from inputs import SECOND

dimensionstrings = SECOND.dimensionstrings

class packerl:
    l = None
    w = None
    h = None

    def __init__(self, dimensions):
        self.l = int(dimensions.split('x')[0])
        self.w = int(dimensions.split('x')[1])
        self.h = int(dimensions.split('x')[2])

    def wrapping_size(self):
        return 2 * self.l * self.w + 2 * self.w * self.h + 2 * self.h * self.l + self.smallest_side()

    def smallest_side(self):
        dims = [self.l,self.w,self.h]
        return dims.pop(dims.index(min(dims))) * dims.pop(dims.index(min(dims)))

    def smallest_perimeter(self):
        dims = [self.l,self.w,self.h]
        return dims.pop(dims.index(min(dims))) * 2 + dims.pop(dims.index(min(dims))) * 2

    def volume(self):
        return self.l * self.w * self.h

    def ribbon(self):
        return self.smallest_perimeter() + self.volume()


alle_packerlsizes = [packerl(dimstring).wrapping_size() for dimstring in dimensionstrings]
summe_size = sum(alle_packerlsizes)

alle_ribbons = [packerl(dimstring).ribbon() for dimstring in dimensionstrings]
summe_ribbons = sum(alle_ribbons)

print summe_size, summe_ribbons
