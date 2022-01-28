import logging
import tkinter as tk
from connectors.binance_futures import BinanceFuturesClient

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)


logger.addHandler(stream_handler)
logger.addHandler(file_handler)



if __name__ == '__main__':
    binance = BinanceFuturesClient(
        '9aab64ab8fea14e0064c48b189c17f8eccc5a60b2a485c06f73d0e4233695c53',
        '7b8b4a0d0fb9c307c70d3ed6fdf8b0702173bf9c361b35c10607f7009dd92360',
        True
    )
    root = tk.Tk()
    root.mainloop()