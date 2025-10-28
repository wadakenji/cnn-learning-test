FROM --platform=linux/arm64/v8 python:3.10.14 as develop
RUN python -m pip install -U pip
RUN python -m pip install tensorflow==2.10.0 -f https://files.pythonhosted.org/packages/0e/13/2845290e969d5482dab4a2a8934560043d19329fd1d5af9f9a84ab3042c5/tensorflow-2.10.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
RUN python -m pip install "numpy<2" pillow matplotlib
WORKDIR /cnn-learning-test

FROM public.ecr.aws/lambda/python:3.13 as lambda
RUN pip install tensorflow numpy pillow matplotlib
COPY src/lambda.py ${LAMBDA_TASK_ROOT}
CMD ["lambda.handler"]