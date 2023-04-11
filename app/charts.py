import matplotlib.pyplot as plt

labels = ["a","b","c"]
values = [40, 10, 80]

def generate_bar_chart(country, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f"./imgs/{country}.png")
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.axis("equal")
  plt.savefig("pie.png")
  plt.close()

if __name__ == "__main__":
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)