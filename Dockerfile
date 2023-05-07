FROM python:3.10

# Create and set the working directory
RUN mkdir /twitter_reloaded
WORKDIR /twitter_reloaded

# Install dependencies
COPY requirements.txt /twitter_reloaded/
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . /twitter/reloaded/

# Expose the port the app runs on
EXPOSE 8000

# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "twitter_reloaded.wsgi"]

