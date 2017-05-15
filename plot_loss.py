from matplotlib import pyplot as plt 
import numpy as np
import os
import sys
import math

def main():
	loss_file = sys.argv[1]
	losses = np.genfromtxt(loss_file, delimiter = ' ')
	print "total number of iterations: ", len(losses)
	avg_period = 72
	plt.figure(1)
	plt.subplot(221)
	# smoothnes loss
	smooth_loss = np.zeros(int(math.ceil(len(losses[:, 0])/float(avg_period))))
	for i in range(0, len(smooth_loss)):
		smooth_loss[i] = np.mean(losses[:,0][i*avg_period:min((i+1)*avg_period, len(losses[:,0]))])
	plt.plot(range(len(smooth_loss)), smooth_loss)
	plt.xlabel('perceptual loss')
	plt.subplot(222)
	# perceptual loss
	percept_loss = np.zeros(int(math.ceil(len(losses[:, 1])/float(avg_period))))
	for i in range(0, len(percept_loss)):
		percept_loss[i] = np.mean(losses[:,1][i*avg_period:min((i+1)*avg_period, len(losses[:,1]))])
	plt.plot(range(len(percept_loss)), percept_loss)
	plt.xlabel('smoothness loss')
	plt.subplot(223)
	# adversarial loss
	adversarial_loss = np.zeros(int(math.ceil(len(losses[:, 2])/float(avg_period))))
	for i in range(0, len(adversarial_loss)):
		adversarial_loss[i] = np.mean(losses[:,2][i*avg_period:min((i+1)*avg_period, len(losses[:,2]))])
	plt.plot(range(len(adversarial_loss)), adversarial_loss)
	plt.xlabel('adversarial loss')
	plt.subplot(224)
	# discrminator loss
	disc_loss = np.zeros(int(math.ceil(len(losses[:, 3])/float(avg_period))))
	for i in range(0, len(disc_loss)):
		disc_loss[i] = np.mean(losses[:,3][i*avg_period:min((i+1)*avg_period, len(losses[:,3]))])
	plt.plot(range(len(disc_loss)), disc_loss)
	plt.xlabel('discrminator loss')
	plt.show()
	plt.close('all')
	return

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("Usage: python {} loss_file_name".format(sys.argv[0]))
		exit()
	main()