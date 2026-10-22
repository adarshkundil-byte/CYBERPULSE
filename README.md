# CYBERPULSE — Predictive Security & Exposure Intelligence

Student portfolio project: asset inventory, vulnerability management, explainable risk
scoring, attack-path analysis and reporting. **Status: Phases 1–2 of 8 (core app + asset
management).** All demo data is synthetic and labeled.

Requires Python 3.10 or newer.

## Install (Linux / Kali)
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # then set SECRET_KEY
python -c "import secrets; print(secrets.token_hex(32))"   # paste into .env
flask --app run init-db
flask --app run seed-demo
python run.py                 # http://127.0.0.1:5000
python -m pytest -q
```

## Install (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
flask --app run init-db
flask --app run seed-demo
python run.py
python -m pytest -q
```

## Reset the demo data
`flask --app run seed-demo` deletes only records flagged as demo, then reloads the original set.

## Security notes
- Local development server only; never expose it to the public internet.
- No authentication yet (planned for Phase 8). CSRF, output escaping, input validation and
  security headers are in place.
