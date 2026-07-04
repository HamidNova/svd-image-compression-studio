from PIL import Image
import numpy as np


def load_image(uploaded_file):

    image = Image.open(uploaded_file)

    image = image.convert("RGB")

    return image


def image_to_matrix(image):

    matrix = np.array(image)

    return matrix


def matrix_to_image(matrix):

    matrix = np.clip(matrix, 0, 255)

    matrix = matrix.astype(np.uint8)

    image = Image.fromarray(matrix)

    return image


def get_image_size(image):

    width, height = image.size

    return width, height
