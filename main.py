#Copyright (c) 2022 IdotMaster1
import json
from time import sleep
import cozmo
from decimal import Decimal
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Get data from Bitco1n RPC
def getinfo():
 rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:22225"%("user", "pass"))
 return rpc_connection.getinfo()

# Show the data
print(getinfo())

# Json stuff
#data = json.loads(getinfo())
jtopy=str(getinfo())

# Split the string
j = jtopy[:251]
j1 = jtopy[251:]

# Cozmo! Do this!
def cozmosay1(robot: cozmo.robot.Robot):
 robot.say_text(j).wait_for_completed()

def cozmosay2(robot: cozmo.robot.Robot):
 robot.say_text(j1).wait_for_completed()

# No! Now do this!
cozmo.run_program(cozmosay1)
sleep(1)
cozmo.run_program(cozmosay2)
