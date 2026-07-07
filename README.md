## Running HELIOS Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd HELIOS
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

The API key is only required when running HELIOS in **DEMO mode**.
**SAFE mode runs completely offline without making Gemini API calls.**

### 5. Launch the application

```bash
streamlit run helios/app.py
```

The HELIOS dashboard will open in your browser.

### Execution Modes

* **SAFE Mode**

  * Fully offline execution.
  * Uses deterministic agents and simulated routing.
  * No external API calls.

* **DEMO Mode**

  * Enables live Gemini-powered planning, routing, and execution.
  * Requires a valid `GEMINI_API_KEY`.

### Running Tests

To verify the system:

```bash
pytest
```

Expected result:

```
12 passed
```
