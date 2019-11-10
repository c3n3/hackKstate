import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.ili9341 as ili9341


class lcdInterface():
    def __init__(self):
        BORDER = 20
        # Configuration for CS and DC pins (these are PiTFT defaults):
        cs_pin = digitalio.DigitalInOut(board.CE0)
        dc_pin = digitalio.DigitalInOut(board.D24)
        reset_pin = digitalio.DigitalInOut(board.D25)

        # Config for display baudrate (default max is 24mhz):
        BAUDRATE = 24000000

        # Setup SPI bus using hardware SPI:
        spi = board.SPI()

        self.disp = ili9341.ILI9341(spi, rotation=90, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE)

        self.lines = []
        self.width = 320
        self.heigth = 240
        self.image = Image.new('RGB', (self.width, self.heigth))
        self.font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)
        # Get drawing object to draw on image.
        self.lines.append("8 + 9 * 7")

    def graph3D(self, function):
        for x in range(0, self.width):
            for y in range(0, self.height):
                function(x, y) # print the z value of the color
                # use Image.Draw.point((x, y), color)

    def graph1D(self, function):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle((0, 0, self.width, self.heigth), fill=(0, 0, 0))
        drawGrid(draw)
        for x in range(0, self.width):
            draw.point((x, 20*(120 - function(x))), fill=(255, 0, 0)) # plot the point if within the range
            # use Image.Draw.point((x, y), color)
        self.disp.image(self.image)

    def drawGrid(self, draw):
        for x in range(0, self.width):
            draw.point((x, 120), fill=(100,100,100))
        for x in range(0, self.heigth):
            draw.point((160, x), fill=(100,100,100))

    def setFirstLine(self, string):
        self.lines[0] = string
        _update()

    def _update(self):
        draw = ImageDraw.Draw(self.image)

        draw.rectangle((0, 0, self.width, self.heigth), fill=(0, 0, 0))
        for x in range(1, len(self.lines) + 1):
            print("something")
            draw.text((4, (244 - (x*9 + x*30))), self.lines[x - 1],font=self.font, fill=(255, 255, 0, 255))
            #draw.text((width//2 - font_width//2, height//2 - font_height//2),
            #text, font=font, fill=(255, 255, 0))
        self.disp.image(self.image)
    def clear(self):
        self.lines = []
        self.lines.append("")
        self._update()

    def shiftRowsUp(self):
        while (len(self.lines) >= 6):
            self.lines.pop()
        temp = []
        temp.append("")
        for x in self.lines:
            temp.append(x)
        self.lines = temp
        print(temp)
        self._update()
    def execute(self, result):
        self.lines.insert(0, "= " + result)
        self.shiftRowsUp()

    def text(string):
        draw = ImageDraw.Draw(self.image)
        draw.text((10,10), self.lines[x - 1],font=self.font, fill=(255, 255, 0, 255))
        draw.rectangle((0, 0, self.width, self.heigth), fill=(0, 0, 0))
        self.disp.image(self.image)
