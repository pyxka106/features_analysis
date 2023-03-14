library(ggplot2)
library(ggpubr)

ggplot(data=df, aes(x=p_estimated, y=p_known)) + 
      geom_smooth(method = "lm", se=F) + 
      geom_point() + 
      stat_regline_equation(label.x = 0.5, label.y = 0.9) + 
      stat_cor(aes(label=..rr.label..), label.x = 0.5, label.y = 0.7)
      
# t-test using R-package
library(tidyverse)
library(rstatix)
library(ggpubr)

stat.v_2 <- v_gene_2 %>% 
            group_by(v_gene) %>% 
            t_test(frequency ~ subject_id, paired = TRUE) %>% 
            adjust_pvalue(method = "BH") %>% 
            add_significance()
