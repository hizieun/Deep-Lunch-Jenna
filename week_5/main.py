import mediapipe as mp
import os
import cv2
import math
import numpy as np
import argparse


def resize_and_save(args, image, name):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (args.DESIRED_WIDTH, math.floor(h/(w/args.DESIRED_WIDTH))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/args.DESIRED_HEIGHT)), args.DESIRED_HEIGHT))

  # Save Results
  save_path = f"./img/result_{name}"
  cv2.imwrite(save_path, img)
  return
    

def get_faceMesh(args):
    # Read images with OpenCV.
    image_list = os.listdir(args.IMG_DIR)
    
    mp_face_mesh = mp.solutions.face_mesh
    # help(mp_face_mesh.FaceMesh) # MP Option Check

    # Load drawing_utils and drawing_styles
    mp_drawing = mp.solutions.drawing_utils 
    mp_drawing_styles = mp.solutions.drawing_styles

    # Run MediaPipe Face Mesh.
    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        refine_landmarks=True,
        max_num_faces=2,
        min_detection_confidence=0.5) as face_mesh:
            
      for name, img in enumerate(image_list):
        image = cv2.imread(os.path.join(args.IMG_DIR, img))
        # Convert the BGR image to RGB and process it with MediaPipe Face Mesh.
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
        # Draw face landmarks of each face.
        # print(f"Face landmarks of {name}:")
        if not results.multi_face_landmarks:
          continue
        annotated_image = image.copy()
        for face_landmarks in results.multi_face_landmarks:
          mp_drawing.draw_landmarks(
              image=annotated_image,
              landmark_list=face_landmarks,
              connections=mp_face_mesh.FACEMESH_TESSELATION,
              landmark_drawing_spec=None,
              connection_drawing_spec=mp_drawing_styles
              .get_default_face_mesh_tesselation_style())
          mp_drawing.draw_landmarks(
              image=annotated_image,
              landmark_list=face_landmarks,
              connections=mp_face_mesh.FACEMESH_CONTOURS,
              landmark_drawing_spec=None,
              connection_drawing_spec=mp_drawing_styles
              .get_default_face_mesh_contours_style())
          mp_drawing.draw_landmarks(
              image=annotated_image,
              landmark_list=face_landmarks,
              connections=mp_face_mesh.FACEMESH_IRISES,
              landmark_drawing_spec=None,
              connection_drawing_spec=mp_drawing_styles
              .get_default_face_mesh_iris_connections_style())
        resize_and_save(args, annotated_image, img)
    return
          

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='이미지 전처리 관련 변수 설정')
    parser.add_argument('--IMG_DIR', type=str, default="./img", help='image height')
    parser.add_argument('--DESIRED_HEIGHT', type=int, default=480, help='image height')
    parser.add_argument('--DESIRED_WIDTH', type=int, default=480, help='image width')
    args = parser.parse_args()

    # Preview the images.
    # Read images with OpenCV.
    # images = os.listdir(args.IMG_DIR)
    
    # for _, img in images:
    #   img_path = os.path.join(args.IMG_DIR, img) 
    #   resize_and_save(args, img_path)

    # Get Face Mesh from images.
    get_faceMesh(args)