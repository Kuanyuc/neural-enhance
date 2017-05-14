from matplotlib import pyplot as plt 
import numpy as np
import os
import sys


def main():
	loss_file = sys.argv[1]
	losses = np.genfromtxt(loss_file, delimiter = ' ')
	plt.figure(1)
	plt.subplot(221)
	# smoothnes loss
	plt.plot(range(len(losses[:,0])), losses[:, 0])
	plt.xlabel('smoothness loss')
	plt.subplot(222)
	# perceptual loss
	plt.plot(range(len(losses[:,1])), losses[:, 1])
	plt.xlabel('perceptual loss')
	plt.subplot(223)
	# adversarial loss
	plt.plot(range(len(losses[:,2])), losses[:, 2])
	plt.xlabel('adversarial loss')
	plt.subplot(224)
	# discrminator loss
	plt.plot(range(len(losses[:,3])), losses[:, 3])
	plt.xlabel('discrminator loss')
	plt.show()
	plt.close('all')
	return

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("Usage: python {} loss_file_name".format(sys.argv[0]))
		exit()
	main()