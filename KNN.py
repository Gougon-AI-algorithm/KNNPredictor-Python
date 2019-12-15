import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar
import pandas as pd
import matplotlib.pyplot as plt
from DFHelper import DFHelper
from Factor import Factor

PITCH_TEXT = 'Pitch : '
NEEDED_NAME = ['R80721', 'R80790']
NEEDED_ATTR = ['Ba', 'P', 'Ws']

df_helper = DFHelper()

def click_select_file_button():
    filepath = filedialog.askopenfilename()
    _load_csv(filepath)
    
def _load_csv(filepath):
    dataframe = pd.read_csv(filepath, sep='\t')
    df_helper.set_dataframe(dataframe)
    df_helper.choose_needed_data(NEEDED_NAME, NEEDED_ATTR)
    df_helper.drop_na()
    df_helper.transform_df_to_float()
    dataframe = df_helper.get_dataframe()
    plt.scatter(df_helper.get_column('Ws'), df_helper.get_column('P'))
    plt.show()
    
def click_predict_button():
    wind = wind_textbox.get()
    power = power_textbox.get()
    factor = Factor(wind, power, 0)
    neighbors = _find_neighbors(df_helper.get_dataframe(), factor)
    pitch = _calc_most_appear_pitch(neighbors)
    pitch_text.set(PITCH_TEXT + str(pitch))
    
def _find_neighbors(dataframe, predicted_factor):
    euclidean_dict = _get_all_euclidean_distances(dataframe, predicted_factor)
    neighbors_key = _get_neighbors_key(euclidean_dict)
    neighbors = _make_neighbors(neighbors_key, dataframe)
    return neighbors
    
def _get_all_euclidean_distances(dataframe, predicted_factor):
    euclideanDict = {}
    for count in range(len(dataframe)):
        factor = _make_factor(count, dataframe)
        euclideanDict[count] = factor.get_euclidean(predicted_factor)
    return euclideanDict

def _get_neighbors_key(euclidean_dict):
    neighbors_key = []
    for i in range(0, 10):
        min_key = min(euclidean_dict, key=euclidean_dict.get)
        neighbors_key.append(min_key)
        del euclidean_dict[min_key]
    return neighbors_key

def _make_neighbors(neighbors_key, dataframe):
    neighbors = []
    for i in range(0, 10):
        factor = _make_factor(i, dataframe)
        neighbors.append(factor)
    return neighbors
        
def _make_factor(count, dataframe):
    row = dataframe.iloc[count]
    pitch = row[0]
    power = row[1]
    wind = row[2]
    return Factor(wind, power, pitch)

def _calc_most_appear_pitch(neighbors):
    pitchCounter = {}
    for neighbor in neighbors:
        _add_pitch_times(neighbor, pitchCounter)
    pitch = max(pitchCounter, key=pitchCounter.get)
    if pitch < 0:
        pitch = 0
    return pitch
        
def _add_pitch_times(neighbor, pitchCounter):
    pitch = neighbor.get_pitch()
    if pitch in pitchCounter.keys():
        pitchCounter[pitch] = pitchCounter[pitch] + 1
    else:
        pitchCounter[pitch] = 1
    
window = tk.Tk()
window.title('KNN Predictor')
window.geometry('500x240')

pitch_text = StringVar()
pitch_text.set(PITCH_TEXT)

wind_label = tk.Label(window, text='Wind : ', font=('Arial, 12'), height=1)
wind_label.place(x=20, y=40)
wind_textbox = tk.Entry(window, show=None, font=('Arial, 12'))
wind_textbox.place(x=90, y=40)
    
power_label = tk.Label(window, text='Power : ', font=('Arial, 12'), height=1)
power_label.place(x=20, y=110)
power_textbox = tk.Entry(window, show=None, font=('Arial, 12'))
power_textbox.place(x=90, y=110)
    
pitch_label = tk.Label(window, textvariable=pitch_text, font=('Arial, 12'), height=1)
pitch_label.place(x=20, y=180, anchor='nw')
    
select_file_button = tk.Button(window, text='Select file', font=('Arial, 12'), command=click_select_file_button, width=11, height=1)
select_file_button.place(x=350, y=70)
    
predict_button = tk.Button(window, text='Predict', font=('Arial, 12'), command=click_predict_button, width=11, height=1)
predict_button.place(x=350, y=175)
window.mainloop()
    
