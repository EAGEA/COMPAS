def plt_decorate(ax, title, x_label, y_label, despine = True):
    """
    Decorate the plot with title and labels.
    """
    if despine:
        ax.spines["left"].set_visible(True)
        ax.spines["bottom"].set_visible(True)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        
    _ = ax.set_title(title,
                     pad = 30,
                     size = 20)
    _ = ax.set_xlabel(x_label, 
                      labelpad = 10, 
                      size = 15)
    _ = ax.set_ylabel(y_label, 
                      labelpad = 10, 
                      size = 15)