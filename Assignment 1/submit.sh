#!/bin/sh

# Function to show usage
function usage() {
    echo "Usage: ./submit.sh ROLL_NO"
    echo "Please run it from the root directory of the assignment."
}

# Function to check if a program is available on $PATH
function check_prog() {
    if ! which $1 > /dev/null; then
	echo "Please install '$1' to continue."
	exit 1
    fi
}

# Read argument and show help
if [ -z $1 ] || [ $1 == "-h" ]; then
    usage
    exit 1
fi

# Useful variables
SECURE_FILE_LIST=("submission.py" "output") # Fill this based on the assignment
ROLL_NO=$1
ASSIGNMENT_NO=1 # Fill this based on the assignment
ASSIGNMENT_DIR=".submit/Assignment $ASSIGNMENT_NO"
GIT_URL="https://github.com/CSE241N-Fall18/CSE241N-ArtificialIntelligenceFall18.git"
KEY_ID="mayank.cse14@iitbhu.ac.in"

# Check if all the useful programs are installed and available
check_prog git
check_prog gpg

# Validate Roll Number
if ! [[ $ROLL_NO =~ ^[0-9]{8}$ ]]; then
    echo "$ROLL_NO is an invalid roll number."
    exit 1
fi

# Check all files exist
for file in "${SECURE_FILE_LIST[@]}"; do
    if ! [ -e "$file" ]; then
	echo "File '$file' does not exist in the current directory."
	echo "Make sure:"
	echo "  - You are running this program from the correct directory."
	echo "  - Have not deleted any important files."
	echo "  - Have created all the necessary output files."
	echo ""
	usage
	exit 1
    fi
done

# Encrypt files
for file in "${SECURE_FILE_LIST[@]}"; do
    if ! gpg --encrypt --recipient "$KEY_ID" "$file"; then
        echo "File '$file' could not be encrypted. See the error above."
	echo "Have you setup GNUPG and imported the key properly?"
	echo ""
	usage
	exit 1
    fi
done

rm -rf .submit
mkdir -p "$ASSIGNMENT_DIR"

# Move the solution files to the repo
cp -r * "$ASSIGNMENT_DIR/"
rm "$ASSIGNMENT_DIR/submit.sh*" # Why submit myself?

# Remove the unsecure versions of all secure files
for file in "${SECURE_FILE_LIST[@]}"; do
    rm "$ASSIGNMENT_DIR/$file"
done

cd .submit
git init
git remote add origin "$GIT_URL"
git checkout -b $ROLL_NO
git pull origin $ROLL_NO
git add .
git commit -m "Submitting Assignment $ASSIGNMENT_NO for $ROLL_NO."
git push origin $ROLL_NO

cd .. && rm -rf .submit
