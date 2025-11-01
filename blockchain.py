import streamlit as st
import hashlib, datetime

st.set_page_config("Blockchain Ledger", layout="wide")
st.markdown("""
<style>
body{background:linear-gradient(135deg,#f7f9fc,#eef2f6);color:#111;font-family:Inter, sans-serif}
.header{color:#2b2d42;text-align:center;margin-bottom:6px}
.card{background:#fff;border-radius:12px;padding:14px;margin-bottom:12px;box-shadow:0 6px 18px rgba(36,59,85,0.08)}
.stButton>button{background:#4b6cb7;color:#fff;border-radius:8px;padding:8px 12px}
code{background:#f1f5f9;padding:2px 6px;border-radius:6px;color:#0f172a}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header'>Blockchain Ledger</h1>", unsafe_allow_html=True)
st.write("A minimal demo showing chained blocks with SHA-256 hashes.")
st.sidebar.header("Add Transaction")
s = st.sidebar.text_input("Sender")
r = st.sidebar.text_input("Receiver")
a = st.sidebar.text_input("Amount")

if "prev" not in st.session_state:
    st.session_state.prev = "0000"
if "n" not in st.session_state:
    st.session_state.n = 0
if "chain" not in st.session_state:
    st.session_state.chain = []

def h(x): return hashlib.sha256(x.encode()).hexdigest()

if st.sidebar.button("Add Block"):
    if not (s and r and a):
        st.sidebar.error("Fill all fields")
    else:
        st.session_state.n += 1
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"{st.session_state.n}|{s}|{r}|{a}|{st.session_state.prev}|{ts}"
        hh = h(data)
        st.session_state.chain.append({
            "n": st.session_state.n, "s": s, "r": r, "a": a, "ts": ts,
            "prev": st.session_state.prev, "hash": hh
        })
        st.session_state.prev = hh
        st.sidebar.success("Block added")

st.subheader("Ledger")
if not st.session_state.chain:
    st.info("No blocks yet — add one from the sidebar.")
else:
    for blk in reversed(st.session_state.chain):
        st.markdown(f"""
        <div class="card">
        <b>Block #{blk['n']}</b><br>
        Sender: {blk['s']} &nbsp;|&nbsp; Receiver: {blk['r']} &nbsp;|&nbsp; Amount: {blk['a']}<br>
        <small>Time: {blk['ts']}</small><br>
        Prev: <code>{blk['prev']}</code><br>
        Hash: <code>{blk['hash']}</code>
        </div>
        """, unsafe_allow_html=True)

if st.sidebar.button("Clear Ledger"):
    st.session_state.chain = []; st.session_state.prev = "0000"; st.session_state.n = 0
    st.sidebar.info("Cleared")
