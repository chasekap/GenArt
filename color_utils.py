import re
import numpy as np 
class Color: 

    def __init__(self, b, g, r, ratio): 
        self.b = b 
        self.g = g 
        self.r = r 
        self.ratio = ratio 
    
    def print_RGB(self):
        print("Red:", self.r)
        print("Green:", self.g)
        print("Blue:", self.b)

def load_palettes(path: str,exclude_white= True, exclude_black= False) -> dict: 
   
    colors = {}
    curr  = None
    currsum = 0 
    f = open(path, "r")

    for line in f: 
        if line[0] != '(':
            if curr: 
                for color in colors[curr]: 
                    color.ratio /= currsum  
                    color.ratio = color.ratio
            curr = line 
            currsum = 0 
        else:
            nums = re.findall(r'[0-9]+',line)
            try: 
                color = Color(int(nums[0]),int(nums[1]),
                int(nums[2]),int(nums[3]))
                if exclude_white and 675 <= int(nums[0]) + int(nums[1]) + int(nums[2]): 
                    continue 
                if exclude_black and int(nums[0]) + int(nums[1]) + int(nums[2]) < 110: 
                    continue 
                currsum += int(nums[3])
            except: 
                print("Invalid Color:", nums)
            if curr not in colors: 
                colors[curr] = []
            colors[curr].append(color)    
    for color in colors[curr]: 
                    color.ratio /= currsum 
                    color.ratio = color.ratio
    return colors
def color_dist(palette): 
    return [color.ratio for color in palette]

def color_from_palette(palette,distro): 
    return np.random.choice(palette,p=distro)