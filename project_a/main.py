from scripts.load_data import load_data
from scripts.validate_data import validate_participants, validate_visits
from scripts.clean_data import clean_participants
from scripts.merge_data import merge_data
from scripts.monthly_report import create_monthly_report
from scripts.overdue_visits import get_overdue_visits
from scripts.output_csv_file import output_csv_file

def main():
    # Load all DataFrames
    participants = load_data("participants")
    visits = load_data("visits")
    assessments = load_data("assessments")

    # Validate 'participants' and 'visits'
    # Errors will be flagged, but the pipeline will continue
    validate_participants(participants)
    validate_visits(visits)

    # Clean the participants data
    participants = clean_participants()

    # Merge tables: left-merge, rename 'date' cols in visits and assessments
    full_table = merge_data(participants, visits, assessments)

    # Monthly enrollment report
    monthly_report = create_monthly_report(full_table)

    # Overdue Visits
    overdue, no_visits = get_overdue_visits(full_table)

    # Output files
    output_csv_file(participants, "participants_clean")
    output_csv_file(overdue, "overdue_visits")
    output_csv_file(no_visits, "no_visits")
    output_csv_file(monthly_report, "monthly_enrollment")
    output_csv_file(full_table, "full_dataset")

if __name__ == "__main__":
    main()