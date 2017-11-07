from matplotlib import pyplot
import matplotlib as mpl
import numpy as np

def show_image(image,value = "?"):
  #Render a given numpy.float32 2D array of pixel data.
  fig = pyplot.figure()
  pyplot.title(value, y=1.05)
  ax = fig.add_subplot(1,1,1)
  imgplot = ax.imshow(image, cmap='gray_r')
  imgplot.set_interpolation('nearest')
  ax.xaxis.set_ticks_position('top')
  ax.yaxis.set_ticks_position('left')
  pyplot.show()


def shape_to_2d_image(samples,index):
  return samples[index][0].reshape(28,28)

def get_sample_value(samples,index):
  if not isinstance(samples[index][1], int): # then the value has been vectorized as the final output of the nodes [0,0,0,0,0,0,0,0,0,1] = node 9
    x = 0
    for test in samples[index][1]:
      if test == 1:
        return x
      x += 1

  return samples[index][1]