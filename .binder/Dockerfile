FROM jupyter/minimal-notebook

# Install any dependencies (if required)
RUN pip install dash plotly

# Copy the project files to the Docker image
COPY . /home/jovyan/app
WORKDIR /home/jovyan/app

# Run the start script when the container launches
CMD ["./start"]
