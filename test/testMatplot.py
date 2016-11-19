import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import os
if __name__ =='__main__':
    image_file = cbook.get_sample_data(os.getcwd()+'\.png')
    image = plt.imread(image_file)
    plt.imshow(image)
    plt.axis('off')
    plt.show()
