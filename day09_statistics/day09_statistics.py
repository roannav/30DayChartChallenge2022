import numpy as np
from scipy.stats import norm, poisson
import matplotlib.pyplot as plt
import math

plt.xkcd()   # start using xkcd style

# This code uses the OO-style matplotlib, using subplots().
fig, ax = plt.subplots(4, 3,   # 4 rows, 3 col of subplots
    figsize = (16,18)          # dimensions of the figure in inches
)


#########################################################################
#  Colors 
#########################################################################

# names from the xkcd color survey  https://xkcd.com/color/rgb/
# prefixed with 'xkcd:' (e.g., 'xkcd:sky blue');

# fairly light colors: pink, light blue, very pale green, very pale blue
# salmon, pale peach, pale salmon, light beige, ecru
# too bright: butter, light peach
# very light green is too close to pale green
# good: pale peach, very light purple, very light pink

# set axes bg
# row 0
ax[0,0].set_facecolor('xkcd:pale peach')
ax[0,1].set_facecolor('xkcd:pale peach')
#ax[0,2] is covered by the drawing

# row 1
ax[1,0].set_facecolor('xkcd:pale green')
ax[1,1].set_facecolor('xkcd:pale green')
ax[1,2].set_facecolor('xkcd:pale green')

# row 2
ax[2,0].set_facecolor('xkcd:creme')
ax[2,1].set_facecolor('xkcd:creme')
ax[2,2].set_facecolor('xkcd:creme')

# row 3
ax[3,0].set_facecolor('xkcd:very light blue')
ax[3,1].set_facecolor('xkcd:very light blue')
ax[3,2].set_facecolor('xkcd:very light blue')


#########################################################################
#  Title Area
#########################################################################

# main title above everything else
plt.suptitle("Poisson Distribution", 
    fontsize=30,
    fontweight='bold'
)

# text just below the title
plt.figtext(0.069, 0.92,
    "What if you study and listen to music for 4 hours...  What's the distribution of the number of favorite songs you'll hear?",
    ha="left",
    fontsize=18)


#########################################################################
#  Helper Functions 
#########################################################################

def make_text_section( _ax):
    # remove spines
    for loc in ['top','right','bottom','left']:
        _ax.spines[loc].set_visible(False)

    # remove x ticks and y ticks
    _ax.set_xticks([])
    _ax.set_yticks([])


TOP = 0.94
CENTER = 0.4  #0.45
BOTTOM = 0.04

LARGE_FONT_SIZE = 28

def write_text( _ax, y, txt, _fontsize=18):
    _ax.text(0.04,
        y,
        txt,
        ha="left",  # horizontalalignment
        va= "top" if y==TOP else "bottom",
        fontsize=_fontsize)


# Use Poisson Distribution formula
def calc_prob( _lambda, k):
    return math.exp(-_lambda) * pow(_lambda, k) / math.factorial(k)

# 0.13958653195059692
#print(f"Probability of 8 events is {calc_prob( 8, 8)}")

 
#########################################################################
#  subplot 0,0:  
#########################################################################

make_text_section(ax[0][0])
write_text( ax[0,0], TOP, "Hard Way: Do the experiment\n1000 times.") 
write_text( ax[0,0], CENTER, "Listen for 1000 * 4 hours.") 
write_text( ax[0,0], BOTTOM, "Record how many times the event\noccurs in each of the 4 hours.") 


#########################################################################
#  subplot 0,1:  A histogram shows frequency distributions.
#  It shows how many occurrences happen within each bin.
#########################################################################

ax[0,1].set_title("Histogram", 
    {'color':'blue', 'size':20})
ax[0,1].set_xlabel("events")
ax[0,1].set_ylabel("count")

# Poisson distributions:
#     are always right skewed. 
#     mean = μ = λ 
#     standard deviation = σ = sqrt( λ) 

# mean = lambda = (avg events / time) * (time period)
#      = (1/30 min)(4 hr)(60 min/hr) = 8

# std dev = sqrt( λ) = sqrt(8)

# This is an approximation of running the experiment.
# np.random.normal( mean, std_dev, num_samples)
#     generates a random list that is num_samples long.
x = np.random.normal(8, math.sqrt(8), 1000)
x = x[x>=0]  # remove negative numbers

ax[0,1].hist(x,20)  # plot histogram with 20 bins


#########################################################################
#  subplot 0,1: Drawing 
#########################################################################

# remove x ticks and y ticks
ax[0][2].set_xticks([])
ax[0][2].set_yticks([])

im = plt.imread('headphones.jpg') # load image
ax[0][2].imshow(im)


#########################################################################
#  subplot 1,0: Poisson Process 
#  subplot 1,1:  
#  subplot 1,2:  
#########################################################################

make_text_section(ax[1][0])
write_text( ax[1,0], TOP, "event = Hearing a favorite\nsong from streaming music") 
write_text( ax[1,0], CENTER, "This is a ...") 
write_text( ax[1,0], BOTTOM, "Poisson Process", _fontsize=LARGE_FONT_SIZE) 

