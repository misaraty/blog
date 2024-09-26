#!/bin/bash
tar -zxvf gsl-2.4.tar.gz && cd ./gsl-2.4 &&./configure --prefix=$(pwd)&&make -j&&make install &&cd ../&& cp -r ./gsl-2.4/include ./gsl-2.4/lib $(pwd) && rm -rf ./gsl-2.4 #&& rm -rf ./gsl-2.4.tar.gz
echo "The gsl's location is" $(pwd)'.'
cat >> $HOME/.bashrc <<EOF
#gsl
export C_INCLUDE_PATH=$(pwd)/include:\$C_INCLUDE_PATH
export LD_LIBRARY_PATH=$(pwd)/lib:\$LD_LIBRARY_PATH
export LIBRARY_PATH=$(pwd)/lib:\$LIBRARY_PATH
EOF
source ~/.bashrc
echo "The gsl's environment variable has been added to ~/.bashrc."
echo "test gsl……"
gcc test.c -lgsl -lgslcblas -O2 -Wall -o test.out && ./test.out && rm -rf test.out