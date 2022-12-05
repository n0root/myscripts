#!/bin/bash

###############################
# перейти в директорию path
# посчитать количество файлов
# если файлов n или больше n
# очистить директорию path
###############################

path='/home/user/test/testdir'
n=4

cd $path
COUNT=$(ls | wc -l)

if [[ "$COUNT" == "$n" ]]; then

	cd $path
	rm -rf *
fi

