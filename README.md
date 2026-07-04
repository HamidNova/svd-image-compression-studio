# SVD Image Compression Studio

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Zero-Day-Hero/svd-image-compression-studio?style=social)](https://github.com/Zero-Day-Hero/svd-image-compression-studio)

An interactive image compression application built with **Python** and **Streamlit** using **Singular Value Decomposition (SVD)**.

The application compresses RGB images by keeping only the most significant singular values, allowing users to balance image quality and compression ratio through an intuitive web interface.

---

## Features

- Interactive Streamlit interface
- Compress RGB images using Singular Value Decomposition
- Two compression modes:
  - Component-based (k-value)
  - Compression percentage
- Fast Mode and High Quality Mode
- Automatic component selection
- Quality evaluation using:
  - Mean Squared Error (MSE)
  - Peak Signal-to-Noise Ratio (PSNR)
- Original vs Compressed comparison
- Difference Map visualization
- Singular Values Importance Plot
- Compression statistics
- Download compressed image

---

## Tech Stack

- Python
- Streamlit
- NumPy
- Pillow (PIL)
- Matplotlib
- OpenCV
- scikit-image
- Pandas

---

## How It Works

Each RGB channel is treated as an independent matrix.

For every channel:

```
A = U Σ VT
```

Only the first **k** singular values are preserved.

```
A ≈ Uk Σk VkT
```

Reducing **k** decreases storage requirements while maintaining most of the important visual information.

---

## Project Structure

```text
SVD_Image_Compression_Studio
│
├── app.py
│
├── core
│   ├── svd_compressor.py
│   ├── compression.py
│   └── metrics.py
│
├── utils
│   ├── image_utils.py
│   └── visualization.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Zero-Day-Hero/svd-image-compression-studio.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Performance Metrics

The application evaluates compression quality using:

- Mean Squared Error (MSE)
- Peak Signal-to-Noise Ratio (PSNR)

It also reports:

- Original image size
- Compressed image size
- Compression ratio
- Number of retained singular values

---

## Highlights

- From-scratch SVD-based image compression
- Interactive visualization tools
- Adjustable compression level
- Educational implementation of Linear Algebra concepts
- Real-time image reconstruction
- Automatic quality evaluation

---

## Future Improvements

- GPU acceleration
- Support for grayscale optimization
- Batch image compression
- JPEG quality comparison
- Additional quality metrics (SSIM)

---

## License

MIT License

---

## Author

**Hamidreza Mirzaei**

GitHub: https://github.com/Zero-Day-Hero