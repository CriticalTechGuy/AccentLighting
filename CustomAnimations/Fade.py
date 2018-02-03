from bibliopixel.animation import BaseStripAnim
import numpy as np
from bibliopixel import util


class Fade(BaseStripAnim):
    def __init__(self, layout, *, range=(255, 0), mask=(1, 1, 1), **kwds):
        super().__init__(layout, **kwds)
        self.range = range
        self.mask = mask

    def pre_run(self):
        env = np.linspace(self.range[0], self.range[1], len(self.color_list),
                          endpoint=False, dtype=int)
        self.color_list[:] = np.outer(env, self.mask)
        print(self.color_list)
