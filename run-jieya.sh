#for target in `find ./ -name *tar.gz`
#do
#    tar -zxvf binaries.tar.gz -C `pwd`/
#done
for target in `find ./ -name *tar.gz`
do
    tar -xjvf $target -C `pwd`/
done


