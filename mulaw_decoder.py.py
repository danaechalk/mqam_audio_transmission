import numpy as np
from gnuradio import gr

MU = 255.0

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="mu-law decoder",
            in_sig=[np.uint8],    # byte input
            out_sig=[np.float32], # float output
        )

    def work(self, input_items, output_items):
        y = input_items[0].astype(np.float32)

        # scale bytes 0-255 → [-1, 1]
        y = (y - 128.0) / 128.0

        # μ-law expansion (inverse)
        sign = np.sign(y)
        abs_y = np.abs(y)

        x = sign * (1.0 / MU) * ((1.0 + MU)**abs_y - 1.0)

        output_items[0][:] = x
        return len(output_items[0])



