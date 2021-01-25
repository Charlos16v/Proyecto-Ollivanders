class GildedRose():
    def __init__(self, items):
        self.items = items



class Inventory(GildedRose):
    def update_quality(self):
        for item in self.items:
            item.update_quality()



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Updateable():
    def update_quality():
        pass

class NormalItem(Item, Updateable):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setSell