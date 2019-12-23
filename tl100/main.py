import pexpect

def c(the_code):
    return "char-write-req 0x0014 " + the_code


class TL100Lamp:

    def __init__(self, device_id="57:4C:42:75:CF:49"):
        self.id = device_id

    def connect(self):
        handle = pexpect.spawn("gatttool -I")
        handle.sendline("connect {0}".format(self.id))
        handle.expect("Connection successful", timeout=10)
        return handle

    def disconnect(self):
        l = self.connect()
        l.sendline("disconnect")

    def send(self, line):
        l = self.connect()
        l.sendline(c(line))
        l.sendline("disconnect")

    def start_solar_mode(self):
        l = self.connect()
        l.sendline(c("FEEF0A09ABAA04370132550D0A"))
        l.sendline(c("FEEF0A0AABAA0531016451550D0A"))
        l.sendline("disconnect")

    def stop_solar_mode(self):
        l = self.connect()
        l.sendline(c("FEEF0A09ABAA04350130550D0A"))
        l.sendline("disconnect")

    def start_color_mode(self):
        l = self.connect()

        # initialize color mode
        l.sendline(c("FEEF0A09ABAA04370231550D0A"))

        # pause scene
        l.sendline(c("FEEF0A09ABAA04340030550D0A"))
        l.sendline(c("FEEF0A09ABAA04300236550D0A"))

        # max color light
        l.sendline(c("FEEF0A0AABAA0531026452550D0A"))

        l.sendline("disconnect")

    def set_color(self, rgb_hex):

        l = self.connect()
        l.sendline(c("FEEF0A0BABAA0632" + rgb_hex.upper() + "CB550D0A"))
        l.sendline("disconnect")

    def set_color_brightness(self, val=0):

        if val in range(0, 101):
            volume = hex(val * 65607 + 33568341).lstrip('0x')
            l = self.connect()
            l.sendline(c("FEEF0A0AABAA05310" + volume.upper() + "0D0A"))
            l.sendline(c("FEEF0A0AABAA0531026452550D0A"))

    def stop_color_mode(self):
        l = self.connect()

        l.sendline(c("FEEF0A09ABAA04350233550D0A"))
        l.sendline("disconnect")

    def run_scene(self, scene_name="None"):

        scenes = {
            "None":        "FEEF0A09ABAA04340030550D0A",
            "Rainbow":     "FEEF0A09ABAA04340232550D0A",
            "RainbowSlow": "FEEF0A09ABAA04340333550D0A",
            "Fusion":      "FEEF0A09ABAA04340434550D0A",
            "Pulse":       "FEEF0A09ABAA04340535550D0A",
            "Wave":        "FEEF0A09ABAA04340636550D0A",
            "Chill":       "FEEF0A09ABAA04340737550D0A",
            "Action":      "FEEF0A09ABAA04340838550D0A",
            "Forest":      "FEEF0A09ABAA04340939550D0A",
            "Summer":      "FEEF0A09ABAA04340A3A550D0A"}

        if scene_name in scenes:
            l = self.connect()
            l.sendline(c("FEEF0A09ABAA04370231550D0A"))
            l.sendline(c(scenes[scene_name]))
            l.sendline(c("FEEF0A09ABAA04300236550D0A"))
            l.sendline("disconnect")

    def stop_scene(self):
        self.stop_color_mode()
