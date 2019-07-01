import tkinter as tk

# Define class for a map tile
class Tile:
    type = "X";
    value = 0;

#Print a 1-D map
def print_map(map_in):
    for x in map_in:
        print(x.value, end="");


#Create a map
tile_array = [];
for i in range(5):
    newTile = Tile();
    newTile.value = i;
    tile_array.append(newTile);

print_map(tile_array);
