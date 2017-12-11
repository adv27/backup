#-- include('examples/showgrabfullscreen.py') --#
import pyscreenshot as ImageGrab

def main():
	im = ImageGrab.grab(bbox=(10,10,510,510))
	im.show()

if __name__ == '__main__':
	main()


