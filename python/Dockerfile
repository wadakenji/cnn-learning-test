FROM --platform=linux/arm64/v8 python:3.13 as develop
RUN python -m pip install -U pip
RUN python -m pip install tensorflow -f https://files.pythonhosted.org/packages/ea/4c/c1aa90c5cc92e9f7f9c78421e121ef25bae7d378f8d1d4cbad46c6308836/tensorflow-2.20.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
RUN python -m pip install numpy pillow matplotlib
WORKDIR /cnn-learning-test

FROM public.ecr.aws/lambda/python:3.13 as lambda
RUN pip install tensorflow numpy pillow matplotlib
COPY src ${LAMBDA_TASK_ROOT}/src
CMD ["src.lambda.handler"]