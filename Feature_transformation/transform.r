#usage transform.r ids117.csv all_117fet_values.csv
Args <- commandArgs()
fasta <- read.csv("all_pre.fa", header = F)
data <- read.csv("117res.csv", header = T)
ids <- read.csv(Args[1], header = F)

outseq <- output <- as.data.frame(t(ids))
ids <- as.data.frame(ids[-1,1])

name <- c(1)
fa <- c(1)
ji <- ij <- c(1)
for (ii in 1:nrow(fasta)) {
  if(grepl(">", fasta[ii, 1], perl = T)){
    name[ji] <- as.character(fasta[ii, 1])
    ji <- ji + 1
  }else{
    fa[ij] <- as.character(fasta[ii, 1])
    ij <- ij + 1
  }
}

l_ids <- nrow(ids) + 1
for (j in 1:length(fa)) {
  fas <- as.character(fa[j])
  ds <- as.data.frame(strsplit(fas, split = "", perl = T))
  sequen <- values <- c(1)
  for (i in 1:nrow(ids)) {
    id <- as.numeric(ids[i,1])
    dss <- as.data.frame(data[data$Residue == id, ])
    if(as.character(ds[id, 1]) == as.character("X")){
      values[i] <- mean(dss$average[1:20]) # "X" means colud be any AA, the value of X take average of all 20 nature AA`s values
      sequen[i] <- c("X")
    }else{
      dsss <- as.data.frame(dss[dss$Substitution == as.character(ds[id, 1]), ])
      if(nrow(dsss) == 1){
        values[i] <- dsss$average
      }else{
        values[i] <- 0
      }
      sequen[i] <- as.character(ds[id, 1])
    }
  }
  outseq[j, 1] <- output[j, 1] <- as.character(name[j])
  output[j, 2:l_ids] <- t(values)
  outseq[j, 2:l_ids] <- t(sequen)
}
colnames(outseq) <- colnames(output) <- cbind(c('name'), t(ids[,1]))
write.csv(output, Args[2], row.names  = F)
#write.csv(outseq, "all_117fet_sequences.csv", row.names  = F)
