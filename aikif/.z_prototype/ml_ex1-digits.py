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
from sklearn.cross_validation import train_test_split
from sklearn import svm        
from sklearn import metrics  
from sklearn.manifold import Isomap 

   
def main():
    digits = datasets.load_digits()
    #print_digit_data(digits)    # tok
    #plot_training_data(digits)  # tok
    #plot_target_data(digits)    # tok
    #show_PCA_training(digits)   # tok
    
    data = preprocess_data(digits)   # tok
    #print(data)   # tok
    
    X_train, X_test, y_train, y_test = split_data_into_training_and_test(data, digits)   # tok
    
    
    clf = cluser_digits(X_train)   # tok
    # show_cluster_digits(clf)  # TOK
    
    y_pred = predict_labels(clf, X_test, y_test, X_train, y_train)   # tok
    show_prediction_confusion_matrix(y_test, y_pred)   # tok
   
    homogeneity_score(clf, X_test, y_test, X_train, y_train, y_pred)   # tok
   
    ##########################################
    # try a different model
    svc_model, X_train, X_test, y_train, y_test, images_train, images_test = model_SVC(digits)   # tok
    
    # grid_search - use this to tune parameters
    grid_search(digits)   # tok
    apply_grid_search(clf, X_test, y_test, X_train, y_train)
    predicted = classify_rbf(svc_model, X_test, y_test, images_test)
    check_model_performance(y_test, predicted)
    
    show_model2_results(svc_model, X_train, y_train)
    
    
def show_model2_results(svc_model, X_train, y_train):
    

    # Create an isomap and fit the `digits` data to it
    X_iso = Isomap(n_neighbors=10).fit_transform(X_train)

    # Compute cluster centers and predict cluster index for each sample
    predicted = svc_model.predict(X_train)

    # Create a plot with subplots in a grid of 1X2
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))

    # Adjust the layout
    fig.subplots_adjust(top=0.85)

    # Add scatterplots to the subplots 
    ax[0].scatter(X_iso[:, 0], X_iso[:, 1], c=predicted)
    ax[0].set_title('Predicted labels')
    ax[1].scatter(X_iso[:, 0], X_iso[:, 1], c=y_train)
    ax[1].set_title('Actual Labels')


    # Add title
    fig.suptitle('Predicted versus actual labels', fontsize=14, fontweight='bold')

    # Show the plot
    plt.show()    
    
def check_model_performance(y_test, predicted):
    """
                    precision    recall  f1-score   support

              0       1.00      1.00      1.00        43
              1       0.97      1.00      0.99        37
              2       0.97      1.00      0.99        38
              3       0.98      0.93      0.96        46
              4       1.00      0.98      0.99        55
              5       0.97      1.00      0.98        59
              6       1.00      1.00      1.00        45
              7       0.98      0.98      0.98        41
              8       1.00      0.97      0.99        38
              9       0.96      0.96      0.96        48

    avg / total       0.98      0.98      0.98       450
    """
    

    # Print the classification report of `y_test` and `predicted`
    print(metrics.classification_report(y_test, predicted))

    # Print the confusion matrix
    print(metrics.confusion_matrix(y_test, predicted))    


def classify_rbf(svc_model, X_test, y_test, images_test):
    # Predict the label of `X_test`
    print(svc_model.predict(X_test))

    # Print `y_test` to check the results
    print(y_test)
    # Import matplotlib
    import matplotlib.pyplot as plt

    # Assign the predicted values to `predicted`
    predicted = svc_model.predict(X_test)

    # Zip together the `images_test` and `predicted` values in `images_and_predictions`
    images_and_predictions = list(zip(images_test, predicted))

    # For the first 4 elements in `images_and_predictions`
    for index, (image, prediction) in enumerate(images_and_predictions[:4]):
        # Initialize subplots in a grid of 1 by 4 at positions i+1
        plt.subplot(1, 4, index + 1)
        # Don't show axes
        plt.axis('off')
        # Display images in all subplots in the grid
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        # Add a title to the plot
        plt.title('Predicted: ' + str(prediction))

    # Show the plot
    plt.show()    
    
    return predicted
    
    
    
    
def apply_grid_search(clf, X_test, y_test, X_train, y_train):
    # Apply the classifier to the test data, and view the accuracy score
    clf.score(X_test, y_test)  

    # Train and score a new classifier with the grid search parameters
    svm.SVC(C=10, kernel='rbf', gamma=0.001).fit(X_train, y_train).score(X_test, y_test)
    
    
