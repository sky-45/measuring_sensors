import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
sns.set(rc={'figure.figsize':(11, 4)})
def get_plt_sensor(sensor:str, last_samples:int, arr_data:list):
    path = 'media/test.png'
    #os.remove(path)
    df = pd.DataFrame(arr_data)
    df["datetime"]=pd.to_datetime(df["datetime"])
    df = df.set_index('datetime')
    plt.plot(df['value'].sort_index().tail(last_samples))
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Valor medido')
    plt.title("Medidas sensor")
    plt.savefig(path)
    plt.close()
    return path
    

