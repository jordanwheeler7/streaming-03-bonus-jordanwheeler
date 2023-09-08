"""
Jordan Wheeler
7 September 2023
Module 3 Bonus

This program will prepare and emit a message based on the orders_deliveries.csv file utilizing the RabbitMQ server.

"""

# add imports as needed
import logging
import csv
import time
import pika
import sys
import os

# set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

# Define program information

HOST = 'localhost'
INPUT_FILE_NAME = 'orders_deliveries.csv'
QUEUE_NAME = 'hello'

# Setup RabbitMQ connection and channel

logging.info(f'Connecting to RabbitMQ at {HOST}')
conn = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
ch = conn.channel()
logging.info(f'Connected to RabbitMQ at {HOST}')

# Setup the queue
ch.queue_declare(queue=QUEUE_NAME)

# Define a function to get the message information
def get_message_information(input_file_name, host, queue_name):
    """Read the information from the input file and emit the message to the queue."""
    logging.info(f'Reading information from {input_file_name}')
    with open(input_file_name, 'r') as input_file:
        reader = csv.reader(input_file)
        header = next(reader) # skip the header row
        logging.info(f'Header: {header}')
        
        # Loop through the rows in the file and emit a message for each row
        for row in reader:
            message = ', '.join(row)
            logging.info(f'Emitting message: {message}')
            
            # Emit the message to the queue
            ch.basic_publish(exchange='', routing_key=queue_name, body=message)
            logging.info(f'Sent Message: {message}')
            time.sleep(2) # wait 2 seconds before emitting the next message

    # Close the connection to RabbitMQ
    conn.close()
    
    #=====================================================================================================
    
    #                               Setup the main code block
    
    #=====================================================================================================
    
if __name__ == '__main__':
    try:
        logging.info("=========================================")
        logging.info(f'Running get_message_information function')
        get_message_information(INPUT_FILE_NAME, HOST, QUEUE_NAME)
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)