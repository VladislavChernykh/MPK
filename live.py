import cv2
import time
import os

IMAGE_FOLDER = 'images'
VIDEO_FOLDER = 'videos'

def stream(cap, out, start_time):
	while(True):
		faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		# Capture frame-by-frame
		ret, frame = cap.read()

		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.2,
			minNeighbors=5,
			minSize=(30, 30)
			#flags = cv2.CV_HAAR_SCALE_IMAGE
		)
		#Current time in sec
		current_time = int(time.time())
		#If some faces found with 5 sec interval taking snapshot!
		if (len(faces) != 0) & (((start_time - current_time) % 5) == 0):
			#Creating file name
			image_filename = IMAGE_FOLDER + "\image_" +  time.strftime("%Y_%m_%d_%H-%M-%S", time.gmtime(current_time)) + ".png"
			#Saving pic in folder
			cv2.imwrite(str(image_filename), frame)
			print('Image saved', str(image_filename))
		out.write(frame)
		#print("Found {0} faces!	".format(len(faces)))

		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		# Display the resulting frame
		cv2.imshow('To exit press Q.', frame)
		keypress = cv2.waitKey(1)
		if keypress & 0xFF == ord('q'):
			break

def main():
	if (os.path.exists(IMAGE_FOLDER)) == False:
		os.mkdir(IMAGE_FOLDER)
	if (os.path.exists(VIDEO_FOLDER)) == False:
		os.mkdir(VIDEO_FOLDER)
	print('Программа для захвата лица.')
	print('1. Начать запись')
	print('2. Выход')
	while(True):
		cmd = '0'
		cmd = input('Введите команду: ')
		if cmd == '1':
			try:
				start_time = int(time.time())
				#Дописать нахождение видео потоков и их выбор!
				#Агрумент VideoCapture номер камеры, если их несколько, то могут быть разные аргументы!
				#Дефолт 0, но может быть и 1 и 2.
				cap = cv2.VideoCapture(1)

				fourcc = cv2.VideoWriter_fourcc(*'XVID')
				video_filename = 'video_' + time.strftime("%Y_%m_%d_%H-%M-%S", time.gmtime(time.time())) + '.avi'
				print(video_filename)
				out = cv2.VideoWriter(video_filename, fourcc, 5.0, (640,480))

				#Function with face detection
				stream(cap, out, start_time)
			#Error with library OpenCV
			except cv2.error as OpenCV_Error:
				print('')
			#Else errors!
			except:
				print('Ошибка в программе!')
			#Finally closing cv2
			finally:
				out.release()
				cap.release()
				cv2.destroyAllWindows()
		elif cmd == '2':
			print('Работа закончена.')
			break
		else:
			print('Неверная команда!')

if __name__ == '__main__':
	main()