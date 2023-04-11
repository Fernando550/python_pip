import utils
import read_csv
import charts

country = []
world_population = []

def chart_poplulation():
  data = read_csv.read_csv("data.csv")
  # get the country 
  country = input("Type country => ")

  list_country = utils.population_by_country(data,country)
  if len(list_country) > 0:
    country = list_country[0]
    labels,values = utils.get_population(country)
    print(values)
    charts.generate_bar_chart(country["Country"],labels, values)

def getWorldPoulation(item):
  new_item = {}
  new_item["Country"] = item["Country"]
  new_item["World Population Percentage"] = item["World Population Percentage"]
  
  return new_item
  
  
def chart_column():
  try:
    data = read_csv.read_csv("data.csv")
    world_countries_labels = list(map(lambda item: item["Country"], data))
    world_population_values = list(map(lambda item: item["World Population Percentage"], data))
    charts.generate_pie_chart(world_countries_labels, world_population_values)
  except SyntaxError as typo:
    # print("something went rwon")
    print(typo)
  

if __name__ == '__main__':
    chart_poplulation()
    

  