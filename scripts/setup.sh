#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m' 

echo -e "${BLUE}📂 Checking and creating directory structure for research project...${NC}\n"

directories=(
  "data/logs"
  "data/preprocessed"
  "data/raw"
  "data/training"
  "models"
)

for dir in "${directories[@]}"; do
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
    echo -e "${GREEN} - Created: $dir${NC}"
  else
    echo -e "${YELLOW} ⏭ Skipped: $dir (already exists)${NC}"
  fi
done

echo -e "\n${GREEN}✅ Directory structure setup complete!${NC}\n"