
from rembg import remove
from PIL import Image
import os


class BackgroundRemover:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

        # Ensure output folder exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

    def remove_background(self):
        try:
            print("Loading image...")
            image = Image.open(self.input_path)

            print("Removing background...")
            output = remove(image)

            print("Saving output image...")
            output.save(self.output_path)

            print("Background removed successfully!")

        except FileNotFoundError:
            print("Input image not found")

        except Exception as e:
            print(f"Error: {e}")


def main():
    input_image = "input_images/sample.jpg"
    output_image = "output_images/sample_no_bg.png"

    remover = BackgroundRemover(input_image, output_image)
    remover.remove_background()


if __name__ == "__main__":
    main()
