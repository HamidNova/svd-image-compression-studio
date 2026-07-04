import numpy as np
from skimage.metrics import peak_signal_noise_ratio


def calculate_mse(original, compressed):

    mse = np.mean(
        (original - compressed) ** 2
    )

    return mse


def calculate_psnr(original, compressed):

    psnr = peak_signal_noise_ratio(
        original,
        compressed,
        data_range=255
    )

    return psnr


def calculate_compression_ratio(
        original_size,
        compressed_size
):

    ratio = (
        1 - (compressed_size / original_size)
    ) * 100

    return ratio
