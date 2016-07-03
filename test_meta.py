import json
import collections
from PIL import Image
from PIL import PngImagePlugin

gp = collections.OrderedDict()
gp['name'] = 'zircles'
gp['params'] = collections.OrderedDict()
gp['params']['matrix'] = 'Lorem ipsum'
gp['params']['bsw'] = 1.258
gp['params']['csw'] = -1

print(gp)
json_gp = json.dumps(gp)
print(json_gp)

im = Image.open('dust.png')

reserved = ('interlace', 'gamma', 'dpi', 'transparency', 'aspect')
meta = PngImagePlugin.PngInfo()
meta.add_text('gb_params', json_gp)

im.save('dust.png', "PNG", pnginfo=meta)

data = json.loads( json_gp, object_pairs_hook=collections.OrderedDict)
print(data)
