FROM public.ecr.aws/lambda/python:3.12

# Copy function code to the Lambda root
COPY ./app ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using requirements.txt
COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" -U --no-cache-dir

# Set the CMD to your handler
CMD ["main.handler"]
