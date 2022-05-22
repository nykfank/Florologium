#!
ssh flor Rscript bin/missing.R
rsync flor:missing_dayplot.svg /var/www/florologium

