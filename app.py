"Alvaro Quintero"
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

with ui.sidebar():
    ui.input_slider:("selected_number_of_bins")
    ui.input_slider("n", "Number of Bins", 0, 100, 20 )


@render.plot(alt="A histogram showing random data distribution")
def histogram():
    np.random.seed(3)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.n(), density=True, color='red') 
