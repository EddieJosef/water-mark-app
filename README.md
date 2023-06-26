# Watermark App

This repository contains a watermark app designed using the Tkinter library in Python. The app allows users to upload an image file and add a custom watermark text to it. The watermarked image can then be saved to the desired location.

## Project Overview

The Watermark App provides a user-friendly interface for adding watermarks to images. With this app, you can upload your photo, enter the desired watermark text, and generate a watermarked image. The app utilizes the Tkinter library for GUI components and the PIL (Python Imaging Library) for image manipulation.

## Features

The Watermark App offers the following features:

1. **Image Selection**: Users can select an image file from their local system using the "Open File" button. Supported image formats include PNG and all other file types.

2. **Image Display**: The selected image is displayed in the app's window, providing a preview of the original image before applying the watermark.

3. **Watermark Addition**: Users can enter their desired watermark text in the text entry field. This text will be added as a watermark to the image.

4. **Watermark Placement**: The watermark is positioned at the center of the image. The app calculates the appropriate font size based on the image width and adds the text in red color for visibility.

5. **Watermarked Image Generation**: After adding the watermark, the user can click the "Add Watermark" button to generate the watermarked image. The watermarked image is saved to the user's specified location.

6. **Multiple Usage**: Users can repeatedly open new images, add different watermarks, and generate watermarked images without closing and reopening the app.

## Dependencies

The following dependencies are required to run the Watermark App:

- Python 3.x
- Tkinter library
- PIL (Python Imaging Library)

The dependencies can be installed using the following command:

```
pip install pillow
```

## Usage

1. Clone the repository to your local machine or download the source code.

2. Install the required dependencies if not already installed (see Dependencies section).

3. Run the `watermark_app.py` file using Python.

4. The app window will appear, showing the "Open File" button.

5. Click the "Open File" button to select an image file from your local system.

6. The selected image will be displayed in the app window.

7. Enter your desired watermark text in the text entry field.

8. Click the "Add Watermark" button to generate the watermarked image.

9. The watermarked image will be saved to your specified location.

10. Repeat the process to add watermarks to other images.

## Future Enhancements

Here are some potential future enhancements for the Watermark App:

- **Customizable Watermark Style**: Allow users to customize the font, size, color, and position of the watermark text to suit their preferences.

- **Batch Processing**: Enable the app to process multiple images at once, applying the same watermark to all of them, saving time and effort for users.

- **Undo/Redo Functionality**: Implement the ability to undo or redo watermark additions, allowing users to make changes or revert to the original image easily.

- **Resizable Window**: Make the app window resizable to provide a more flexible and user-friendly interface, accommodating images of various sizes.
