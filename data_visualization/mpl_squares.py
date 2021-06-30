import matplotlib.pyplot as plt

styles_available = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic',
	'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn',
	'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
	'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
	'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
	'seaborn-ticks','seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# fig represents the entire figure or collection of plots that are generated.
# ax represents a single plot in the figure and is the variable we’ll use most of the time.
# subplots() can generate one or more plots in the same figure.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()