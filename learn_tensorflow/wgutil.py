import matplotlib.pyplot as plt

def plot_loss(history):
	loss = history.history['loss']
	val_loss = history.history['val_loss']
	epochs = range(1, len(loss) + 1)
	plt.plot(epochs, loss, 'bo', label="Training loss")
	plt.plot(epochs, val_loss, 'b', label="Validation loss")
	plt.title('Training and Validation Loss')
	plt.xlabel('Epochs')
	plt.ylabel('Loss')
	plt.legend()
	plt.show()

def plot_acc(history):
	accuracy = history.history['acc']
	val_acc = history.history['val_acc']
	epochs = range(1, len(accuracy) + 1)
	plt.plot(epochs, accuracy, 'bo', label='Training Accuracy')
	plt.plot(epochs, val_acc, 'b', label='Validation Accuracy')
	plt.title('Training and Validation accuracy')
	plt.xlabel('Epochs')
	plt.ylabel('Accuracy')
	plt.legend()
	plt.show()

def plot(history, metric):
	train_metric = history.history[metric]
	val_metric = history.history['val_' + metric]
	epochs = range(1, len(history.epoch)+1)
	plt.plot(epochs, train_metric, 'bo', label='Training ' + metric)
	plt.plot(epochs, val_metric, 'b', label='Validation ' + metric)
	plt.title('Training and Validation ' + metric)
	plt.xlabel('Epochs')
	plt.ylabel(metric)
	plt.legend()
	plt.show()

