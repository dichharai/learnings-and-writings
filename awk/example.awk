#!/usr/bin/awk -f
BEGIN {
  print "Starting...";
  sum = 0;
}
{
  print "In a loop";
  if(sum < 5){
    sum++;
  }else{
    printf("Sum is: %s\n", sum);
  }
}
END {
  print "Ending...";
}
