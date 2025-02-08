
from omnigenai_toolkit.multi_modal import process_text_and_image

def multi_modal_response(text, image_path):
    response = process_text_and_image(text, image_path)
    return response

if __name__ == "__main__":
    text = "Analyze this image:"
    image_path = "example.jpg"
    response = multi_modal_response(text, image_path)
    print("Multi-Modal Response:", response)
