"""A group of utility functions for validating data and graphing them, as well as automating pulling
	from created dictionaries."""
# This library contains utility functions for visualizing the results of clustering algorithms
# from scikit learn. It relies on matplotlib, seaborn, and pylab. This exists because the natural
# input to most machine learning algorithms is an array of vectors. The resulting predictions along
# with their tags can be represented succintly as a tuple containing a vector and the label given
# to it. However, most graphing functions require a list of the coordinates in each dimensions;
# this necessiates splitting the list of tuples vertically for passing to the graphing function.

import pandas as pd
import numpy as np
import matplotlib as plt
import pylab as pyl
import seaborn as sns




def tuple_check(NateTuple):
    """Takes in a tuple, returns true only if every member of the tuple is a number."""
    filtered_tuple = np.isnan(NateTuple)
    if all(item==False for item in filtered_tuple):
        return True
    else: 
        return False


def pull_from_tag(tag_to_pull,whichpair,list_to_pull_from):
	"""Returns all items with tag_to_pull from iterable list_to_pull_from using whichpair to 
		determine which element to take out"""
	if whichpair == 1:
		return [x for x,y in list_to_pull_from if y == tag_to_pull] #decides whether to return first element or second
	else:
		return [y for x,y in list_to_pull_from if x == tag_to_pull]


def tuple_list_creator(list_to_generate_from):
    """Takes in a list of lists of tuples, and then slices them vertically to return a lists of lists of x-
    	dimensions the same as that of the tuple represented as a vector."""
    list_to_return = []
    for x in list_to_generate_from:
        list_to_return.append(zip(*x)) #this is the part doing the slicing
    return list_to_return

colormap = ['#66FF66','#008000','#000066','#8080FF','#660000','#FF4D4D','#990099','#FF33FF','#808000','#FFFF4D','#B26B00','#FFAD33','#476B6B','#A3C2C2','#6B2400','#D6AD99','#FFFFFF','#000000']  
#colormap is a list that provides HTML color codes for makePlot to use. It can represent up to
#eighteen different data sets.

def makePlot_3d(coordinate_list):
    """Creates a 3d plot of objects with multiple tags from coordinate list.
    	coordinate_list is a list of tuples of lists, where each tuple element is a set of
    	coordinates for that particular list. Ex: [([x,x,x,x],[y,y,y,y],[z,z,z,z]),...]"""
    plotObjectBox = pyl.figure() #creates a figure
    plotObjectBox_ax = plotObjectBox.add_subplot(111, projection='3d') #adds a subplot
    togetherlist = zip(coordinate_list,colormap[:len(coordinate_list)-1]) #creates a tuple list
    for x,y in togetherlist: #associates each set of coordinates with an html color tag
        plotObjectBox_ax.scatter(x[0], x[1],x[2],c=y)
