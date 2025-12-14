#!/bin/bash
OUTPUT_FILE="activate.sh"
export MLB_PATH="${PWD}"
# Write the content to the file
cat <<EOF > "$OUTPUT_FILE"
export PROJECT_ID=$(gcloud config get-value project)
export LOCATION=us-central1
export MODEL_ID=gemini-2.5-flash
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_GENAI_USE_VERTEXAI=1
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
export GOOGLE_CLOUD_LOCATION=us-central1
# virtual environment path
export VIRTUAL_ENV="$MLB_PATH/.venv"
export PATH="$VIRTUAL_ENV/bin:$PATH"
EOF
# once you have the activate.sh created
source activate.sh