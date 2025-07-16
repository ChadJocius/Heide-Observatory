import matplotlib.pyplot as plt

# Planet symbols with names
planet_symbols = [
    ('Mercury', '\u263f'),
    ('Venus', '\u2640'),
    ('Earth', '\u2295'),
    ('Mars', '\u2642'),
    ('Jupiter', '\u2643'),
    ('Saturn', '\u2644'),
    ('Uranus', '\u26e2'),
    ('Neptune', '\u2646'),
    ('Pluto', '\u2647'),
    ('Ceres', '\u26b3'),
]

# Create a figure
fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('off')  # Hide axes

# Plot each symbol in a grid
n_cols = 5
for i, (name, symbol) in enumerate(planet_symbols):
    row = i // n_cols
    col = i % n_cols
    x = col
    y = -row  # invert for top-down order
    ax.text(x, y, symbol, fontsize=50, ha='center', va='center')
    # ax.text(x, y - 0.4, name, fontsize=12, ha='center', va='top')

# Adjust plot limits
ax.set_xlim(-0.5, n_cols - 0.5)
ax.set_ylim(-2, 1)

# Save to file
plt.tight_layout()
plt.savefig('planet_symbols.png', dpi=300)
plt.show()