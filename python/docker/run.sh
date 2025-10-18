docker run \
  --mount type=bind,src="$(pwd)"/src,dst=/cnn-learning-test/src \
  --name cnn-learning-test \
  -it \
  cnn-learning-test