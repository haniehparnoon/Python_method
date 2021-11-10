lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana","Nevada"]
result =sum(map(lambda x: x.count("A") + x.count("a"), lst1))
print(result)




