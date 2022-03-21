"""
Classify the data using a supervised machine learning algorithm: support vector machine (svm)
Will use the data from all of the channels, but remember, we want to use separate data to train and test the classifier. 
"""

SVMStruct = fitcsvm(train_data,train_cat_labels,'Standardize','on');
pred = predict(SVMStruct,test_data) 

load('SVM_prediction.mat');
load('MEG_decoding_data_final.mat');
        
%% Train SVMStruct classifier, then use it with fitcsvm here.
SVMStruct = fitcsvm(train_data,train_cat_labels,'Standardize','on');
pred = predict(SVMStruct,test_data)
%% Display the pred and test_cat_labels to visually compare them. 
%% Add an apostrophe to either to properly orient the data.
pred
test_cat_labels'
        
%% Calculate the accuracy of the SVM Prediction by replacing the question marks.
A = sum(pred==test_cat_labels')
accuracy = A/length(pred)
