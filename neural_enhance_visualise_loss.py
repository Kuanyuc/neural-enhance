import numpy as np 
import cPickle
import matplotlib
# matplotlib.use('TkAgg')  # for visualisation + writing
# matplotlib.use('WX')  # for visualisation + writing
# matplotlib.use('Agg')  # for just writing
import matplotlib.pyplot as plt
import sys

def main():
	loss_history_file = sys.argv[1]
	save_name = sys.argv[2]
	loss_history = np.genfromtxt(loss_history_file)
	avg_period = 1

	print ("minimum loss:", np.min(loss_history))
	print ("maximum loss:", np.max(loss_history))
	loss_history_to_plot = np.zeros(len(loss_history)/avg_period)
	for i in range(0, len(loss_history_to_plot)):
		loss_history_to_plot[i] = np.average(loss_history[i*avg_period:(i+1)*avg_period])
	plt.plot(loss_history_to_plot)
	# plt.xticks(np.arange(len(loss_history_to_plot)) * avg_period)
	plt.ylabel('loss')
	plt.xlabel('iterations')
	plt.title(loss_history_file[:loss_history_file.find('.')])
	# plt.savefig(save_name)
	plt.show()
	plt.clf()

	return

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print ("Usage: python {0} loss_history_file save_name".format(sys.argv[0]))
		exit()
	main()