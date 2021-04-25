def fahr_to_celsius(temp_fahrenheit):
  return (temp_fahrenheit-32)/2.8;

def temp_classifier(temp_celsius):
  if temp_celsius<-2:
    return 0
  elif temp_celsius<2:
    return 1
  elif temp_celsius<15:
    return 2
  else:
    return 3