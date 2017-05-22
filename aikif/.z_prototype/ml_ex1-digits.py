#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ml_ex1-digits.py
# based on tutorial at https://www.datacamp.com/community/tutorials/machine-learning-python#gs.bisadvw 

import os
import sys

sys.path.append('..')

import cls_file_mapping as mod_filemap
import core_data as c


# Setup the training data
#################################################################

try:
    from sklearn import datasets
    
except Exception as ex:
    print('cant import sklean - are you running this in Anaconda prompt?')


import matplotlib.pyplot as plt 
    
    
def main():
    digits = datasets.load_digits()
    #print_digit_data(digits)    # tok
    #plot_training_data(digits)  # tok
    #plot_target_data(digits)    # tok
    show_PCA_training(digits)
    


def print_digit_data(digits):
    # Get the keys of the `digits` data
    print(digits.keys)

    # Print out the data
    print(digits.data)

    # Print out the target values
    print(digits.target)

    # Print out the description of the `digits` data
    print(digits.DESCR)


def plot_training_data(digits):
    # Visualise the Data 
    #############################################################

    import matplotlib.pyplot as plt

    # Figure size (width, height) in inches
    fig = plt.figure(figsize=(6, 6))

    # Adjust the subplots 
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

    # For each of the 64 images
    for i in range(64):
        # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
        ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
        # Display an image at the i-th position
        ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
        # label the image with the target value
        ax.text(0, 7, str(digits.target[i]))

    # Show the plot
    plt.show()


def plot_target_data(digits):
    
    
    # Join the images and target labels in a list
    images_and_labels = list(zip(digits.images, digits.target))

    # for every element in the list
    for index, (image, label) in enumerate(images_and_labels[:8]):
        # initialize a subplot of 2X4 at the i+1-th position
        plt.subplot(2, 4, index + 1)
        # Don't plot any axes
        plt.axis('off')
        # Display images in all subplots 
        plt.imshow(image, cmap=plt.cm.gray_r,interpolation='nearest')
        # Add a title to each subplot
        plt.title('Training: ' + str(label))

    # Show the plot
    plt.show()


def show_PCA_training(digits):
    # Create a Randomized PCA model that takes two components
    from sklearn import decomposition
    
    randomized_pca = decomposition.RandomizedPCA(n_components=2)


    # Fit and transform the data to the model
    reduced_data_rpca = randomized_pca.fit_transform(digits.data)

    # Create a regular PCA model 
    pca = decomposition.PCA(n_components=2)

    # Fit and transform the data to the model
    reduced_data_pca = pca.fit_transform(digits.data)

    # Inspect the shape
    reduced_data_pca.shape

    # Print out the data
    print(reduced_data_rpca)
    print(reduced_data_pca)    
    
    colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
    for i in range(len(colors)):
        x = reduced_data_rpca[:, 0][digits.target == i]
        y = reduced_data_rpca[:, 1][digits.target == i]
        plt.scatter(x, y, c=colors[i])
    plt.legend(digits.target_names, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.title("PCA Scatter Plot")
    plt.show()
    
    
    
       
if __name__ == '__main__':
    main()
