# geometric-bot
**Python3** experimental bot that generates randomly geometric-like images. **Always WIP**. This is my very first project with Python3 so be merciful with WIP parts or _not-so-good-pactices_ ;)

Resulting images are posted in <https://twitter.com/@GeometricBot>

<img src="output/sample-output.png">

# modules used
```
cairo
collections
colorsys
datetime
importlib
math
noise
os
random
yaml -> PyYAML (3.11)
sys
```

Modules starting with `mod/algorithm` are the core of each type of geometric deisgn, rest of modules ( `draw, name, tweet` ) are utilities or general functionallities.

# config
The config settings and API keys are stored in the `config.yml` in the root of the project, a `config.yml.sample` is provided.

# Attribution-NonCommercial 4.0 International

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">GeometricBot</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/carloscabo/geometric-bot" property="cc:attributionName" rel="cc:attributionURL">Carlos Cabo</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/carloscabo/geometric-bot" rel="dct:source">https://github.com/carloscabo/geometric-bot</a>.
