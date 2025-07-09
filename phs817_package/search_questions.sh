#!/bin/bash

# Create output directory
mkdir -p answers

# Questions extracted from your exam paper (PHS817)
questions=(
  "conditions governing workers’ health surveillance"
  "developing an accident recording and investigation system"
  "Risk Identification"
  "Risk Assessment"
  "Silicosis"
  "Asbestosis"
  "occupational infections"
  "return-to-work health assessment"
  "monitoring sickness-related absence from work"
  "ethical and legal issues in workplace"
  "first aid techniques for head and eye injuries in the workplace"
)

# Loop through questions and search PubMed
for q in "${questions[@]}"; do
  echo "Searching for: $q"
  safe_name="${q// /_}"  # replace spaces with underscores
  esearch -db pubmed -query "$q" | efetch -format abstract > "answers/${safe_name}.txt"
  echo "Saved: answers/${safe_name}.txt"
done
