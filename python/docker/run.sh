docker run cnn-learning-test \
  --mount type=bind,src="$(pwd)"/src,dst=/cnn-learning-test/src \
  --name cnn-learning-test \
  -it /bin/bash