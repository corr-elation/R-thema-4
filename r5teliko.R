#thema 5 
cosineSimilarity<- function(a,b) {(sum(a*b))/sqrt((sum(a^2))*(sum(b^2)))}

x=c(9.32, -8.3, 0.2)
y=c(-5.3, 8.2, 7)
cos=cosineSimilarity(x,y)
cos 

x=c(6.5, 1.3, 0.3, 16, 2.4, -5.2, 2, -6, -6.3)
y=c(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)
cos=cosineSimilarity(x,y)
cos 

x=c(-0.5, 1, 7.3, 7, 9.4, -8.2)
y=c(1.25, 9.02, -7.3, -7, 15, 12.3)
cos=cosineSimilarity(x,y)
cos 

x=c(2, 8, 5.2)
y=c(2, 8, 5.2)
cos=cosineSimilarity(x,y)
cos 

