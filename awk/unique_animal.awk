#!/usr/bin/awk -f

BEGIN {
  print "Starting...";
}
{
  if(animals[$3] != "null"){
    animals[$3]++;
    states[$3] = $1;
  }
  if(animals[$4] != "null"){
    animals[$4]++;
    states[$4] = $1;
  }
}
END {
  printf("Unique animals found just in one state\n\n");
  count = 0;
  for (animal in animals) {
    #print( animal, " occurs ", animals[animal], " times.");
    if(animals[animal] == 1 && animal != null){
      printf("%-25s %s\n", animal, states[animal]);
      count++;
      }
  }
  printf("\n\nThere are total %s unique animals unique to a state.\n", count);
  print("Ending..."); 
}
