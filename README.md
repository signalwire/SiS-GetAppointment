# SiS Blog - Expanding SW's Call Flow Builder with an AI agent


## Prerequisites
- Python 3.x
- pip (Python Package Manager)
- [ngrok](https://ngrok.com/) (for setting up a tunnel to your local server)

## Setup and Installation

### Clone the Repository
Clone the repository to your local machine using:

```bash
git clone [Your-Repository-URL]
cd [Repository-Name]
```
### Virtual Environment Setup

Run the following commands to create a virtual environment and activate it:

``` bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies:

``` bash
pip install -r requirements.txt
```

### Running the Application
To start the server, run:

```bash
python app.py
```

### Setting up a NGROK tunnel to your local server:


1 - Download and install ngrok from ngrok's website.

2 - In a separate terminal, start the tunnel and set the http port to 8080.
    
```bash
ngrok http 8080
```

### Configure SignalWire's AI Agent:

1 - Navigate to the AI agent's function tab

2 - In the webhook input section, paste the copied ngrok URL

3 - Append the /get_appointment endpoint to this URL. For example, if your ngrok URL is http://12345.ngrok.io, you will enter http://12345.ngrok.io/get_appointment.

4 - Save the Configuration: Save the changes to update the webhook settings in your SignalWire AI agent.

