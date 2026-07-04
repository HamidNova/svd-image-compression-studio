import matplotlib.pyplot as plt
import numpy as np


def show_comparison(original, compressed):

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(10,5)
    )

    axes[0].imshow(
        original.astype(np.uint8)
    )

    axes[0].set_title(
        "Original Image"
    )

    axes[0].axis("off")

    axes[1].imshow(
        compressed.astype(np.uint8)
    )

    axes[1].set_title(
        "Compressed Image"
    )

    axes[1].axis("off")

    return fig


def show_difference(original, compressed):

    difference = np.abs(
        original - compressed
    )

    difference = difference.astype(
        np.uint8
    )

    fig, ax = plt.subplots(
        figsize=(6,5)
    )

    ax.imshow(
        difference
    )

    ax.set_title(
        "Difference Map"
    )

    ax.axis("off")

    return fig


def plot_singular_values(channel):

    U, S, VT = np.linalg.svd(
        channel,
        full_matrices=False
    )

    fig, ax = plt.subplots(
        figsize=(8,4)
    )

    ax.plot(
        S
    )

    ax.set_title(
        "Singular Values"
    )

    ax.set_xlabel(
        "Component"
    )

    ax.set_ylabel(
        "Value"
    )

    return fig
