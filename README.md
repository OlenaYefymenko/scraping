## **Web Scraping Project**

Analyzed site: https://interaction24.ixda.org/

### **About structure of the project**

The project consists of several modules organized in the `scraping_project` directory. The main functionality is executed in the `main.py` file.

### **Getting Started**

1. Clone the repository:
    
    ```bash
    git clone git@github.com:OlenaYefymenko/scraping.git
    ```
    
2. Navigate to the project directory:

    
    `cd scraping`
    

1. Set up a virtual environment and install the required dependencies:
    
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install pip-tools
    pip-compile requirements/base.in
    pip-sync requirements/base.txt
    
    ```
    

### **Requirements**

The project uses `pip-tools` for managing dependencies. Here are the key commands:

- `pip install pip-tools`: Installs `pip-tools` in your virtual environment.
- `pip-compile requirements/base.in`: Generates the `requirements/base.txt` file based on the dependencies specified in `requirements/base.in`.
- `pip-sync requirements/base.txt`: Synchronizes the virtual environment with the dependencies listed in `requirements/base.txt`.


### **Future Enhancements**

Here are some potential improvements for this project:

- Add social media information to the scraped data files (LinkedIn, Instagram, others)
- Store Google credentials securely using Google Cloud Storage or implement authentication through GitHub Actions (now there are problems with access when writing to google tables, I need to deal with security issues)
- Add tests and integrate CI pipeline.