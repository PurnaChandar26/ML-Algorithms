import matplotlib.pyplot as plt

# Sample data
data = [25, 30, 33, 35, 36, 40, 45, 50, 55, 60]

# Create a boxplot
plt.boxplot(data)

# Add labels and title
plt.xlabel('Data')
plt.ylabel('Values')
plt.title('Boxplot')

# Display the plot
plt.show()
