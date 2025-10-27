import matplotlib.pyplot as plt

def plot_history(hist, save_dir):
    print(hist.history.keys())
    epochs = hist.epoch
    # loss
    plt.figure(1)
    plt.plot(epochs, hist.history['loss'], label='training loss')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend()
    plt.savefig(save_dir + "/loss.png")
 
    # mse
    plt.figure(2)
    plt.plot(epochs, hist.history['mean_absolute_error'], label='training mae')
    plt.xlabel('epoch')
    plt.ylabel('mean absolute error')
    plt.legend()
    plt.savefig(save_dir + "/mae.png")