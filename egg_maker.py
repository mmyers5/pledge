from PIL import Image
from copy import deepcopy
from random import randint
import os
import time

color_templates = {
    'base': (254, 206, 36, 255),
    'pattern': (153, 0, 80, 255),
    'highlight': (254, 221, 47, 255),
    'shadow': (177, 144, 25, 255)
}

def hex_to_rgba(hex, alpha=255):
    h = hex.strip('#')
    rgb = [int(h[i:i+2], 16) for i in (0, 2 ,4)]
    return tuple(rgb + [alpha])

def get_pixel_mask(im, template='pattern'):
    width, height = im.size
    pixels = []
    for w in range(width):
        for h in range(height):
            if im.getpixel((w,h)) == color_templates[template]:
                pixels.append((w,h))
    return pixels

def change_pixels(im, pixel_mask, color):
    pixels = im.load()
    for w, h in pixel_mask:
        pixels[w, h] = color
    return im

def create_image(image_file, color, template='pattern'):
    template_image = Image.open(image_file)
    pixel_mask = get_pixel_mask(template_image, template=template)
    if template != 'base':
        template_image = Image.new('RGBA', template_image.size, (0,0,0,0))
    change_pixels(template_image, pixel_mask, color)
    return template_image


class Egg:
    def __init__(self, base_file):
        self.base_file = base_file
        self.raw_base = Image.open(self.base_file)
        self.image = deepcopy(self.raw_base)

    def set_base(self, color):
        # never have transparent base, ever.
        if color[-1] != 255:
            color = color[:-1] + (255,)
        self.image = create_image(self.base_file, color, template='base')

    def add_pattern(self, pattern_file, color):
        pattern = create_image(pattern_file, color, template='pattern')
        self.image = Image.alpha_composite(self.image, pattern)

    def add_lighting(self, lighting_file):
        shadow = create_image(
            lighting_file, (0, 0, 0, 100), template='shadow'
        )
        self.image = Image.alpha_composite(self.image, shadow)
        highlight = create_image(
            lighting_file, (255, 255, 255, 100), template='highlight'
        )
        self.image = Image.alpha_composite(self.image, highlight)


class EggGenerator:
    def __init__(self, images, base_file, lighting_file):
        self.base_file =  base_file
        self.lighting_file = lighting_file
        self.images = images
        #self.images.remove(base_file)
        #self.images.remove(lighting_file)

    def get_random_color(self):
        return (
            randint(0,255),
            randint(0,255),
            randint(0,255),
            randint(100,255)    # avoid very transparent patterns
        )

    def get_random_pattern(self):
        n_images = len(self.images)
        r = randint(0, n_images-1)
        return '{}/{}'.format(self.images_dir, self.images[r])

    def create_random_egg(self, n=1, layers=1, save=False):
        for e in range(n):
            egg = Egg(self.base_file)
            egg.set_base(self.get_random_color())
            for p in range(layers):
                egg.add_pattern(
                    self.get_random_pattern(),
                    self.get_random_color()
                )
            egg.add_lighting(self.lighting_file)
            if save:
                self.save_egg(egg, tag='{}_{}'.format(p,e))

    def save_egg(self, egg, tag='', save_file=None):
        if save_file is None:
            posix = int(time.time())
            save_file = '{}_{}.png'.format(posix, tag)
        egg.save(save_file)

    def create_specific_egg(self, base_color, pattern_file, pattern_color):
        egg = Egg(self.base_file)
        egg.set_base(base_color)
        egg.add_pattern(pattern_file, pattern_color)
        egg.add_lighting(self.lighting_file)
        return egg

if __name__ == '__main__':
    egg = Egg('/Users/mmyers/pledge/images/BaseEgg.png')
    egg.set_base((0, 0, 255, 255))
    pattern_file = '/Users/mmyers/pledge/images/Splotch2.png'
    lighting_file = (
        '/Users/mmyers/pledge/images/Base-Eggwith-Shadowand-Highlight.png'
    )
    egg.add_pattern(pattern_file, (0, 255, 0, 255))
    egg.add_lighting(lighting_file)
    egg.image.show()
