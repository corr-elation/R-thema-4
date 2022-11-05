library(MASS)
data("Cars93")
head(Cars93)



summary(Cars93)

Cars93.pca = Cars93[,-c((1:3),(9:11), 16, 26, 27)]
Cars93.pca

# Does variable Sepal.Length have any (at least 1) missing (na) value? 
if (any(is.na(Cars93.pca[,]))) {
  sprintf("Data has NA values")
} else
  sprintf("Data is ok! ")

Cars93.pca = na.omit(Cars93.pca)#if data not okay

if (any(is.na(Cars93.pca[,]))) {
  sprintf("Data has NA values")
} else
  sprintf("Data is ok! ")

principalComponents = princomp(Cars93.pca, cor=FALSE, score=TRUE)

attributes(principalComponents)

#Eigenvectors
print(principalComponents$loadings)
Eigenvectors<-principalComponents$loadings[,1:18]
print(Eigenvectors)

#Eigenvalues
Eigenvalues<-principalComponents$sdev^2
print(Eigenvalues)

##### percentage ###
percent = proportions(Eigenvalues)*100
print(percent)

principalComponents$loadings
principalComponents$scores
