"""Module for writing data to the Google Sheets."""
import os
import pandas
import json
import logging
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

logging.basicConfig(level=logging.INFO)

# Doesn't work :(
# CREDENTIALS_FILE = os.environ.get('GOOGLE_CREDENTIALS_FILE')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# this token isn't valid, it should be changed to another security variant
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'scraping_project', 'cred',
                                'client_secret.json')  


def create_sheets_service():
    """Create an instance of the Google Sheets API service."""
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, scopes)
    credentials = flow.run_local_server(port=0)
    service = build('sheets', 'v4', credentials=credentials)
    return service


def write_to_sheet(service, spreadsheet_id, data, range_name):
    """Write data to Google Sheets."""
    body = {
        'values': data
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption='RAW', body=body
    ).execute()
    logging.info(f'Wrote {len(data)} rows to {spreadsheet_id}')

