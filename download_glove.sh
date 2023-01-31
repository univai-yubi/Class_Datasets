curdir=`pwd`
cd tmp
mkdir glove
cd glove
# need to download glove from http://nlp.stanford.edu/data/glove.6B.zip
wget http://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip
cd $curdir
