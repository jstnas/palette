from PIL import Image
import os


class Palette:
    _image_path: str = ''
    _pixels: list = []
    _palette: dict = {}

    def get(self, image_path):
        self._image_path = image_path
        self.get_pixels()
        self.get_palette()
        self.save_palette()

    def get_pixels(self):
        with Image.open(self._image_path, 'r') as image_file:
            self._pixels = list(image_file.getdata())
            return

    def get_palette(self):
        palette = {}
        for pixel in self._pixels:
            if pixel in palette:
                palette[pixel] += 1
            else:
                palette[pixel] = 1
        self._palette = palette
        return

    def save_palette(self):
        file_name = os.path.splitext(self._image_path)[0]
        with open(f'{file_name}.txt', 'w') as palette_file:
            for colour in sorted(self._palette, key=self._palette.__getitem__, reverse=True):
                palette_file.write(f'{Palette.rgb_to_hex(colour)} {self._palette[colour]}\n')
        return

    @staticmethod
    def rgb_to_hex(rgb: tuple):
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
