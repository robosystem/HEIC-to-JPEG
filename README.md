# HEIC to JPEG Converter

## Introduction

This Python script, `heic_to_jpeg.py`, is designed to convert HEIC (High-Efficiency Image Format) files to JPEG format. Before using the script, ensure that you have installed the required packages using pip.

## Requirements

1. **Install Pillow, pillow-heif and tqdm package:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Download the Script:**

    Download the `heic_to_jpeg.py` script to your local machine.

2. **Run the Script:**

    Open a terminal and run the script pointing to the directory where the HEICs are located.

    ```bash
    python heic_to_jpeg.py --help

    usage: heic2jpg.py [-h] [-r] path

    Convert HEIC in JPG.

    positional arguments:
      path          path of file HEIC or folder containing HEIC files.

    options:
      -h, --help    show this help message and exit
      -r, --remove  remove original HEIC file after successful operation.
    ```

