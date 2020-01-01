from sys import argv, stdout
from math import floor


class Layer():
    def __init__(self, width, height, data):
        self._width = width
        self._height = height
        self._data = data

    def __iter__(self):
        return iter(self._data)

    def render(self):
        offset = 0
        for i in range(self._height):
            for i in range(self._width):
                if self._data[offset] == "0":
                    stdout.write(" ")
                elif self._data[offset] == "1":
                    stdout.write("█")
                elif self._data[offset] == "2":
                    stdout.write("▒")
                offset += 1
            stdout.write("\n")


class Image():
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._layer_size = width * height
        self._layers = []

    def load(self, data):
        layer_count = int(len(data) / self._layer_size)
        for offset in range(0, len(data), self._layer_size):
            layer_data = data[offset:offset + self._layer_size]
            layer = Layer(self._width, self._height, layer_data)
            self._layers.append(layer)

    def checksum(self):
        min_zero, check_sum = self.compute_layer_checksum(self._layers[0])
        for layer in self._layers[1:]:
            zero, _sum = self.compute_layer_checksum(layer)
            if min_zero > zero:
                min_zero = zero
                check_sum = _sum
        return check_sum

    def compute_layer_checksum(self, data):
        counts = dict()
        for p in data:
            counts.setdefault(p, 0)
            counts[p] += 1
        return counts.get("0", 0), counts.get("1", 0) * counts.get("2", 0)

    def flatten(self):
        data = []
        for pixel_group in zip(*[l for l in self._layers]):
            for pixel in pixel_group:
                if pixel == "0":
                    data.append("0")
                    break
                elif pixel == "1":
                    data.append("1")
                    break
                elif pixel == "2":
                    pass
        return Layer(self._width, self._height, "".join(data))

    def render(self):
        layer = self.flatten()
        layer.render()



def main(path):
    with open(path, 'r') as fd:
        w, h, data = fd.read().split(":")
        image = Image(int(w), int(h))
        image.load(data[:-1])
        print("Checksum:", image.checksum())
        image.render()



if __name__ == "__main__":
    main(argv[-1])

