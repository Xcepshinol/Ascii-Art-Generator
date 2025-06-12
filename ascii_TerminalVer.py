import cv2, os, platform

def clear_term():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def webcam():
    lett = "@#$%&*+-.  "

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    
    while True:
        s=''

        ret, frame = cap.read()
        if not ret:
            break

        w = 100

        l1, w1 = frame.shape[:2]
        l = int((l1 / w1) * w * 0.5)

        frame = cv2.resize(frame, (w,l), interpolation=cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        clear_term()
        for i in range(l):
            s += '\n'
            for j in range(w):
                x = (255-(frame[i, j]))//25 #find the character corresponding brightness
                s+=lett[x]        
        print(s)

        cv2.imshow('test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

webcam()
