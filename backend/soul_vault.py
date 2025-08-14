
# soul_vault.py
# Duke Bot Trinity Core → Soul Vault (Firestore) logger
# Requires: pip install firebase-admin

import uuid, hashlib, json, datetime as dt
from typing import Dict, Any

import firebase_admin
from firebase_admin import credentials, firestore

class SoulVault:
    def __init__(self, service_account_path: str):
        """Initialize Firebase Admin and prepare collection handle."""
        if not firebase_admin._apps:
            cred = credentials.Certificate(service_account_path)
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.col = self.db.collection("soul_vault_runs")

    @staticmethod
    def _iso_now():
        return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    @staticmethod
    def _hash(record: Dict[str, Any]) -> str:
        blob = json.dumps(record, sort_keys=True).encode("utf-8")
        return hashlib.sha256(blob).hexdigest()

    def log_cycle(self, scenario: str, inputs: Dict[str, Any], outputs: Dict[str, Any], status: str = "complete", meta: Dict[str, Any] = None) -> str:
        """Persist a completed Trinity cycle to Firestore and return the run_id."""
        doc = {
            "run_id": str(uuid.uuid4()),
            "ts": self._iso_now(),
            "scenario": scenario,
            "inputs": inputs,
            "outputs": outputs,
            "status": status,
            "meta": meta or {}
        }
        doc["hash"] = self._hash(doc)
        self.col.document(doc["run_id"]).set(doc)
        return doc["run_id"]
