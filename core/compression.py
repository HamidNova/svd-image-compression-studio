import numpy as np
from core.svd_compressor import apply_svd


def calculate_k_from_compression(channel, compression):

    m, n = channel.shape

    k = (
        (1 - compression)
        *
        (m*n)
        /
        (m+n+1)
    )

    k = int(k)

    k = max(k,1)

    k = min(k, min(m,n))

    return k


def compress_by_percentage(image_matrix, compression):

    channel = image_matrix[:,:,0]

    k = calculate_k_from_compression(
        channel,
        compression
    )

    channels=[]

    for i in range(3):

        channel = image_matrix[:,:,i]

        U,S,VT = apply_svd(channel)

        compressed = (
            U[:,:k]
            @ np.diag(S[:k])
            @ VT[:k,:]
        )

        channels.append(compressed)

    return np.stack(
        channels,
        axis=2
    ), k
