import io
import streamlit as st
import numpy as np


from PIL import Image

from utils.image_utils import (
    load_image,
    image_to_matrix,
    matrix_to_image
)

from core.svd_compressor import compress_image

from core.compression import (
    compress_by_percentage
)

from core.metrics import (
    calculate_mse,
    calculate_psnr
)

from utils.visualization import (
    show_comparison,
    show_difference,
    plot_singular_values
)


st.set_page_config(
    page_title="SVD Image Compression Studio",
    layout="wide"
)

st.title(
    "SVD Image Compression Studio"
)

st.write(
    "Image compression using Singular Value Decomposition (SVD)"
)

uploaded_file = st.file_uploader(
    "Upload Image",
    type=[
        "jpg",
        "png",
        "jpeg"
    ]
)

if uploaded_file:

    image = load_image(
        uploaded_file
    )

    original_matrix = image_to_matrix(
        image
    )

    st.subheader(
        "Original Image"
    )

    st.image(
        image,
        width=400
    )

    st.sidebar.title(
        "Compression Settings"
    )

    processing_mode = st.sidebar.selectbox(
        "Processing Mode",
        [
            "Fast (Recommended)",
            "High Quality (Slow)"
        ]
    )

    if processing_mode == "Fast (Recommended)":

        max_size = 1024

    else:

        max_size = 4096

    image = image.copy()

    image.thumbnail(
        (max_size, max_size),
        Image.Resampling.LANCZOS
    )

    original_matrix = image_to_matrix(
        image
    )

    mode = st.sidebar.radio(
        "Choose Method",
        [
            "Components",
            "Compression Percentage"
        ]
    )

    if mode == "Components":

        k = st.sidebar.slider(
            "Number of Components",
            min_value=5,
            max_value=300,
            value=50
        )

        compress_button = st.sidebar.button(
            "Compress"
        )

    else:

        percentage = st.sidebar.slider(
            "Compression Percentage (%)",
            0,
            99,
            50
        )

        compress_button = st.sidebar.button(
            "Compress"
        )

    if compress_button:

        with st.spinner(
            "Applying SVD..."
        ):

            if mode == "Components":

                compressed_matrix = compress_image(
                    original_matrix,
                    k
                )

            else:

                compressed_matrix, selected_k = compress_by_percentage(
                    original_matrix,
                    percentage / 100
                )

            compressed_image = matrix_to_image(
                compressed_matrix
            )

            original_size = uploaded_file.size

        st.success(
            "Compression Completed!"
        )

        col1,col2 = st.columns(2)


        with col1:

            st.subheader(
                "Compressed Image"
            )

            st.image(
                compressed_image,
                width=400
            )

            download_buffer = io.BytesIO()

            compressed_image.save(
                download_buffer,
                format="JPEG",
                quality=95
            )

            compressed_size = len(
                download_buffer.getvalue()
            )

            compression_ratio = (
                    1 -
                    (compressed_size / original_size)
            ) * 100

            st.download_button(

                label="Download Compressed Image",

                data=download_buffer.getvalue(),

                file_name="compressed_image.jpg",

                mime="image/jpeg"

            )

        mse = calculate_mse(
            original_matrix,
            compressed_matrix
        )

        psnr = calculate_psnr(
            original_matrix,
            compressed_matrix
        )

        st.subheader(
            "Quality Metrics"
        )

        m1,m2 = st.columns(2)

        m1.metric(
            "MSE",
            round(mse,2)
        )

        m2.metric(
            "PSNR",
            round(psnr,2)
        )

        st.subheader(
            "Compression Statistics"
        )

        s1, s2, s3 = st.columns(3)

        s1.metric(
            "Original Size",
            f"{original_size / 1024:.2f} KB"
        )

        s2.metric(
            "Compressed Size",
            f"{compressed_size / 1024:.2f} KB"
        )

        s3.metric(
            "Compression",
            f"{compression_ratio:.2f}%"
        )

        st.subheader(
            "Comparison"
        )

        fig = show_comparison(
            original_matrix,
            compressed_matrix
        )

        st.pyplot(
            fig
        )

        st.subheader(
            "Difference Map"
        )

        diff_fig = show_difference(
            original_matrix,
            compressed_matrix
        )

        st.pyplot(
            diff_fig
        )

        st.subheader(
            "SVD Components Importance"
        )

        svd_fig = plot_singular_values(original_matrix[:,:,0]
        )

        st.pyplot(
            svd_fig
        )
