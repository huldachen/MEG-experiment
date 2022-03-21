"""
Plot the K-Means Results
MEG_data is a matrix with 125 rows, corresponding to the data from 125 different trials (the subject viewed one of the 25 images in each trial), and 306 columns, corresponding to the response in each of the 306 MEG sensors. 
stim_ID is a 125-element row vector containing which stimulus or image (ordered 1-25) the subject was viewing in each trial.
cat_ID is a 125-element row vector containing which of the 5 stimulus or scene categories ('beach', 'building', 'forest', 'highway', or 'mountain', ordered 1-5).
MEG_data(i,:) contains the MEG response in all 306 sensors to the image labeled with stim_ID(i) and cat_ID(i). MEG_data(i,j) contains the response in the jth sensor (j=1:306) to the ith (1:125) stimulus.
"""

load('kmeans_results.mat');
load('MEG_decoding_data_final.mat');
X = MEG_data(:,[200,233]);

figure
x1 = X(IDX==1,1); y1 = X(IDX==1,2) ; 
plot(x1,y1,'b.','MarkerSize',16);
xlabel('Sensor 200 (T x 10^-12)'); ylabel('Sensor 233 (T x 10^-12)');
set(gca,'Xticklabel', {'-8','-6','-4','-2','0','2','4'});
set(gca,'Yticklabel', {'-6','-4','-2','-0','2','4','6'});

x2 = X(IDX==2,1); y2 = X(IDX==2,2); 
plot(x2,y2,'r.','MarkerSize',16);
x3 = X(IDX==3,1); y3 =X(IDX==3,2); 
plot(x3,y3,'g.','MarkerSize',16);
x4 = X(IDX==4,1); y4 = X(IDX==4,2); 
plot(x4,y4,'k.','MarkerSize',16);
x5 = X(IDX==5,1); y5 = X(IDX==5,2); 
plot(x5,y5,'m.','MarkerSize',16);


%%K-Means Replicates
load('kmeans_results.mat');
load('MEG_decoding_data_final.mat');
X = MEG_data(:,[200,233]);
IDX = kmeans(X,5);
disp(X)
        
figure
plot(X(IDX==1,1),X(IDX==1,2),'b.','MarkerSize',16)
hold on
plot(X(IDX==2,1),X(IDX==2,2),'r.','MarkerSize',16)
plot(X(IDX==3,1),X(IDX==3,2),'g.','MarkerSize',16)
plot(X(IDX==4,1),X(IDX==4,2),'k.','MarkerSize',16)
plot(X(IDX==5,1),X(IDX==5,2),'m.','MarkerSize',16)

xlabel('Sensor 200 (T x 10^-12)');
ylabel('Sensor 233 (T x 10^-12)');
set(gca,'Xticklabel', {'-8','-6','-4','-2','0','2','4'});
set(gca,'Yticklabel', {'-6','-4','-2','-0','2','4','6'});

