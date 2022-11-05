#thema 4.I
#euklidean Distance a)
x = c(1,2,3,4,5,6)
y = c(1,2,3,4,5,6)
euklideanDistance <- function(x, y) sqrt(sum((x - y)^2))
euklideanDistance(x,y)

#euklidean Distance b)
x = c(-0.5,1,7.3,7,9.4,-8.2,9,-6,-6.3)
y = c(0.5,-1,-7.3,-7,-9.4,8.2,-9,6,6.3)
euklideanDistance <- function(x, y) sqrt(sum((x - y)^2))
euklideanDistance(x,y)


#euklidean Distance c)
x = c(-0.5,1,7.3,7,9.4,-8.2)
y = c(1.25,9.02,-7.3,-7,5,1.3)
euklideanDistance <- function(x, y) sqrt(sum((x - y)^2))
euklideanDistance(x,y)

#euklidean Distance d)
x = c(0,0,0.2)
y = c(0.2,0.2,0)
euklideanDistance <- function(x, y) sqrt(sum((x - y)^2))
euklideanDistance(x,y)

#thema 4.II.A
x1 = c(25000, 14, 7)
x2 = c(42000, 17, 9)
x3 = c(55000, 22, 5)
x4 = c(27000, 13, 11)
x5 = c(58000, 21, 13)


euklideanDistance <- function(x1, x5) sqrt(sum((x1 - x5)^2))
euklideanDistance(x1,x5)
dist15 = euklideanDistance(x1, x5)

euklideanDistance <- function(x2, x5) sqrt(sum((x2 - x5)^2))
euklideanDistance(x2,x5)
dist25 = euklideanDistance(x2, x5)

euklideanDistance <- function(x3, x5) sqrt(sum((x3 - x5)^2))
euklideanDistance(x3,x5)
dist35 = euklideanDistance(x3, x5)

euklideanDistance <- function(x4, x5) sqrt(sum((x4 - x5)^2))
euklideanDistance(x4,x5)
dist45 = euklideanDistance(x4, x5)

#thema 4.II.B
dist55 = 0
pinakas = data.frame (dist = c(dist15, dist25, dist35, dist45, dist55),
                      time = c(25000,42000,55000,27000,58000),
                      sms = c(12,17,22,13,21),
                      mb = c(7,9,5,11,13))

model = lm(dist ~ time + sms + mb, data = pinakas)

summary(model)$r.squared

model1 = lm(dist ~ time , data = pinakas)

summary(model1)$r.squared


model2 = lm(dist ~ sms, data = pinakas)

summary(model2)$r.squared

model3 = lm(dist ~ mb, data = pinakas)

summary(model3)$r.squared


