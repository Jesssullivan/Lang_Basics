# Ref:
# https://stat.ethz.ch/R-manual/R-devel/library/base/html/ifelse.html
# 
# Conditional loop: crank until car starts
#
# Constant: To get car running
Running <- 3 
RunProb <- 0
conditional <- function(){
  AddProb <- runif(1, min = .1, max = .2) # random number adding odds per crank
  WillRun <- runif(1, min = 0, max = 2) # random number starting odds for run
  i <- 0
  repeat{
    if(RunProb <= Running) {
    i <- i+1
  RunProb <- RunProb+AddProb
  cat("Cranking... Keep Cranking with R...",
    "You have cranked",i,"times so far, and your RunProb is", 
    RunProb, "out of 3",
    "...")
  cat("\n")
  Sys.sleep(.3)
    }
  else
  return(cat("Car is running after", i, "cranks"))
  }
}
conditional()  
    
