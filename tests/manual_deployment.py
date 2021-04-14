#!/usr/bin/env python3

# ==============================================================================
# 
import freeton_utils
from   freeton_utils import *
from   contract_DnsRecord import DnsRecord
from  pprint import pprint

TON    = 1000000000
SERVER = "http://localhost"
freeton_utils.asyncClient = TonClient(config=ClientConfig(network=NetworkConfig(server_address=SERVER)))

# ==============================================================================
# 
# Create a DnsRecord class with "freeton" name
domain = DnsRecord(name="freeton")

# Create a Multisig class with a random keypair
msig   = Multisig(signer=loadSigner(keysFile="msig.json"))

# If you want Multisig with a keypair from file, use this syntax:
#msig = Multisig(signer=loadSigner(keysFile="msig.json"))

# Giver for TON OS SE
giverGive(contractAddress=domain.ADDRESS, amountTons=TON*1)
giverGive(contractAddress=domain.ADDRESS, amountTons=TON*1)

# Deploy DnsRecord with Multisig address as owner; please note, "0:" is removed from owner to keep only uint256;
result = domain.deploy(ownerID = "0x" + msig.ADDRESS[2:])
pprint(result[0].transaction)
pprint(result[1])

# Check Whois
result = domain.run(functionName="getWhois", functionParams={})
pprint(result)

# To call any DnsRecord function from Multisig use this syntax:
#domain.callFromMultisig(msig=msig, functionName="claimExpired",  functionParams={"newComment":stringToHex("custom comment")}, value=100000000, flags=1)
#domain.callFromMultisig(msig=msig, functionName="changeComment", functionParams={"newOwnerID":"0x" + msig.ADDRESS[2:]}, value=100000000, flags=1)
