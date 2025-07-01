from paddleocr import PaddleOCR
import cv2

def _join_text(text_chunks: list):
    return ' '.join(text_chunks)

def run_ocr(image_path):
    # Initialize OCR model
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # or 'ch' / 'en' / 'en'+'ch'
    
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image at {image_path}")
        return
    
    # Run OCR
    result = ocr.predict(img)
    print(result)
    
    print("**************************")
    
    print(_join_text(result[0].get("rec_texts", "Text was found!")))


if __name__ == "__main__":
    run_ocr(r"/home/eugene/Desktop/MyStudies/Projects/BackEnd/ocr_app/text.png")

#/home/eugene/Downloads/text-image-title.png 
