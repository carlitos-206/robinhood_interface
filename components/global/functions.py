def globalParsing(list):
  if isinstance(list, dict):
    for k , v in list.items():
      # if isinstance(v, dict):
      #   for k, i in v.items():
      #     print(f"\n{k}: {i}\n")
      # else:
          print(f"\n{k}: {v}\n")
  else:
    print("Not Dict")
    time.sleep(2)
    print(list)
      