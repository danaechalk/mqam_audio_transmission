import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, mu=255, B=8):
        gr.sync_block.__init__(self,
            name="mu_law_compand_quantize",
            in_sig=[np.float32],
            out_sig=[np.uint8])
        self.mu = float(mu)
        self.B = int(B)
        self.levels = 2**self.B

    def compand(self, x):
        sign = np.sign(x)
        ax = np.abs(x)
        y = sign * (np.log(1 + self.mu * ax) / np.log(1 + self.mu))
        return y

    def quantize(self, y):
        y_clip = np.clip(y, -1.0, 1.0)
        q = ((y_clip + 1.0) / 2.0) * (self.levels - 1)
        return np.round(q).astype(np.uint8)

    def work(self, input_items, output_items):
        inp = input_items[0]
        out = output_items[0]
        y = self.compand(inp)
        q = self.quantize(y)
        out[:len(q)] = q
        return len(q)

