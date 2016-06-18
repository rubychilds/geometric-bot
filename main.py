# #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# System / third party modules
import sys
import random
import datetime
import importlib

# Graph modules
drawing_modules = {
    # name, probability
    # 'algorithm_chrysanthemum': 0, # Disabled
    'algorithm_param_eq': 1,
    'algorithm_perlin_brush': 1,
    'algorithm_drawing_machine': 2,
    'algorithm_gingko': 2,
    'algorithm_zircles': 3,
}
temp = []
for name, prob in drawing_modules.items():
    if prob > 0:
        temp.extend( [name] * prob )
current = random.choice( temp )
# print(current)
# sys.exit()

# Import my modules
# from mod import algorithm_param_eq
m = importlib.import_module("mod.%s" % current)
from mod import tweet

def main():
    # Launch render module
    ims, filename, footline = m.render()
    ims.write_to_png( './output/'+filename )

    # Tuitear imagen
    print(filename)
    print(footline)
    tweet.withImage( './output/'+filename, footline+' #generative #geometric #ProceduralArt #python #bot' )

if __name__ == '__main__':
    print('Main time: '+str(datetime.datetime.now()))
    main()
