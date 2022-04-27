import matplotlib.pyplot as plt
import numpy as np
from random import randint
import streamlit as st


###############################################################
#  People 
###############################################################

person = '😎'

people = [ '🕵️‍♀️', '🕵️‍♂️', '😎', '😐', '😴', '😷', '😀', 
    '🙋‍♀️', '🙋‍♂️', '🙍‍♀️', '🙍‍♂️', '🤓', '🤔',
    '🤗', '🤠', '🤡', '🤦‍♀️', '🤦‍♂️', '🤦', '🤧', '🤨',
    '🤪', '🤴', '🤵‍♀️', '🤵‍♂️', '🤵', '🤶', '🤷‍♀️',
    '🤷‍♂️', '🤷', '🤹‍♀️', '🥱', '🥴', ]

num_people_types = len(people)

# OUT: returns a random person from the people list
def random_person():
    ind = randint(0,num_people_types - 1)
    return people[ind] 
    

###############################################################
#  Chair
###############################################################

chair = '🪑'

chair_list = [ chair ] * 100  # list of 100 chairs


def fill_chair_list_packed_together( accept_rate):
    chair_index = 0
    filled_chairs = 0
    while (filled_chairs < accept_rate):
        chair_list[chair_index] = person
        filled_chairs += 1
        chair_index += 1


# Many different ways to kinda randomly fill the seats.  Here's one:
#
# pass 1:  start at the first chair, then consider each chair one 
# at a time, using this rule:
# while more chairs need to be filled  and we haven't reached the last chair,
#    skip every 0-2 chairs, then place a person there
#    move to the next chair
#
# pass 2:  start at the first chair, then consider each chair one
# at a time, using this rule:
# while more chairs need to be filled:
#    find the next blank chair and fill it
def fill_chair_list( accept_rate):
    # pass 1
    chair_index = 0    # start at the first chair
    filled_chairs = 0
    while (filled_chairs < accept_rate and chair_index < 100):
        # NOTE: each time the below code runs, 
        # filled_chairs will increase by 1
        # and chair_index will increase by 1..3

        # skip some chairs, maybe
        skip_seat = randint(0,2)  # 0..2 inclusive
        chair_index += skip_seat

        if (chair_index < 100):
            # put a person here
            chair_list[chair_index] = random_person()
            filled_chairs += 1
            chair_index += 1
   
    # pass 2
    chair_index = 0    # start at the first chair
    while (filled_chairs < accept_rate):
        assert chair_index < 100, "ERROR: chair_index >= 100"
        if chair_list[chair_index] == chair:   # empty chair
            # put a person here
            chair_list[chair_index] = random_person()
            filled_chairs += 1
        chair_index += 1


def draw_chairs():
    # chairs are numbered 0..99, starting from the top left chair
    # Draw a 2D chair matrix, where each row has ROW_LENGTH chairs.
    chair_index = 0
    ROW_LENGTH = 15
    for row in range(ROW_LENGTH):
        # create the string representation of the row
        sublist =  chair_list[ row*ROW_LENGTH : 
                               min(99, (row+1)*ROW_LENGTH) ]
        s = ''.join(sublist)

        # draw row
        st.write(s)


###############################################################
#  Web Page
###############################################################

#st.title("College Admissions Simulator")
st.header("College Admissions Simulator")

accept_rate = st.slider("Please use the slider to choose how easy it will be to get into college (100 is easiest, 1 is hardest)", 1, 100, 10)

st.subheader("Results")

left_column, right_column = st.columns(2)


with left_column:
    st.write(f"Your college has an acceptance rate of {accept_rate}%.")
    st.write(f"Below is a visual depiction of {accept_rate}% chairs filled at the college lecture hall.")

    fill_chair_list( accept_rate)
    draw_chairs()


with right_column:
    # Draw matplotlib bar chart

    # From 2017, https://www.pewresearch.org/fact-tank/2019/04/09/
    # a-majority-of-u-s-colleges-admit-most-students-who-apply/
    # Added single columns together, to create a cumulative chart.
    data = {
        0: 100.0,
        10: 98.8,
        20: 96.7,
        30: 93.7,
        40: 89.0,
        50: 80.3,
        60: 66.6,
        70: 47.0,
        80: 25.5,
        90: 10.0
    }

    total_colleges = 1364

    # round down to nearest 10 
    table_key = accept_rate - accept_rate % 10  
    if accept_rate == 100:
        table_key = 90

    table_rate = data[table_key]
    table_number = int(table_rate * total_colleges / 100)
    

    st.write(f"{table_rate}% of U.S. colleges or universities ({table_number} out of {total_colleges}) has an acceptance rate of {table_key}% or higher.")

    # This is the bar we want to highlight
    # because it represents the selected accept_rate
    color_index = int(table_key / 10)

    bar_colors = [ '#011F5B'] * 10        # Wharton Blue
    bar_colors[ color_index] = '#FF4B4B'  # Streamlit primary red 
    #alt color:   '#990000'  # Wharton Red

    fig, ax = plt.subplots()

    plt.bar(list(data.keys()), list(data.values()), 
       color=bar_colors,
       width=9)

    for d in ['left','right','top','bottom']:
        ax.spines[d].set_visible(False)

    plt.xlabel("Admissions Rate %")
    plt.ylabel("Percentage of Institutions")

    ax.set(xlim=(-6, 96),
           xticks=np.arange(0, 100, 10))

    # remove tick marks, but leave tick labels
    plt.tick_params(bottom=False)
    plt.tick_params(left=False)

    st.pyplot(fig)


st.columns(1)
st.write("Data: Pew Research Center https://www.pewresearch.org/fact-tank/2019/04/09/a-majority-of-u-s-colleges-admit-most-students-who-apply/  1364 U.S. colleges or universities were surveyed in 2017.")
st.write("Viz: @roannav")
