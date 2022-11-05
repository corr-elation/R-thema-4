nominalDistance <- function(x,y)
{
  k=0
  d=0
  if (length(x) != length(y))
    return( "There are different number of variables.")
  else 
    for (i in 1:length(x) ) {
      if(x[i]==y[i])
        k=0
      else
        {
        k=1
    }
    d=d+k
  }
  
  return(d)}
x<-c("Green","Potato","Ford")
y<-c("Tyrian purple", "Pasta", "Opel")
d<-nominalDistance(x,y)
print(d)
x=c("Eagle", "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay")
y=c("Eagle","Ronaldo", "Real madrid", "Prussian blue", "Michael Bay")
d<-nominalDistance(x,y)
print(d)
x<-c("Werner Herzog", "Aquirre, the wrath of God", "Audi", "Spanish red")
y<-c("Martin Scorsese", "Taxi driver", "Toyota", "Spanish red")
d<-nominalDistance(x,y)
print(d)

