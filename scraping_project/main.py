"""Basic script in the project."""
from scraping_and_save import core_team_data, save_to_csv, save_to_json
from write_to_google_sheet import create_sheets_service, write_to_sheet


def main():
    """Scrape team data, save it to CSV and JSON, upload to Google Sheets."""
    # Get team data from the website
    core_team_info = core_team_data('https://interaction24.ixda.org/')

    # Save data to CSV and JSON files
    save_to_csv(core_team_info, 'team_data.csv')
    save_to_json(core_team_info, 'team_data.json')

    # Create Google Sheets service instance
    sheets_service = create_sheets_service()

    # Upload data to Google Sheets
    spreadsheet_id = '19P2V7zcbwMGw7lI65YCxhwtcSCM3pdh8CKTwwpGxBa0'
    range_name = 'Sheet1!A1'
    data = [['Name', 'Role', 'Image URL']] + [[member['name'], member['role'],
                                               member['image']] for member
                                              in core_team_info]
    write_to_sheet(sheets_service, spreadsheet_id, data, range_name)


if __name__ == "__main__":
    main()
