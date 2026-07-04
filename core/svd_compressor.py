import numpy as np


def apply_svd(channel):

    U, S, VT = np.linalg.svd(
        channel,
        full_matrices=False
    )

    return U, S, VT


def compress_channel(channel, k):

    U, S, VT = apply_svd(channel)

    U_k = U[:, :k]

    S_k = np.diag(S[:k])

    VT_k = VT[:k, :]

    compressed = (
        U_k @ S_k @ VT_k
    )

    return compressed


def compress_image(image_matrix, k):

    channels = []

    for i in range(3):

        channel = image_matrix[:, :, i]

        compressed_channel = compress_channel(
            channel,
            k
        )

        channels.append(compressed_channel)

    compressed_image = np.stack(
        channels,
        axis=2
    )

    return compressed_image
