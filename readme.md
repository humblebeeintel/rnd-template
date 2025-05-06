# Computer Vision R&D Template

A streamlined template for computer vision projects with everything you need to start coding quickly.

## ✨ Why Use This Template?

- **Save time** - Pre-configured project structure so you can focus on your algorithms
- **Best practices** - Follows industry standards for CV project organization
- **Beginner-friendly** - Simple configuration and clear examples to get started fast

## 🚀 Quick Start

```bash
# Clone the template
git clone https://github.com/humblebeeintel/rnd-template.git my_project
cd my_project

# Setup environment
python -m venv .venv # or use conda 
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies (choose one)
pip install -r requirements/requirements.cpu.txt  # For CPU
pip install -r requirements/requirements.cuda.txt  # For GPU

# Initialize project structure
./scripts/setup.sh  # Make executable first with: chmod +x scripts/setup.sh

# Create your .env file for credentials
cp .env.example .env
```

## 📂 Project Structure

```
.
├── configs/              # Your configuration files
├── data/                 # Data files (gitignored)
├── experiments/          # Notebooks and experiment code
├── models/               # Saved models
├── modules/              # Reusable code
├── scripts/              # Utility scripts
├── .env                  # Environment variables (create from .env.example)
└── config.py             # Configuration management
```

## 💡 Working With This Template


### 📦 modules/ – Your Custom and External Code Hub

The modules/ directory is where all reusable components and helper functions live. This helps keep your project modular and maintainable.

#### 🧱 What Goes Here?

Utility functions – e.g., image preprocessing, data augmentation

Custom modules – e.g., your own neural network layers, loss functions

Reusable code – anything you expect to use in multiple experiments

Third-party code – GitHub repositories or open-source packages that aren't on PyPI but are useful for your workflow

#### 📅 Downloading External Repos?

If you're integrating a GitHub repo (e.g., for a model architecture or dataset tools), clone it directly inside the modules/ folder:

```bash
cd modules
git clone https://github.com/some-user/some-cv-library.git
```

Then you can import it in your code like:

```bash
from modules.some_cv_library import some_module
```
Tip: Keep external modules in their own subfolders to avoid namespace issues and make version control easier.

### Environment Variables (.env)

For API keys and sensitive information:

```
# .env file example - DO NOT commit to git!
API_KEY=your_secret_key
DATASET_PATH=/path/to/data
```

Access in code:
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
```

## 🔍 Need Help?

- Check `docs/` for detailed documentation
- Example notebooks are in `experiments/notebooks`
- Common modules are in `modules/` directory

## 📝 Next Steps

- Add your data to `data/`
- Create preprocessing scripts in `scripts/`
- Build your model or move pre-trained models to `models/` 
- Track experiments with logging
