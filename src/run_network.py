'''
This project is a proof of concept that an OCR system can reliably read printed documents even when 
obfuscated.  The design of the basic neural network is taken from Michael A. Nielson's book "Neural 
Networks and Deep Learning" 2015 and the code is lightly adapted from the associated repo: 
https://github.com/mnielsen/neural-networks-and-deep-learning.git

It provides validation that the design of experiment is well founded and maps to reality well.  
Furthermore it provides data about the effectiveness of image preprocessing to achieve higher 
accuracy and faster training than raw images.


'''



import show_data
import numpy as np

import time

'''import draw_digits
generated_data = [[],[],[],[],[]] 
for x in xrange(0,0):
  sets = draw_digits.draw_rand_text(5,3)
  for en_num in range(0,len(sets)):
    generated_data[en_num].append(sets[en_num])
    show_data.show_image(show_data.shape_to_2d_image(generated_data[en_num],x), "_e" + str(en_num) + ": " + str(show_data.get_sample_value(generated_data[en_num],x)))
'''
import generate_sample_data
sample_set_names = generate_sample_data.generate_all_data("small", 5, 3)
#sample_set_names = ["../data/hardData/small_bg5_a3_e0.pkl", "../data/hardData/small_bg5_a3_e1.pkl", "../data/hardData/small_bg5_a3_e2.pkl",  "../data/hardData/small_bg5_a3_e3.pkl", "../data/hardData/small_bg5_a3_e4.pkl"]

import custom_loader
import hard_alphabet

for batch in range(0,len(sample_set_names)):
  training_data, validation_data, test_data = custom_loader.load_data_wrapper(custom_loader.load_text_data(sample_set_names[batch]))
  
  show_data.show_image(show_data.shape_to_2d_image(training_data,0), hard_alphabet.num_to_chars(show_data.get_sample_value(training_data,0),3))

  print 'running network for ' + sample_set_names[batch]

  accuracy_record = open('accuracy.txt', 'a')
  accuracy_record.write("\n\n" + sample_set_names[batch] + "\n\n")
  accuracy_record.close()

  import network2
  net = network2.Network([784, 30, 10], cost=network2.CrossEntropyCost)
  net.large_weight_initializer()

  #net.SGD(training_data, 30, 10, 0.3, evaluation_data=test_data, monitor_evaluation_accuracy=True)
  net.SGD(training_data, 30, 10, 0.1,
  lmbda = 5.0,
  evaluation_data=validation_data,
  monitor_evaluation_accuracy=True,
  monitor_training_accuracy=True)
