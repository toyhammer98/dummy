def report_count(target):
  count = 0
  with open("corpus.txt", "r") as n:
    for line in n:
      #cleaning the text
      line = line.strip()
      line = line.lower()
      words = line.split(" ")
      print(words)
      #counting occurrences of target word
      for i in words:
        if (i == target):
          count += 1
    print("The term ",target," shows up in the corpus ",count," times.")
