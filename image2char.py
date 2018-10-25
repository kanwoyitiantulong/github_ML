#usr/bin/python
#-*-conding:utf-8-*-

from PIL import Image
import numpy as np

if __name__=='__main__':
    im=Image.open("lena.png")
    im_wigth,im_height=im.size
    height=100
    wigth=im_wigth*height//im_height
    im=im.resize((wigth,height),Image.ANTIALIAS)
    pxesl=np.array(im.convert('L'))
    chars="MNHQ$OC?7>!:?-;. "
    # chars=":{}_)<>?!@#$%%^& ;'.,/"
    N=len(chars)
    step=256//N
    print(N)
    res=''
    for i in range(height):
        for j in range(wigth):
            res += chars[pxesl[i][j]//step]
        res += '\n'
    with open('image.txt', mode='w') as f:
        f.write(res)
    print('OK')
