from Zone import *
from json_serialize import *

class Table:
    def __init__(self, config_file = ''):
            self.root_zone = None
            self.zones_map = {}
            self.red_robots = []
            self.blue_robots = []
            self.elements = []

    def set_root(self, zone):
        self.root_zone = zone
        self.add_zone(zone)
        
    def add_zone(self, zone):
        self.zones_map[zone.id] = zone
        

    def __repr__(self):
        res = 'Table, zones: \n'
        for zone in self.zones_map.values():
            res += str(zone) + '\n'
        return res

  

if __name__ == '__main__':   
    background = Zone('background')
    square = [(0,0), (3000,0), (3000,2000), (0,2000)]
    background.set_polygon(square)
    up_left = Zone('start_red')
    square = [(0,0), (50,0), (50,50), (0,50)]
    up_left.set_polygon(square)
    up_right = Zone('start_blue')
    square = [(3000-50,0), (3000,0), (3000,50), (3000-50,50)]
    up_right.set_polygon(square)

    background.add_child(up_left.id)
    background.add_child(up_right.id)

    table = Table()
    table.set_root(background)
    table.add_zone(up_left)
    table.add_zone(up_right)
    print table
