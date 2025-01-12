#!/bin/bash

# Script Name: list_contributors_with_years.sh
# Description: Lists all contributors to a specific file in a Git repository along with their first and last contribution years and commit counts.
# Usage: ./list_contributors_with_years.sh <file_path>

# Function to display usage information
usage() {
    echo "Usage: $0 <file_path>"
    echo "Example: $0 src/app/main.py"
    exit 1
}

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Error: Exactly one argument expected."
    usage
fi

FILE_PATH="$1"

# Check if inside a Git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Error: This script must be run inside a Git repository."
    exit 1
fi

# Check if the file is tracked by Git
if ! git ls-files --error-unmatch "$FILE_PATH" > /dev/null 2>&1; then
    echo "Error: File '$FILE_PATH' is not tracked in the current Git repository."
    exit 1
fi

# Retrieve all commits for the file with author name and date
# Format: Author Name <email> | Year
COMMITS=$(git log --follow --format='%aN <%aE>|%ad' --date=format:'%Y' -- "$FILE_PATH")

# Check if there are any commits
if [ -z "$COMMITS" ]; then
    echo "No contributors found for '$FILE_PATH'."
    exit 0
fi

# Declare associative arrays to store data
declare -A FIRST_YEAR
declare -A LAST_YEAR
declare -A COMMIT_COUNT

# Process each commit
while IFS='|' read -r AUTHOR YEAR; do
    # Initialize if author not seen before
    if [ -z "${FIRST_YEAR[$AUTHOR]}" ]; then
        FIRST_YEAR["$AUTHOR"]=$YEAR
        LAST_YEAR["$AUTHOR"]=$YEAR
        COMMIT_COUNT["$AUTHOR"]=1
    else
        # Update first year if current YEAR is earlier
        if [ "$YEAR" -lt "${FIRST_YEAR[$AUTHOR]}" ]; then
            FIRST_YEAR["$AUTHOR"]=$YEAR
        fi
        # Update last year if current YEAR is later
        if [ "$YEAR" -gt "${LAST_YEAR[$AUTHOR]}" ]; then
            LAST_YEAR["$AUTHOR"]=$YEAR
        fi
        # Increment commit count
        COMMIT_COUNT["$AUTHOR"]=$((COMMIT_COUNT["$AUTHOR"] + 1))
    fi
done <<< "$COMMITS"

# Gather all unique authors
AUTHORS=("${!FIRST_YEAR[@]}")

# Sort authors alphabetically
IFS=$'\n' SORTED_AUTHORS=($(sort <<<"${AUTHORS[*]}"))
unset IFS

# Display the results
echo "Contributors to '$FILE_PATH':"
echo "-------------------------------------------------------------"
printf "%-30s %-15s %-15s %-10s\n" "Author" "First Year" "Last Year" "Commits"
echo "-------------------------------------------------------------"

for AUTHOR in "${SORTED_AUTHORS[@]}"; do
    printf "%-30s %-15s %-15s %-10s\n" "$AUTHOR" "${FIRST_YEAR[$AUTHOR]}" "${LAST_YEAR[$AUTHOR]}" "${COMMIT_COUNT[$AUTHOR]}"
done

echo "-------------------------------------------------------------"

exit 0
