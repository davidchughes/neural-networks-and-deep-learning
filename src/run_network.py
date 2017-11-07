'''
This project is a proof of concept that an OCR system can reliably read printed documents even when 
obfuscated.  The design of the basic neural network is taken from Michael A. Nielson's book "Neural 
Networks and Deep Learning" 2015 and the code is lightly adapted from the associated repo: 
https://github.com/mnielsen/neural-networks-and-deep-learning.git

It provides validation that the design of experiment is well founded and maps to reality well.  
Furthermore it provides data about the effectiveness of image preprocessing to achieve higher 
accuracy and faster training than raw images.


'''
import os
import numpy as np
import time


alpha_group = 3
bg = 5
prefix = "small"
import hard_alphabet
import show_data

'''
import draw_digits
generated_data = [[],[],[],[],[]]

for x in xrange(0,10):
  sets = draw_digits.draw_rand_text(bg,alpha_group)
  for en_num in range(0,len(sets)):
    generated_data[en_num].append(sets[en_num])
    show_data.show_image(show_data.shape_to_2d_image(generated_data[en_num],x), "_e" + str(en_num) + ": " + hard_alphabet.num_to_chars(show_data.get_sample_value(generated_data[en_num],x)),alpha_group)
'''

if not os.path.exists("../data/hardData"):
    os.makedirs("../data/hardData")

sample_set_names = ["../data/hardData/"+prefix+"_bg"+str(bg)+"_a"+str(alpha_group)+"_e"+str(e)+".pkl" for e in range(0,5)]
missing = False
#check to see if the data set files already exist
for file in sample_set_names:
  if not os.path.exists(file):
    missing = file
    print "Could not find '" + file + "'. Generating whole new set now."
    break
# if the .pkl files aren't all there, then generate more
if missing:
  import generate_sample_data
  generated_set_names = generate_sample_data.generate_all_data(prefix, bg, alpha_group)
  # in case someone in the future only wants to run a subset of the enhancements and asks for one that didn't get generated, throw a soft little message on the screen
  if not set(generated_set_names).issuperset(sample_set_names):       #check to make sure all requested files names have been generated
    print "Error! Set names don't match. Expected:" + str(sample_set_names) + " Generated:" + str(generated_set_names)    # an attempt at being civilized
    # continue on with what was generated since I don't want to come back after hours of running and see a fat finger mistake to have killed the program.
    sample_set_names = generated_set_names

import custom_loader


for batch in sample_set_names:
  print "Loading " + batch 
  training_data, validation_data, test_data = custom_loader.load_data_wrapper(custom_loader.load_text_data(batch))
  
  #show_data.show_image(show_data.shape_to_2d_image(training_data,0), hard_alphabet.num_to_chars(show_data.get_sample_value(training_data,0),3))

  print 'running network for ' + batch

  accuracy_record = open('accuracy.txt', 'a')
  accuracy_record.write("\n\n" + batch + "\n\n")
  accuracy_record.close()

  import network2
  net = network2.Network([784, 30, 10], cost=network2.CrossEntropyCost)
  net.large_weight_initializer()

  #net.SGD(training_data, 30, 10, 0.3, evaluation_data=test_data, monitor_evaluation_accuracy=True)
  net.SGD(training_data, 30, 10, 0.1,
  lmbda = 5.0,
  evaluation_data=test_data,
  monitor_evaluation_accuracy=True,
  monitor_training_accuracy=True)
