
import requests

head = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " 
}



def getSnapshot():
    res  = requests.get('https://api.digitalocean.com/v2/snapshots', headers=head).json()
    for snapshot in res["snapshots"]:
        if "temp" in snapshot["name"]:
            return snapshot['id']

def createDroplet():
    data = {
        "name": "temp",
        "region": "nyc1",
        "size": "s-1vcpu-2gb",
        "image": ""+str(getSnapshot()),
    }
    print(requests.post('https://api.digitalocean.com/v2/droplets', headers=head, json=data ).json())


def getDroplet():
    res = requests.get('https://api.digitalocean.com/v2/droplets/', headers=head).json()
    for droplet in res["droplets"]:
        if "temp" in droplet["name"]:
            return droplet["id"]
def deleteDroplet():
    print(requests.delete('https://api.digitalocean.com/v2/droplets/'+str(getDroplet()), headers=head))


answer = ''

while True:
    commandList = [createDroplet, deleteDroplet]
    answer = input("commands: \n1. create droplet (create the server)\n2. delete droplet (delete server)\n")
    print(commandList[int(answer)-1]())



