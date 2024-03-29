import matplotlib.pyplot as plt
import imageio

plt.ion()

def plot(scores, mean_scores, num_games):
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.draw()
    plt.pause(0.001)
    plt.savefig('plot.png')  # Save the plot as an image file

    # Append the current plot as an image to the GIF
    image = imageio.imread('plot.png')
    imageio.imwrite('C:/Users/maxwe/Documents/Github repos/snake-game-pytorch/snake-pygame/images/plot.gif', image)