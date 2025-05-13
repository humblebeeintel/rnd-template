# Computer Vision R&D Template

This is a base template for computer vision projects focused on Research and Development of the projects.

## ✨ Features

- Base structure
- Custom configuration
- Common recommended files and folders
- Best practices

## 🚀 Quick Start

```bash
# Clone the template

git clone https://github.com/humblebeeintel/rnd-template.git my_project
cd my_project

# Setup environment

python -m venv .venv
source .venv/bin/activate  

# Windows: 
# .venv\Scripts\activate

# Install dependencies (choose one)

pip install -r requirements/requirements.cpu.txt  # For CPU
pip install -r requirements/requirements.cuda.txt  # For GPU

# Initialize project structure

chmod +x ./scripts/setup.sh && ./scripts/setup.sh

# Create your .env file for credentials

cp .env.example .env
```

## 📂 Project Structure

```.
├── configs/              # Your configuration files
├── data/                 # Data files (gitignored)
├── experiments/          # Notebooks and experiment code
├── models/               # Saved models
├── modules/              # Reusable code
├── scripts/              # Utility scripts
├── .env                  # Environment variables
└── config.py             # Configuration management
```

## 💡 How to use this template

### 📦 Use [modules](modules) for external source code

> GitHub repositories or open-source packages that aren't on PyPI but are useful for your workflow

### Integrate an external GitHub repo to the template

```bash
cd modules
git clone https://github.com/some-user/some-cv-library.git
```

Then you can import it in your code like:

```bash
from modules.some_cv_library import some_module
```

**Tip**: Keep external modules in their own subfolders to avoid namespace issues and make version control easier.

### ⛰️ Environment Variables (.env)

> Define API keys and sensitive information:

```
API_KEY=your_secret_key
DATASET_PATH=/path/to/data
```

**Important:** Make sure you don't commit it to GitHub and you have it in the `.gitignore` file

## 📝 Documentation

- Check `docs/` for detailed documentation
- Example notebooks are in `experiments/notebooks`
- Common modules are in `modules/` directory

## ✨ Other considerations

- Add your data to `data/`
- Create preprocessing scripts in `scripts/`
- Build your model or move pre-trained models to `models/` 
- Track experiments with logging
