import cairo, math,random 
from color_utils import load_palettes, color_dist, color_from_palette
import numpy as np 
W = 995
H = 995




def concentric():
    radius = 0
    thickness = 20
    STD = 1 
    palettes = load_palettes("palettes.txt",exclude_black=True)
    palette = random.choice(list(palettes.keys()))
    print(palette)
    curr_palette = palettes[palette]
    distro = color_dist(curr_palette)

    

    with cairo.SVGSurface("concentrics/concentric015.svg", W, H) as surface:
        rng_gen = np.random.default_rng()
        radius = rng_gen.normal(30,STD)
        context = cairo.Context(surface)
        context.set_source_rgb(240/255,240/255,240/255)
        context.rectangle(0,0,W,H)
        context.fill()
        #context.stroke()
        while radius < W // 2.5: 
            color = color_from_palette(curr_palette,distro)
            context.set_source_rgb(color.r/255,color.g/255,color.b/255)
            context.arc(W//2, H//2, radius, -2*math.pi, 0)
            context.set_line_width(thickness)
            context.stroke()
            radius += rng_gen.normal(80,3)
            thickness -= rng_gen.normal(2,5)
            if thickness <= 5: 
                break 
            STD += 1
def genStar(context, x, y,curr_palette,distro): 

    context.set_source_rgb(1,1,1)
    context.arc(x, y, 1, -2*math.pi, 0)
    context.fill()
    context.stroke()
    color = color_from_palette(curr_palette,distro)
    context.set_source_rgb(color.r/255,color.g/255,color.b/255)
    red = color.r 
    green = color.g
    blue = color.b 
    rad = 1
    while red > 50 or blue > 50 or green > 50: 
            context.arc(x, y, rad, -2*math.pi, 0)
            context.stroke()
            rad += 1 
            red -= 50 
            green -= 50 
            blue -= 50 
            context.set_source_rgb(red/255,green/255,blue/255)
    
def stars(): 
     with cairo.SVGSurface("concentrics/star.svg", 500, 500) as surface:
         palettes = load_palettes("palettes.txt",exclude_black=True)
         palette = random.choice(list(palettes.keys()))
         print(palette)
         curr_palette = palettes[palette]
         distro = color_dist(curr_palette)
         
         context = cairo.Context(surface)
         context.set_line_width(1)
         context.set_source_rgb(0,0,0)
         context.rectangle(0,0,500,500)
         context.fill()
         for i in range(500): 
             for j in range(500): 
                 rando = np.random.random()
                 if rando < (1 / 2500): 
                     genStar(context,i,j,curr_palette,distro)
def circline(y, curr_palette, context,odds):
         
         
         xshift = 160
         rng_gen = np.random.default_rng()
         rad = 55
         
         
        
         print(y)
         distro = color_dist(curr_palette) 
         
         #context.set_line_width(5)
         while (xshift) < (1280 * 2): 
             radius = rng_gen.normal(40,5)
             color = color_from_palette(curr_palette,distro)
             context.set_source_rgb(color.r/255,color.g/255,color.b/255)
              
            
            
             rando = np.random.random()
             if rando < (odds): 
                context.arc(xshift, y, radius, -2*math.pi, 0)
                context.fill() 
             
             xshift += 160
             
def circlines(n,y_delta):
    palettes = load_palettes("palettes.txt",exclude_black=True)
    palette = random.choice(list(palettes.keys()))
    print(palette)
    with cairo.SVGSurface("strlights/str.svg", 1280 * 2, 1280 * n / 5 ) as surface:
        context = cairo.Context(surface)
        context.set_source_rgb(252/255,252/255,252/255)
        context.rectangle(0,0,1280 * 2,y_delta * (n + 1) )
         
        context.fill()  
        curr_palette = palettes[palette]
       
        for i in range(0,n): 
            circline((y_delta * (i + 1)), curr_palette, context,1)
circlines(5, 250/2)