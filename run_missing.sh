#!
ssh flor Rscript Florologium/missing.R
rsync flor:missing_dayplot.svg /var/www/florologium

