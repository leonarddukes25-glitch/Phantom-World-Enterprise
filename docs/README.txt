
DUKE BOT TRINITY CORE → SOUL VAULT INTEGRATION

Quick Steps
1) Install deps:
   pip install -r requirements.txt

2) Get Firebase service account JSON:
   Firebase Console → Project Settings → Service accounts → Generate new private key
   Save it to: config/firebase-key.json  (or any path you choose)

3) Open duke_trinity_core.py and set SERVICE_ACCOUNT_JSON to your path.

4) Run:
   python duke_trinity_core.py

5) Verify:
   Firestore → Data → collection 'soul_vault_runs' contains a new document.
