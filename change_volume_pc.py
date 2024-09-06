import cv2
import mediapipe as mp

from utilities.utility import calculate_distance_between_points, set_system_volume, get_system_volume

mediapipeHands = mp.solutions.hands
hands = mediapipeHands.Hands()


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    h,w,c = frame.shape
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    result = hands.process(frame_rgb)
    
    if result.multi_hand_landmarks:
        
        for handlandmarks in result.multi_hand_landmarks:
            
            point_4 = handlandmarks.landmark[4]
            point_8 = handlandmarks.landmark[8]
            
            
            distance = round(calculate_distance_between_points(point_4, point_8), 1) # between 0.0 and 0.5
            set_system_volume(distance * 2)
            
            thumb_tip_coords = (int(point_4.x * w), int(point_4.y * h))
            index_tip_coords = (int(point_8.x * w), int(point_8.y * h))
            
            cv2.line(frame, thumb_tip_coords, index_tip_coords, (0, 0, 255), 3)
    
    
    
    cv2.imshow("Camera", frame)
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

