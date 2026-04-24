import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def generate_random_numbers(count):
    """Generates a list of random numbers."""
    return np.random.normal(0, 1, count)

# streamlit app to plot random numbers
st.title("Random Number Generator")

# get user input
count = st.slider("Select the number of random numbers to generate", 1, 5000, 100)
st.write(f"Histogram of values from {count} random draws from a normal distribution ...")

# do something with user input
random_numbers = generate_random_numbers(count)

# plot using matplotlib
fig, ax = plt.subplots()
ax.hist(random_numbers, bins=30, alpha=0.7, color='blue')
ax.set_ylabel("Frequency")
ax.set_xlabel("Value")

# display the plot using streamlit
st.pyplot(fig)