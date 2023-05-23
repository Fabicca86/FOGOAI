from my_detect import parse_opt, main, yolo_detector
import cv2
import time

cap = cv2.VideoCapture(0)
a = yolo_detector()
while True:
    rec, img = cap.read()
    print(img.shape)
    # img = cv2.imread('fire_000082.jpg')
    # img = cv2.resize(img, (640, 480))
    print(img.shape)
    results,im = a.run(img)

    if results:
        for i, pts in enumerate(results):
            cv2.rectangle(img, pts[0], pts[1], (0, 0, 255), 2)
    cv2.imshow("video", img)

    if cv2.waitKey(1) == ord('q'):
        break

def start_fire_detect(image):
    opt = parse_opt()
    # opt.source = 'fire_000082.jpg'
    # opt.temporal = 'persistence'
    # opt.save_txt = True
    # opt.save_conf = True

    # annotated_image, result_data = main(opt, image)
    # print(result_data) # 类别，xywh，置信度
    # while True:
    #     cv2.imshow("Window", annotated_image)
    #     key = cv2.waitKey(1)
    #     if key & 0xFF == ord('q'):
    #         break
    cap = cv2.VideoCapture(0)

    # 循环读取视频帧
    while True:
        # 从splitcam读取一帧
        ret, frame = cap.read()
        # 如果读取成功，显示在窗口上
        if ret:
            print(type(frame))
            t1 = time.time()
            annotated_image, result_data = main(opt, frame)
            t2 = time.time()
            print(t2-t1)
            cv2.imshow("Window", annotated_image)
            print(result_data)
        # 如果按下q键，退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return annotated_image, result_data


if __name__ == '__main__':
    image = cv2.imread('fire_000082.jpg')
    print(type(image))
    start_fire_detect(image)