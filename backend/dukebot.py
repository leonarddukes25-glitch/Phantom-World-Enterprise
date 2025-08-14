import time, traceback
import firebase_admin
from firebase_admin import credentials, firestore

# ---- INIT ----
cred = credentials.Certificate("SERVICEACCOUNTKEY.json")  # your key in this folder
firebase_admin.initialize_app(cred)
db = firestore.client()

BOT_DOC = db.collection("Dukes").document("TEST")
CMD_COL = db.collection("commands")  # each doc = one command

def set_status(status:str, note:str=""):
    BOT_DOC.set({
        "STATUS": status,
        "NOTE": note,
        "LAST_SEEN": firestore.SERVER_TIMESTAMP,
    }, merge=True)

def handle_command(cmd_doc):
    data = cmd_doc.to_dict() or {}
    cmd_id = cmd_doc.id
    ctype = (data.get("type") or "").lower()
    args  = data.get("args") or {}

    # mark in-progress
    cmd_doc.reference.set({
        "status": "running",
        "started_at": firestore.SERVER_TIMESTAMP,
    }, merge=True)

    # ---- basic commands ----
    if ctype == "ping":
        result = {"pong": True}
    elif ctype == "set_status":
        new_status = str(args.get("value", "ONLINE"))
        set_status(new_status, note=f"set by command {cmd_id}")
        result = {"ok": True, "status": new_status}
    else:
        raise ValueError(f"Unknown command type: {ctype}")

    # mark done
    cmd_doc.reference.set({
        "status": "done",
        "result": result,
        "finished_at": firestore.SERVER_TIMESTAMP,
    }, merge=True)

def poll_commands():
    # oldest pending command
    q = CMD_COL.where("status", "==", "pending").order_by("created_at").limit(1).stream()
    for doc in q:
        handle_command(doc)

def main():
    set_status("ONLINE", note="DukeBot process started")
    print("DukeBot ONLINE. Watching for commands…")
    while True:
        try:
            poll_commands()
            set_status("ONLINE")  # heartbeat
        except Exception as e:
            traceback.print_exc()
            set_status("ERROR", note=str(e))
        time.sleep(3)

if __name__ == "__main__":
    main()
