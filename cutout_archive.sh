#!
cp /var/www/florologium/cutout/* /var/www/florologium/cutout_noon/
sed 's/cutout/cutout_noon/g' /var/www/florologium/cutout/table.html >/var/www/florologium/cutout_noon/table.html
