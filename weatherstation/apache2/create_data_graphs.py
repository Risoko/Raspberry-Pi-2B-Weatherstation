import matplotlib.pyplot as plt
from weatherstation.apache2.create_data_draw import get_all_data
from weatherstation.apache2.settings import labels, titles

def create_graphs(labels:list=labels, title:list=titles, path:str="/var/www/weatherstation"):
    """Create and save graphs in path."""
    data = get_all_data()
    date, date_label = list(data[0]), labels[0]
    for number_figure, data_graphs in enumerate(zip(data[1:], labels[1:], title), 1):
        data, data_labels, title = data_graphs
        plt.figure(number_figure)
        plt.plot(date, list(data))
        plt.ylabel(data_labels)
        plt.xlabel(date_label)
        plt.title(title)
        plt.savefig(path + '/' + title + '.png')
    return True

if __name__ == "__ main__":
    print(create_graphs())
    
        
        
        
        

