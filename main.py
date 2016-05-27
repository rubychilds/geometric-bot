# #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# System / third party modules
import sys
import random
import datetime
import importlib

# Graph modules
drawing_modules = {
    'algorithm_param_eq': 1,
    'algorithm_perlin_brush': 1,
    'algorithm_chrysanthemum': 1
}
current, prob = random.choice(list(drawing_modules.items()))
print(current)
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
    tweet.withImage( './output/'+filename, footline+' #generative #geometric #ProceduralArt #python #bot' )

if __name__ == '__main__':
    print('Main time: '+str(datetime.datetime.now()))
    main()
