# tl100

Hacks for Beurer TL100 lamp. Requires gatttool.

## install

```bash
$ pip install tl100
```

## example

```python

import time

from tl100 import TL100Lamp

lamp = TL100Lamp()

lamp.start_solar_mode()
time.sleep(1)
lamp.stop_solar_mode()
time.sleep(1)

lamp.start_color_mode()
lamp.set_color("FFFF00")
lamp.set_color_brightness(1)
time.sleep(1)
lamp.set_color_brightness(50)
time.sleep(1)
lamp.set_color_brightness(100)
time.sleep(1)
lamp.stop_color_mode()
time.sleep(1)

lamp.run_scene("Rainbow")
time.sleep(10)
lamp.stop_scene()

```

## scenes

* None
* Rainbow
* RainbowSlow
* Fusion
* Pulse
* Wave
* Chill
* Action
* Forest
* Summer