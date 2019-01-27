from PIL import Image
from copy import deepcopy

TEST_EGG_BASE = '/home/y2kekse/images/BaseEgg.png'
TEST_EGG_PATTERN = '/home/y2kekse/images/Splotch2.png'
TEST_EGG_LIGHTING = (
    '/home/y2kekse/images/Base-Eggwith-Shadowand-Highlight.png'
)

IM_BASE = Image.open(TEST_EGG_BASE)
IM_PATTERN = Image.open(TEST_EGG_PATTERN)
IM_LIGHTING = Image.open(TEST_EGG_LIGHTING)

color_templates = {
    'base': (254, 206, 36, 255),
    'pattern': (153, 0, 80, 255),
    'highlight': (254, 221, 47, 255),
    'shadow': (177, 144, 25, 255),
    'exterior': (255, 255, 255, 0)
}
color_codes = {
    'red': (255, 0, 0, 255),
    'green': (0, 255, 0, 255),
    'blue': (0, 0, 255, 255),
    'highlight': (255, 255, 255, 255),
    'shadow': (0, 0, 0, 255)
}

def get_pixel_mask(im, template='pattern'):
    rgba_im = im.convert('RGBA')
    width, height = rgba_im.size
    pixels = []
    for w in range(width):
        for h in range(height):
            if rgba_im.getpixel((w,h)) == color_templates[template]:
                pixels.append((w,h))
    return pixels

def get_image_mask(im, mask, alpha=255):
    rgba_im = im.convert('RGBA')
    width, height = rgba_im.size
    mask_im = Image.new(
        'RGBA', (width, height),
        color=(255, 255, 255, 0)
    )
    mask_pixels = mask_im.load()
    for wh in mask:
        w, h = wh
        mask_pixels[w, h] = (255, 255, 255, alpha)
    return mask_im

def change_pixels(im, mask, color):
    pixels = im.load()
    for wh in mask:
        w, h = wh
        pixels[w, h] = color_codes[color]
    return im

def create_base(color):
    mask = get_pixel_mask(IM_BASE, template='base')
    im = change_pixels(IM_BASE, mask, color)
    return im

def add_pattern(base, pattern, color, template='pattern', alpha=255):
    mask = get_pixel_mask(pattern, template=template)
    im_mask = get_image_mask(pattern, mask, alpha=alpha)
    base.paste(color_codes[color], (0,0), im_mask)
    return base

def add_lighting(im):
    im = add_pattern(
        im, IM_LIGHTING, 'shadow',
        template='shadow', alpha=50
    )
    im = add_pattern(
        im, IM_LIGHTING, 'highlight',
        template='highlight', alpha=50
    )
    return im

if __name__ == '__main__':
    im = create_base('blue')
    im = add_pattern(im, deepcopy(IM_PATTERN), 'green')
    im = add_lighting(im)
    im.show()
