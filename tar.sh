for file in `ls -d */`
do
        file=${file%%/}
        tar -czvf $file.tar.gz $file
        mv $file.tar.gz /job/code/
done
