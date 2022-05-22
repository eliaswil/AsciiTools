import os
import cv2
import numpy as np

density :str = 'Ñ@#W$9876543210?!abc;:+=-,._ '
reverse_density :str = density[::-1]
shades :int = len(density)


os.system('') # activate coloring


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)

def fill(height :int, width :int, char :str) -> str:
    s :str = '\n'
    for h in range(height-3):
        for w in range(width):
            s += char
    
    print(s , end='')
    
    return s


def generate_ascii(height :int, width :int, image :np.ndarray, color :bool = False) -> str:
    small = cv2.resize(image, (width, height))
    gray = cv2.cvtColor(small,cv2.COLOR_BGR2GRAY)
    cv2.imshow('small',small)
    
    s :str = '\n'
    for h in range(height):
        for w in range(width):
            index = int(gray[h][w]/255*shades)
            index = max(index, 0)
            index = min(index, len(density)-1)
            
            char :str = reverse_density[index]
            
            if color:
                b,g,r = small[h][w]
                char = colored(r,g,b,char)
            
            s += char
    print(s, end='')
    return s

def main():
    
    width, height = os.get_terminal_size()
    print(width, height)
    
    fill(height, width, "*")
    
    camera = cv2.VideoCapture(0)
    print('here')
    
    color :bool = False
    
    while True:
        
        width, height = os.get_terminal_size()
        _, image = camera.read()
        cv2.imshow('image',image)
        
        generate_ascii(height, width, image, color)
        
        
        # cv2.waitKey(0)
        
        key :int = cv2.waitKey(1)& 0xFF
        if key == ord('q'): # q
            break
        if key == ord('c'): # q
            color = True
        if key == ord('g'): # q
            color = False

            
        
    camera.release()
    cv2.destroyAllWindows()
    
    
    
    
    
    
    pass



if __name__ == '__main__':
    main()