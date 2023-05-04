"""
@author: Percy Brown
@date: 25th November 2021

Task: Developing and deploying a web application (containing APIs) using docker.
"""

#Import relevant modules
from flask import Flask, request, render_template
import json

"""
Creates the Flask application object, which contains data about the application and also methods (object functions) that tell
the application to do certain actions
"""
app = Flask(__name__)

app.config["DEBUG"] = True  # Starts the debugger

# Home route
@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')


"""
Helper method: permission_cases(binary)
This function takes the binary bits in a list, and replaces them with the corresponding permissions.
"""

def permission_cases(binary):
    bits = [int(x) for x in binary]
    if bits[0] == 1:
        bits[0] = 'read'
    if bits[1] == 1:
        bits[1] = 'write'
    if bits[2] == 1:
        bits[2] = 'execute'
    perms = list(filter(lambda a: a != 0, bits))
    return perms

"""
This function accepts the permission code as parameter
Returns a JSON object specifying the groups and their corresponding permissions
"""

def permissions(code):
    if len(code) !=3:
        permissions = "Error: The code must be 3 digits long."
        return permissions
    elif not (code.isdecimal()):
        permissions = "Error: The code must contain only digits."
        return permissions
    elif any([int(ch)>7 for ch in code]):
        permissions = "Error: The API works with 3 bits. Therefore, enter characters between from 0 to 7 only."
        return permissions
    else:
        digits = [int(x) for x in code]
        bits = map(lambda value: format(value, '03b'), digits)
        bitlist = list(bits)
        permissions = {'owner': bitlist[0], 'group': bitlist[1], 'other': bitlist[2]}
        permissions.update({k: permission_cases(v) for k, v in permissions.items()})
        permissions = json.dumps(permissions)
        return permissions

"""
Permissions Code API Routing
/permissions?code=<number>
This API method accepts a code given by number and returns a JSON object specifying the permissions represented for owner, group and other.
"""

@app.route('/permissions', methods = ['GET'])
def permissions_api():
    if len(request.args)>0:  
        if 'code' in request.args:
            code = request.args['code']
            return render_template('permission.html', message = permissions(code))
        else:
            return render_template('permission.html', message = "Error: No permission code identified. Please specify request as eg. /permissions?code=777")
    return render_template('permission.html', message="Please specify request as eg. /permissions?code=777")

"""
This method accepts the 4 disk block bits as parameters
Returns parity bits
"""

def parity(b1,b2,b3,b4):
    b1 = int(b1)
    b2 = int(b2)
    b3 = int(b3)
    b4 = int(b4)
    parity_bits = b1 ^ b2 ^ b3 ^ b4
    return parity_bits

"""
Parity Bits API Routing
/parity?b1=<bits>&b2=<bits>&b3=<bits>&b4=<bits>
This API method accepts the bits on corresponding disk blocks of a RAID-4 and returns the parity bits. Assume that each block has two bits. 
"""

@app.route('/parity', methods =['GET'])
def parity_api():
    if len(request.args)>0:  
            
        if 'b1' in request.args and 'b2' in request.args and 'b3' in request.args and 'b4' in request.args and len(request.args) == 4:
            b1  = request.args.get('b1')
            b2  = request.args.get('b2')
            b3  = request.args.get('b3')
            b4  = request.args.get('b4')
            if len(b1)!=2 or len(b2)!=2 or len(b3)!=2 or len(b4)!=2:
                return render_template('parity.html', message="Error: Make sure all disk blocks are represented by 2 bits")
            if all(c in '01' for c in b1) and all(c in '01' for c in b2) and all(c in '01' for c in b3) and all(c in '01' for c in b4):
                return render_template('parity.html', message="Parity bits: "+ str(parity(b1,b2,b3,b4)).zfill(2))
            else:
                return render_template('parity.html', message="Error: Some numbers are non-binary. Kindly check and ensure all bits are in 0s and 1s")
        else:
            return render_template('parity.html', message="Error: Disk blocks are not exactly 4. Make sure the bits represent 4 disk blocks.")
    return render_template('parity.html', message="Please specify request as eg. /parity?b1=<bits>&b2=<bits>&b3=<bits>&b4=<bits>")

if __name__ =='__main__':
    app.run()