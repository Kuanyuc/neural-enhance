import numpy as np 
import cPickle
import matplotlib
# matplotlib.use('TkAgg')  # for visualisation + writing
# matplotlib.use('WX')  # for visualisation + writing
matplotlib.use('Agg')  # for just writing
import matplotlib.pyplot as plt
import sys

def main():
	log_file_to_parse = sys.argv[1]
	loss_type = sys.argv[2]
	save_name = sys.argv[3]

	loss_history = []
	with open(log_file_to_parse, 'rb') as f:
		for line in f.readlines():
			line = line.replace('\n', '')
			if (line.find(loss_type) != - 1):
				line_start_with_loss_info = line[line.find(loss_type) + len(loss_type):]
				line_start_with_loss = line_start_with_loss_info[line_start_with_loss_info.find('=')+1:]
				this_loss_history = float(line_start_with_loss[:line_start_with_loss.find(' ')])
				loss_history.append(this_loss_history)
	loss_history = np.asarray(loss_history)
	avg_period = 1

	print "minimum loss:", np.min(loss_history)
	print "maximum loss:", np.max(loss_history)
	loss_history_to_plot = np.zeros(len(loss_history)/avg_period)
	for i in range(0, len(loss_history_to_plot)):
		loss_history_to_plot[i] = np.average(loss_history[i*avg_period:(i+1)*avg_period])
	plt.plot(loss_history_to_plot)
	# plt.xticks(np.arange(len(loss_history_to_plot)) * avg_period)
	plt.ylabel('loss')
	plt.xlabel('epoches')
	plt.title(log_file_to_parse[:log_file_to_parse.find('.')])
	plt.savefig(save_name)
	plt.clf()

	return

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "Usage: python {0} log_file_to_parse loss_type[e.g., 'total', 'prcpt', 'smthn', 'advrs'] save_name".format(sys.argv[0])
		exit()
	main()