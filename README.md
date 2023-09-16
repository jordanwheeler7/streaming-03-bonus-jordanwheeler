# streaming-03-bonus-jordanwheeler

- Jordan Wheeler
- CSIS 44671: Streaming Data
- 7 September 2023
- Module 3 Bonus Assignment
- Original Datasource can be found on [Kaggle](https://www.kaggle.com/datasets/nurielreuven/boeing-historical-airplane-orders-deliveries).
- [Repository Page](https://jordanwheeler7.github.io/streaming-03-bonus-jordanwheeler/)

## Assignment Description
The goal of this bonus assignment is to create a continuous stream of data from a static file. The data is a list of Boeing aircraft orders and deliveries from 1965 to 2020. The data being streamed is in a CSV file. We utilize RabbitMQ and a producer file to create a queue and then stream the data from the CSV file to the queue. We then use a consumer to read the data from the queue and print it to the console.

## The Process
1. We created a virtual environment to install the necessary packages. We use the following command to create the virtual environment:
```python -m venv .venv``` and then '.venv\Scripts\activate' to activate the virtual environment.
2. Install required packages using the following command: ```pip install -r requirements.txt```
3. Add our dataset to the project folder.
4. Create a producer.py file to read the data from the CSV file and send it to the queue. This file used a combination of the code from the previous two assignments. We utilized 'v1_emit_message.py' from the Module 3 repo and 'process_streaming_0.py' from the Module 2 repo.
5. Create a consumer.py file to read the data from the queue and print it to the console. This file used the code from 'v1_listen_for_message.py' from the Module 3 repo and process_streaming_0.py from the Module 2 repo. This is the file that receives the message and prints it to the console. It then prints to a new CSV file as new data is received.
6. Run the producer.py file to send the data to the queue. 
7. Run the consumer.py file to read the data from the queue and print it to the console.

![Multiple Terminal Windows](/multiple_terminal_bonus.png)
