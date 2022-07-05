from scipy.stats import poisson 
import math

averageBlockMinedMin = 10 #average mine a block
consequtiveBlockMinedMin = 120 #2 hour
k = 0 # check 0 events occur

def calculateConsequtiveBlockMinedOccur(k, averageBlockMinedMin , consequtiveBlockMinedMin ):
   eventOccur = consequtiveBlockMinedMin / averageBlockMinedMin 
   posibility=poissonDistribution (k, eventOccur )
   
   day = int((1/posibility * 10) /24/60)
   hour = int(24 *( (1/posibility * 10) /24/60 - day))
   min = int( 60 *  (  24 *( (1/posibility * 10) /24/60 - day) - hour  ))
   return day, hour, min
   


def poissonDistribution(k, eventOccur ):
   return poisson.pmf(k=k, mu=eventOccur) 


day, hour, min = calculateConsequtiveBlockMinedOccur (k, averageBlockMinedMin , consequtiveBlockMinedMin )
print (day , " days ", hour , " hour ", min, " min ")
