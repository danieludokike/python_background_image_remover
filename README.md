# Image Background Remover (Python)

A simple **Image Background Remover** built with **Python** using an **Object-Oriented Programming (OOP)** approach.  
This project removes the background from images automatically and saves the output as a transparent PNG file.

It is suitable for **beginners**, **live classes**, and **real-world use cases**.


## Features
- Remove image background automatically
- Uses a pre-trained AI model (no training required)
- Object-Oriented design
- Clean and easy-to-read code
- Saves output with transparent background
- Error handling for safe execution


## Technologies Used
- **Python 3.8+**
- **rembg** (AI background removal)
- **Pillow (PIL)** for image handling
- **OS module** for file management


## Project Structure
```
bg_remover/
│
├── remover.py
├── input_images/
│ └── sample.jpg
└── output_images/
└── sample_no_bg.png
```



## Installation

### 1. Clone the Repository

```git clone https://github.com/danieludokike/python_background_image_remover.git```
```cd python_background_image_remover```

### 2. Install Required Libraries
```pip install -r requirements.txt```
Ensure Python version is 3.8 or above

How to Run
Place an image inside the input_images folder

Update the image name in remover.py if necessary

Run the application:

```python remover.py```
The background-removed image will be saved inside output_images

### How It Works
The application loads the image using Pillow

The rembg library removes the background using a trained AI model

The output image is saved as a PNG with transparency