make_text_section(ax[1][1])
write_text( ax[1,1], TOP, "A) average time between events\nis a constant.") 
write_text( ax[1,1], BOTTOM, "If you hear a favorite song on\naverage every 30 minutes, then\naverage time between events is\n1/2 hour.") 

make_text_section(ax[1][2])
write_text( ax[1,2], TOP, "B) actual timing of events is\nrandom.") 
write_text( ax[1,2], CENTER, "C) events are independent;  they\ndon't affect each other.") 
write_text( ax[1,2], BOTTOM, "D) two events can't occur at the\nsame time.") 


#########################################################################
#  subplot 2,0:  
#########################################################################

make_text_section( ax[2,0])

write_text( ax[2,0], TOP, "Poisson Distribution", _fontsize=LARGE_FONT_SIZE) 
write_text( ax[2,0], CENTER, "==> Find probability of k events\nhappening in a time period") 


#########################################################################
#  subplot 2,1:  
#########################################################################

make_text_section( ax[2,1])

write_text( ax[2,1], TOP, "P(k events in time interval)") 
write_text( ax[2,1], CENTER, r"= $e^{-\lambda} \frac{\lambda^k}{k!}$", 
    _fontsize=LARGE_FONT_SIZE)
write_text( ax[2,1], BOTTOM, r"$\lambda$ lambda is the rate parameter.") 


#########################################################################
#  subplot 2,2:  
#########################################################################

ax[2,2].set_title("Poisson Distribution", 
    {'color':'blue', 'size':20})
ax[2,2].set_xlabel("k")
ax[2,2].set_ylabel("P(k events in interval t)")

events_per_hour = 2   # events per interval
hours = 4   # interval

# lambda aka rate parameter or expected number of events in an interval
lamb = events_per_hour * hours

# Poisson Probability Density Function
# = probability of a number of events, k, in an interval

lin = np.arange(0,20)  # ints 0..19

ax[2,2].plot(lin, poisson(2).pmf(lin), c='r')
ax[2,2].plot(lin, poisson(7).pmf(lin), c='g')
ax[2,2].plot(lin, poisson(14).pmf(lin), c='b')

ax[2,2].legend(['lambda=2', 'lambda=7', 'lambda=14'] )


#########################################################################
#  subplot 3,0:  
#########################################################################

make_text_section( ax[3,0])

write_text( ax[3,0], TOP, r"$\lambda$ lambda", _fontsize=LARGE_FONT_SIZE)
write_text( ax[3,0], CENTER, "is the expected number of events\nin the interval.") 
write_text( ax[3,0], BOTTOM, r"$\lambda = \frac{events}{time}$ * time period") 


#########################################################################
#  subplot 3,1:  
#########################################################################

ax[3,1].set_title("Poisson Distribution", 
    {'color':'blue', 'size':20})
ax[3,1].set_xlabel("k")
ax[3,1].set_ylabel("P(k events in interval t)")

# draw horizontal and vertical lines to the point on the curve that
# shows the probability of getting 8 events during the interval.
y2 = 0.14  # P(8) = 0.13958653195059692
ax[3,1].plot([8,8], [0,0.14], c='grey')
ax[3,1].plot([0,8], [0.14,0.14], c='grey')

lin = np.arange(0,20)  # ints 0..19

# param #1: array with all the x values
# param #2: array with all the y values
poisson_curve, = ax[3,1].plot(lin, poisson(lamb).pmf(lin), c='red')


# There are 3 lines plotted.
# But I only want to show the 3rd line in the legend.
ax[3,1].legend(handles=[poisson_curve], labels=['lambda=8'])


ax[3,1].text(0, 0.139, "14%", ha="left", va="top", fontsize=18)

txt = r"$\lambda = \frac{1}{1/2}$ * 4 =8" 
ax[3,1].text(12, 0.09, txt, ha="left", va="bottom", fontsize=18)


#########################################################################
#  subplot 3,2:  
#########################################################################

make_text_section( ax[3,2])

write_text( ax[3,2], TOP, r"$\lambda$ = 8, means 8 expected events." + "\nIt's also the most likely outcome.")
write_text( ax[3,2], CENTER, "It doesn't mean we'll get 8 events.") 
write_text( ax[3,2], BOTTOM, "Exactly 8 events has a probability\nof just 14%.") 


#########################################################################
#########################################################################

# adjust the spacing between subplots
fig.subplots_adjust(left=0.06,
    right=0.95,
    bottom=0.07,
    top=0.89,
    wspace=0.2,
    hspace=0.5)


plt.figtext(0.069, 0.02,
    "Drawing: xkcd.com   Data Viz: @roannav",
    ha="left",
    fontsize=14)

plt.savefig('day09_statistics.png')  # savefig must happen before show()
