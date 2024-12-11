#!/bin/bash

# Define the arguments from input
ARG1="$1"
ARG2="$2"

# Display help instructions if requested
if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    echo "Usage: $0 [ARG1] [ARG2]"
    echo
    echo "This script takes two arguments and runs the Reddit Topics application."
    echo "ARG1: url with a formate of https://www.reddit.com/r/<subreddit_name>.json?limit=<the number of desired posts> to the Reddit comments dataset. The dataset should be in JSON format."
    echo "ARG2: The path where the output wordcloud image will be saved."
    echo
    echo "Instructions:"
    echo "- Ensure you have Spark installed on your system."
    echo "- Run the script from the root directory of the application."
    echo "- Verify that all dependencies are correctly installed before starting the application."
    echo "- If any errors occur, check the error messages for guidance on resolving them."
    exit 0
fi

# Run the Python script with the arguments
python3 app/app.py $ARG1 $ARG2