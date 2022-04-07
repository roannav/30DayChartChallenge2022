import matplotlib.pyplot as plt
from pywaffle import Waffle

# font is stored in this project directory
my_font_file = './emojione-color-master/EmojiOneColor.otf'


'''
plots (dict) –
Position and parameters of Waffle class for subplots in a dict, with format like {pos: {subplot_args: values, }, }.

Pos could be a tuple of three integer, where the first digit is the number of rows, the second the number of columns, and the third the index of the subplot.


The parameters of subplots are the same as Waffle class parameters, excluding plots itself.
If any parameter of subplots is not assigned, it use the same parameter in Waffle class as default value.
'''

fig = plt.figure(        # creature a figure with no Axes
    FigureClass=Waffle,
    plots={
        (12,1,1): {
            'values': [1, 9],
            'colors': ("#503335", "brown"),
            'characters': ('🏃','🐻'),
            'title': {
                'label': 'Man vs. Bear',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,2): {
            'values': [1, 9],
            'colors': ("#503335", "#ff8000"),
            'characters': ('🏃','🦁'),
            'title': {
                'label': 'Man vs. Lion',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,3): {
            'values': [1, 9],
            'colors': ("#503335", "blue"), # "#232066"),
            'characters': ('🏃','🐘'),
            'title': {
                'label': 'Man vs. Elephant',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,4): {
            'values': [1, 9],
            'colors': ("#592f2a", "#5946B2"),
            'characters': ('🙎','🦍'),
            'title': {
                'label': 'Man vs. Gorilla',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,5): {
            'values': [1, 9],
            'colors': ("#592f2a", "#5E8C31"),
            'characters': ('👨','🐊'),
            'title': {
                'label': 'Man vs. Crocodile',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,6): {
            'values': [1, 9],
            'colors': ("#592f2a", "grey"),
            'characters': ('🙎','🐺'),
            'title': {
                'label': 'Man vs. Wolf',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,7): {
            'values': [2, 8],
            'colors': ("#592f2a", "#299617"),
            'characters': ('👨','🐍'),
            'title': {
                'label': 'Man vs. King Cobra',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,8): {
            'values': [2, 8],
            'colors': ("#592f2a", "#FF6EFF"),
            'characters': ('🙎','🐒',),
            'title': {
                'label': 'Man vs. Chimpanzee',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,9): {
            'values': [3, 7],
            'colors': ("#592f2a", "red"),
            'characters': ('👨','🦅'),
            'title': {
                'label': 'Man vs. Eagle',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,10): {
            'values': [5, 5],
            'colors': ("#592f2a", "#0080ff"),
            'characters': ('🙎','🐕'),
            'title': {
                'label': 'Man vs. Medium-sized Dog',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,11): {
            'values': [6, 4],
            'colors': ("#592f2a", "#ff00ff"),
            'characters': ('👨','🦆'),
            'title': {
                'label': 'Man vs. Goose',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
        (12,1,12): {
            'values': [7, 3],
            'colors': ("#592f2a", "#8000ff"),
            'characters': ('👦','😾'),
            'title': {
                'label': 'Man vs. House Cat',
                'loc': 'left',
                'fontdict': {
                    'fontsize': 15
                }
            }
        },
    },

    facecolor='#DDDDDD',
    font_file = my_font_file,
    font_size=40,

    # ratio of horizontal distance between blocks to block's width
    interval_ratio_x = 0.8,

    # ratio of vertical distance between blocks to block's height
    interval_ratio_y = 1.1,

    plot_anchor='S',
    rows=1,
    figsize=(8, 13)  # dimensions of the figure in inches
)

# print title
fig.text(
    x=0.5,
    y=1,
    s="Who Wins the Fight?",
    ha="center",
    va="top",
    fontsize=40,
    color='Black',
)

# print in lower left corner
# 0.01 for a little padding
fig.text(0.01, 0, "* No animals were harmed in the making of this survey.")

#fig.show()   # can't display, if using a no GUI console

# Opps, this is for plotly's kaleido
#fig.write_image("day2_pictogram.png")

# For matplotlib.pyplot
plt.savefig("day2_pictogram.png")

