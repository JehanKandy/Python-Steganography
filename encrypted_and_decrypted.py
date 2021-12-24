#import modules

from PIL import Image
import stepic

#code for encrypted 

#------

#open any image
im=Image.open('G:/learning/programming/python/python.jpeg')
#now type anything you want to encryt
im1=stepic.encode(im,b'Jehan Kandy')
#now save the image

#******* important save image in .png extention*****************
#otherwise it not workinh
 
im1.save('G:/learning/programming/python/python.png')
im1=Image.open('G:/learning/programming/python/python.png')
im1.show()


#code of decryted

#------

#open any image
im2=Image.open('G:/learning/programming/python/python.png')
#now decode the image
Image=stepic.decode(im2)
print(Image)

#-------------

