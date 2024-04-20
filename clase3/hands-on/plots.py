import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_curve


def plot_confusion_matrix(y_real, y_pred, save_path=None):

    # Chequeamos que los dataframes estén alineados
    if y_real.shape[0] != y_pred.shape[0]:
        raise ValueError("y_real and y_pred are not aligned")

    cm = confusion_matrix(y_real, y_pred)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.grid(False)
    disp.plot(ax=ax)
    ax.set_title("Matriz de confusión de modelo")

    plt.tight_layout()

    # Grabamos el gráfico si save_path es especificado
    if save_path:
        plt.savefig(save_path, format="png", dpi=600)

    # Prevemos que Matplotlib de mostrar el gráfico cada vez que llamamos a la función
    plt.close(fig)

    return fig


def plot_roc_curve(y_real, y_pred, num_class=3, save_path=None):

    # Chequeamos que los dataframes estén alineados
    if y_real.shape[0] != y_pred.shape[0]:
        raise ValueError("y_real and y_pred are not aligned")

    fig_plots = []
    for i in range(num_class):

        y_real_temp = (y_real == i).astype(int)
        y_pred_temp = (y_pred == i).astype(int)

        fpr, tpr, _ = roc_curve(y_real_temp, y_pred_temp)

        # Creamos la gráfica de barra
        fig = plt.figure(figsize=(12, 8))

        plt.plot(fpr, tpr)
        plt.title(f"Curva ROC clase {i}", fontsize=18)
        plt.xlim([-0.01, 1.01])
        plt.ylim([-0.01, 1.01])
        plt.xlabel("Tasa de falsos positivos", fontsize=16)
        plt.ylabel("Tasa de verdaderos positivos", fontsize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.grid()
        plt.tight_layout()
        fig_plots.append(fig)

        plt.close(fig)

    # Grabamos el gráfico si save_path es especificado
    if save_path:
        plt.savefig(save_path, format="png", dpi=600)

    # Prevemos que Matplotlib de mostrar el gráfico cada vez que llamamos a la función
    return fig_plots
