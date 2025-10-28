docker run \
  -p 9000:8080 \
  --mount type=bind,src="$(pwd)"/src,dst=/task/src \
  --name cnn-learning-test-lambda \
  cnn-learning-test-lambda