#!/bin/bash
OUTPUT_FILE="activate.sh"
export SHIPPING_PATH="${PWD}"
# Write the content to the file
cat <<EOF > "$OUTPUT_FILE"
export PROJECT_ID=$(gcloud config get-value project)
export LOCATION=us-central1
export MODEL_ID=gemini-2.5-flash
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
export GOOGLE_CLOUD_LOCATION=us-central1
# virtual environment path
export VIRTUAL_ENV="$SHIPPING_PATH/.venv"
export PATH="$SHIPPING_PATH/bin:$PATH"
EOF
