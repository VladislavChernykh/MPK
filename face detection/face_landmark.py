import sys
import os
import dlib
import glob
from skimage import io

class Image:
    def __init__(self, file_name, img):
        self.file_name = file_name
        self.dots = []
        self.img = img

    def process(self, predictor_path):
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predictor_path)
        win = dlib.image_window()
        
        print(self.file_name)
        
        win.clear_overlay()
        win.set_image(self.img)

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        dets = detector(self.img, 1)

        print("Number of faces detected: {}".format(len(dets)))
        for k, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                k, d.left(), d.top(), d.right(), d.bottom()))
            # Get the landmarks/parts for the face in box d.
            shape = predictor(self.img, d)
            for i in shape.parts():
                self.dots.append(i)
            win.add_overlay(shape)

        win.add_overlay(dets)
        dlib.hit_enter_to_continue()

    def save_dots_in_file(self):   
        with open("photo_dots.txt", "w") as file:
            for item in dots:
                print(str(item.x) + ' ' + str(item.y), file = file)

def face_dots_detection(predictor_path, faces_folder_path):
    images = []

    for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
        print("Processing file: {}".format(f))
 
        image = Image(f, io.imread(f))
        images.append(image)
        image.process(predictor_path)


def main():  
    
    if len(sys.argv) != 3:
        print(
            "Give the path to the trained shape predictor model as the first "
            "argument and then the directory containing the facial images.\n"
            "For example, if you are in the python_examples folder then "
            "execute this program by running:\n"
            "    ./face_landmark_detection.py shape_predictor_68_face_landmarks.dat ../examples/faces\n"
            "You can download a trained facial shape predictor from:\n"
            "    http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
        exit()

    predictor_path = sys.argv[1]
    faces_folder_path = sys.argv[2]

    face_dots_detection(predictor_path, faces_folder_path)

if __name__ == '__main__':
    main()