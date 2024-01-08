import os

def find_images_without_annotations(image_folder, annotation_folder):
    image_files = set([file.split('.')[0] for file in os.listdir(image_folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))])
    annotation_files = set([file.split('.')[0] for file in os.listdir(annotation_folder) if file.lower().endswith('.txt')])

    images_without_annotations = image_files - annotation_files
    return images_without_annotations

def remove_images_without_annotations(image_folder, images_without_annotations):
    for image in images_without_annotations:
        image_path = os.path.join(image_folder, f'{image}.jpg')  # Assuming image files have jpg extension
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Removed: {image}.jpg")

if __name__ == "__main__":
    images_folder = r"C:\Users\ahmad\Desktop\accessories\AI-Projects\Object-Detection-Project2\temp"
    annotations_folder = r"C:\Users\ahmad\Desktop\accessories\AI-Projects\Object-Detection-Project2\labels"

    missing_annotations = find_images_without_annotations(images_folder, annotations_folder)

    if missing_annotations:
        remove_images_without_annotations(images_folder, missing_annotations)
        print("Images without annotations removed.")
    else:
        print("All images have corresponding annotations.")
