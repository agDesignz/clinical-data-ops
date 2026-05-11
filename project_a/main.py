from scripts.load_data import load_data
from scripts.validate_data import validate_participants, validate_visits
from scripts.clean_data import clean_participants
from scripts.merge_data import merge_data

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

if __name__ == "__main__":
    main()