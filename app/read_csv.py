import csv

def read_csv(path):
  with open(path, "r") as csvfile:      
    reader = csv.reader(csvfile, delimiter= ",") #create a list for each line
    header = next(reader) #get the keys 
    data = []
    for row in reader:
      iterable = zip(header, row) #for each list make a tuple with array header
      #get the key: header and value :row []
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict) #add to data in dict form
    return data
    
def readCsvFilePopulation(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country = {key: value for key, value in iterable if key[-5:] == "ation" or key == "Country"}
      data.append(country)
    return data

if __name__ == "__main__":
  data = read_csv("./app/data.csv")
  # print(data[0])