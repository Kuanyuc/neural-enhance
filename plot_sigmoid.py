from matplotlib import pyplot as plt
import numpy as np
import math

def sigmoid(x,shift,mult):
    """
    Using this sigmoid to discourage one network overpowering the other
    """
    return 1.0 / (1.0 + math.exp(-(x+shift)*mult))

if __name__ == "__main__":
	fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(18,4))
	plt.plot(np.arange(-1,1,.01), [sigmoid(i,0,5) for i in np.arange(-1,1,.01)])
	ax.set_xlabel('Mean of Discriminator(Real) or Discriminator(Fake)')
	ax.set_ylabel('Multiplier for learning rate')
	plt.title('Squashing the Learning Rate to balance Discrim/Gen network performance')
	plt.show()

	print ("sigmoid(0.7, 0, 5):", sigmoid(0.7, 0, 5))
	print ("sigmoid(-0.7, 0, 5):", sigmoid(-0.7, 0, 5))