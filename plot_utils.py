import matplotlib.pyplot as plt


def plot_results(df, x_column, y_columns, y_labels, title):
    plt.figure(figsize=(12, 8))
    for y_column, y_label in zip(y_columns, y_labels):
        if y_column in df.columns:
            y_data = df[y_column]
            if (y_data > 0).all():
                plt.plot(df[x_column], y_data, marker='o', label=y_label)
            else:
                y_data = y_data.apply(lambda x: x if x > 0 else -x)
                plt.plot(df[x_column], y_data, marker='o', label=y_label)
                print(f"Advertencia: {y_column} contiene valores no positivos y se han multiplicado por -1.")
        else:
            print(f"Advertencia: {y_column} no se encuentra en el DataFrame y será omitido.")
    plt.title(title)
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Valor")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--")
    plt.legend()
    plt.show()
