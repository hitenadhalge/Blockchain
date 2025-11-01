# blockchain_streamlit.py
import streamlit as st
from blockchain import Blockchain

# Initialize blockchain
blockchain = Blockchain()

# Streamlit app title
st.title("Blockchain Donation Tracker")

# Add new block section
st.subheader("Add a new block")
proof_input = st.number_input("Enter proof for new block:", min_value=0, step=1)
if st.button("Add Block"):
    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.new_block(proof=proof_input, previous_hash=previous_hash)
    st.success("Block added successfully!")
    st.json(block)

# Add transaction section
st.subheader("Add a new transaction")
sender = st.text_input("Sender")
recipient = st.text_input("Recipient")
amount = st.number_input("Amount", min_value=0.0, step=0.01)

if st.button("Add Transaction"):
    if sender and recipient and amount > 0:
        index = blockchain.new_transaction(sender, recipient, amount)
        st.success(f"Transaction will be added to Block {index}")
    else:
        st.error("Please provide valid transaction details.")

# Show blockchain
st.subheader("Current Blockchain")
for block in blockchain.chain:
    st.write(f"Block {block['index']}")
    st.json(block)
