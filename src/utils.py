def plt_decorate(ax, title, x_label, y_label, despine = True):
    """
    Decorate the plot with title and labels.
    """
    if despine:
        ax.spines["left"].set_visible(True)
        ax.spines["bottom"].set_visible(True)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
    
    ax.set_title(title, fontsize = 16)
    ax.set_xlabel(x_label, fontsize = 12)
    ax.set_ylabel(y_label, fontsize = 12)