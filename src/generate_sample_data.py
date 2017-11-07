import cPickle
import draw_digits
#import show_data

def generate_all_data(prefix, bg_difficulty, alpha_group = 0):
    sample_size = 3000 #medium = approximate geometric mean between 1000 and 10000
    if "small" in prefix:
        sample_size = 1000
    if "large" in prefix:
        sample_size = 10000

    training_data_set = [([],[]),([],[]),([],[]),([],[]),([],[])]           #this is evidence of lazyness and the wrong approach
    validation_data_set = [([],[]),([],[]),([],[]),([],[]),([],[])]
    test_data_set = [([],[]),([],[]),([],[]),([],[]),([],[])]

    # Transform a bunch of these guys
    # [([a_0],[b_0]),([a_1],[b_1]),([a_2],[b_2]),([a_3],[b_3]),([a_4],[b_4])]  from draw_rand_text()
    # into
    # [([a0_0,a1_0,...an_0],[b0_0,b1_0,...bn_0]),([a_1...],[b_1...]),([a_2...],[b_2...]),([a_3...],[b_3...]),([a_4...],[b_4...])]
    # so it looks like a array of 5 mnist data sets: ([pics],[vals]) x 5
    # Fix to use list comprehension
    for x in xrange(0,sample_size*5):   #training data should be about 5x larger than the evaluation data
        temp = draw_digits.draw_rand_text(bg_difficulty, alpha_group)
        for i in xrange(0,5):
            training_data_set[i][0].append(temp[i][0])
            training_data_set[i][1].append(temp[i][1])
            #print training_data_set[i][1]
    for x in xrange(0,sample_size):
        temp = draw_digits.draw_rand_text(bg_difficulty, alpha_group)
        for i in xrange(0,5):
            validation_data_set[i][0].append(temp[i][0])
            validation_data_set[i][1].append(temp[i][1])
    for x in xrange(0,sample_size):
        temp = draw_digits.draw_rand_text(bg_difficulty, alpha_group)
        for i in xrange(0,5):
            test_data_set[i][0].append(temp[i][0])
            test_data_set[i][1].append(temp[i][1])
    
    names = []

    for i in range(0,5):
        names.append("../data/hardData/"+prefix+"_bg"+str(bg_difficulty)+"_a"+str(alpha_group)+"_e"+str(i)+".pkl")
        cPickle.dump( (training_data_set[i], validation_data_set[i], test_data_set[i]) , open( names[i], "wb" ) )

    return names
