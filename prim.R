library(effsize)
data = read.csv("a.csv", header=FALSE)

# V2:F1, V3:F2, V4:duration 

ei = data[1:9,]
eii = data[10:18,]
eu = data[19:27,]
euu = data[28:36,]
ti = data[37:45,]
tii = data[46:54,]
tu = data[55:63,]
tuu = data[64:72,]

welch = function(){
  fd = menu(c("F1", "F2", "duration"))
  if(fd == 1){
    row_name = "V2"
  }else if(fd == 2){
    row_name = "V3"
  }else if(fd == 3){
    row_name = "V4"
  }
  lang = menu(c("EN", "TH"))
  vowel = menu(c("/i/", "/u/"))
  if(lang==1 & vowel==1){
    return(t.test(ei[,row_name],eii[,row_name]))
  }else if(lang==1 & vowel==2){
    return(t.test(eu[,row_name],euu[,row_name]))
  }else if(lang==2 & vowel==1){
    return(t.test(ti[,row_name],tii[,row_name]))
  }else if(lang==2 & vowel==2){
    return(t.test(tu[,row_name],tuu[,row_name]))
  }
}
