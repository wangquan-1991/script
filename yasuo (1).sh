for file in `ls -d */`
do
        file=${file%%/}
        tar --use-compress-program="pigz -k -p 6 " -cf $file.tar.gz $file
#        mv $file.tar.gz /tosomewhere/
done
