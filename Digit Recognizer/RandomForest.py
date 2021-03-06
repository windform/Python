import time
import preprocess

from sklearn.ensemble import RandomForestClassifier

def loaddata():
	print "loading data..."
	#load data in train.csv, divided into train data and validation data
	data,label = preprocess.loadTrainSet()
	val_data = data[0:6000]
	val_label = label[0:6000]
	train_data = data[6000:]
	train_label = label[6000:]
	#load data in test.csv
	test_data = preprocess.loadTestSet()
	return train_data,train_label,val_data,val_label,test_data

def rf(train_data,train_label,val_data,val_label,test_data,name="RandomForest_submission.csv"):
	print "Start training Random forest..."
	rfClf = RandomForestClassifier(n_estimators=400,n_jobs=-1)
	rfClf.fit(train_data,train_label)
	#evaluate on validation set
	val_pred_label = rfClf.predict_proba(val_data)
	logloss = preprocess.evaluation(val_label,val_pred_label)
	print "logloss of validation set:",logloss

	print "Start classify test set..."
	test_label = rfClf.predict_proba(test_data)
	preprocess.saveResult(test_label,filename = name)



if __name__ == "__main__":
	t1 = time.time()
	train_data,train_label,val_data,val_label,test_data = loaddata()
	rf(train_data,train_label,val_data,val_label,test_data) 
	t2 = time.time()
	print "Done! It cost",t2-t1,"s"