def grid_search(digits):
    """
    Best score for training data: 0.9844097995545658
    Best 'C': 10
    Best kernel: rbf
    Best 'gamma': 0.001    
    """
    # Split the `digits` data into two equal sets
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.5, random_state=0)

    # Import GridSearchCV
    from sklearn.grid_search import GridSearchCV

    # Set the parameter candidates
    parameter_candidates = [
      {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
      {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
    ]

    # Create a classifier with the parameter candidates
    clf = GridSearchCV(estimator=svm.SVC(), param_grid=parameter_candidates, n_jobs=-1)

    # Train the classifier on training data
    clf.fit(X_train, y_train)

    # Print out the results 
    print('Best score for training data:', clf.best_score_)
    print('Best `C`:',clf.best_estimator_.C)
    print('Best kernel:',clf.best_estimator_.kernel)
    print('Best `gamma`:',clf.best_estimator_.gamma)
    
 
def model_SVC(digits):
    # Split the data into training and test sets 
    
    X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(digits.data, digits.target, digits.images, test_size=0.25, random_state=42)

    

    # Create the SVC model 
    svc_model = svm.SVC(gamma=0.001, C=100., kernel='linear')

    # Fit the data to the SVC model
    svc_model.fit(X_train, y_train) 
    
    return svc_model, X_train, X_test, y_train, y_test, images_train, images_test
 
 
def homogeneity_score(clf, X_test, y_test, X_train, y_train, y_pred):
    """
    inertia    homo   compl  v-meas     ARI AMI  silhouette
    54276     0.688   0.733   0.710   0.567   0.674    0.146
    """
    from sklearn.metrics import homogeneity_score, completeness_score, v_measure_score, adjusted_rand_score, adjusted_mutual_info_score, silhouette_score
    print('% 9s' % 'inertia    homo   compl  v-meas     ARI AMI  silhouette')
    print('%i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
              %(clf.inertia_,
          homogeneity_score(y_test, y_pred),
          completeness_score(y_test, y_pred),
          v_measure_score(y_test, y_pred),
          adjusted_rand_score(y_test, y_pred),
          adjusted_mutual_info_score(y_test, y_pred),
          silhouette_score(X_test, y_pred, metric='euclidean'))) 

def show_prediction_confusion_matrix(y_test, y_pred):
    # Import `metrics` from `sklearn`
    from sklearn import metrics

    # Print out the confusion matrix with `confusion_matrix()`
    print(metrics.confusion_matrix(y_test, y_pred))   
   
def predict_labels(clf, X_test, y_test, X_train, y_train):
    # Predict the labels for `X_test`
    y_pred=clf.predict(X_test)

    # Print out the first 100 instances of `y_pred`
    print(y_pred[:100])

    # Print out the first 100 instances of `y_test`
    print(y_test[:100])

    # Study the shape of the cluster centers
    clf.cluster_centers_.shape
    
    # display results
    from sklearn.manifold import Isomap

    # Create an isomap and fit the `digits` data to it
    X_iso = Isomap(n_neighbors=10).fit_transform(X_train)

    # Compute cluster centers and predict cluster index for each sample
    clusters = clf.fit_predict(X_train)

    # Create a plot with subplots in a grid of 1X2
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))

    # Adjust layout
    fig.suptitle('Predicted Versus Training Labels', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)

    # Add scatterplots to the subplots 
    ax[0].scatter(X_iso[:, 0], X_iso[:, 1], c=clusters)
    ax[0].set_title('Predicted Training Labels')
    ax[1].scatter(X_iso[:, 0], X_iso[:, 1], c=y_train)
    ax[1].set_title('Actual Training Labels')

    # Show the plots
    plt.show()  


    return y_pred
    
   
    
def cluser_digits(X_train):
    # Import the `cluster` module
    from sklearn import cluster

    # Create the KMeans model
    clf = cluster.KMeans(init='k-means++', n_clusters=10, random_state=42)

    # Fit the training data to the model
    clf.fit(X_train)
    return clf

def show_cluster_digits(clf):    
    import matplotlib.pyplot as plt

    # Figure size in inches
    fig = plt.figure(figsize=(8, 3))

    # Add title
    fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

    # For all labels (0-9)
    for i in range(10):
        # Initialize subplots in a grid of 2X5, at i+1th position
        ax = fig.add_subplot(2, 5, 1 + i)
        # Display images
        ax.imshow(clf.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
        # Don't show the axes
        plt.axis('off')

    # Show the plot
    plt.show()
    
    
    
    
    
    
def split_data_into_training_and_test(data, digits):
    from sklearn.cross_validation import train_test_split
    import numpy as np
    
    # Split the `digits` data into training and test sets
    X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(data, digits.target, digits.images, test_size=0.25, random_state=42)
 
    # Number of training features
    n_samples, n_features = X_train.shape

    print('n_samples = ', n_samples)
    print('n_features = ', n_features)

    # Number of Training labels
    n_digits = len(np.unique(y_train))
    print(len(y_train))
    
    return X_train, X_test, y_train, y_test 

 
def preprocess_data(digits):
    from sklearn.preprocessing import scale
    data = scale(digits.data)   
    return data

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
